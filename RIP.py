#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:13:54 2018

@author: Leoch
email: liuchi_email@foxmail.com
blog: leoch.xyz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:18:39 2018

@author: Leoch
"""
import os
import cv2
import pickle
import matplotlib.pyplot as plt
import random as rd
import numpy
def rip (filepath, outputpath,method, scale):
    try:

        files = os.listdir(filepath)
        img_list = []
        count = 0
        for file in files:
            if file != '.DS_Store':
    #            print (file)
                img = cv2.imread(filepath+file,1)
                img = cv2.resize(img, (img.shape[0],img.shape[0]))
    #                img = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
                res = scaleRadius(img,scale)            
                
                if method == 'c':
                    print ("CLAHE")
                    res = clahe(res)
                elif method == 'g':
                    print ("GRAY")
                    print ("Warning: channel number of gray image is 1")
                    res = gray(res)
                elif method == 'o':
                    print ("ORIGINAL")
                    print ("No change for images")
                    res = ori(res)
                elif method == 'a':
                    print ("AREMOVE")
                    res = aremove(res,scale)
                count += 1
                print (str(count))
                img_list.append((file, res))          
    #    print (img_list)       
    except AttributeError as e:
        print("Error: Your image folder includes non-image file. You must move it and try again")
#                
    pickle_file = outputpath + "img_list_" + method + ".pkl"    
#    print (pickle_file)
    with open(pickle_file, "wb") as f:
        pickle.dump(img_list, f)
        
    return img_list,count

def scaleRadius(img, scale):
    # resize image into a circle
    s = scale * 1.0/ (img.shape[0]/2)
    return cv2.resize(img, (0,0), fx=s, fy=s)

def clahe(img):
    
    clahe = cv2.createCLAHE(clipLimit=2.0 , tileGridSize=(8,8))
    img_new_1 = clahe.apply(img[:,:,0])
    img_new_2 = clahe.apply(img[:,:,1])
    img_new_3 = clahe.apply(img[:,:,2])
    img_merge = cv2.merge([img_new_1,img_new_2,img_new_3])
    
    return img_merge

def gray(img):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return gray_img

def ori(img):

    return img

def aremove(img,scale):
    crop = scale * 2 * 0.9
    height = img.shape[0]
    width = img.shape[1]
    start = int((height-crop)/2)
    end = int((height-crop)/2+crop)
    mask = numpy.zeros(img.shape)
    cv2.circle(mask,(int(img.shape[1]/2), int(img.shape[0]/2)), int(scale*0.9),(1,1,1),-1,8,0)
    gauss = cv2.GaussianBlur(img,(0,0),scale/30)
    enhanced = cv2.addWeighted(img,4,gauss,-4,128)*mask + 128*(1-mask)
#    img = img*mask + 0*(1-mask)
#    resized_crop = img[(height-crop)/2:(height-crop)/2+crop, (width-crop)/2:(width-crop)/2+crop]
#    enhanced_crop = enhanced[start:end, start:end]
#    enhanced_img = cv2.resize(enhanced_crop,(int(scale*2),int(scale*2)))
    return enhanced
#
def main():
    print ("""
=================================RIP 1.0================================
   A preprocessing tool for retinal images.
   
   Author: Leoch
   Version: 1.0
   Info:
       -filepath: your image folder
       -method: 
           o = original
           c = Contrast-limited adaptive histogram equalization
           g = gray
           a = local color average Gaussian blur removed
       -scale: your image size, an int
       -output path: folder to store your output image array
        
   Output: image_list_method.pkl     
========================================================================\n
           """)
    print ("Begin preprocessing...")    
    print ("\nPlease input your image filepath (you must not ignore the last '/', for example:'/my/file/path/')")
    filepath = input("filepath = ")
    print ("\nPlease input your preprocessing method")
    method = input("method = ")
    while method not in ["c","o","g","a"]:
        print ("Unknown input, try again")
        print ("\nPlease input your preprocessing method")
        method = input("method = ")
    print ("\nPlease input your image scale")
    scale = int(input("scale = "))
    scale = scale / 2.0
#    print (type(scale))
    print ("\nPlease input your output path (you must not ignore the last '/', for example:'/my/file/path/')")
    outputpath = input("output path = ")
    
    img_list, n = rip(filepath,outputpath,method,scale)
    print ("End preprocessing.\n")
    print ("Preprocessed image number is " + str(n) + "\n")
    print ("Preprocessed image size is ",img_list[0][1].shape,"\n")
    print ("Do you want to show a image randomly? ")
    show = input('[y/n]:')
    if show in ['y','Y']:
        index = rd.randint(0,n-1)
#        index = 3
        if method != 'g':
            fig = plt.imshow(img_list[index][1][:,:,::-1])
            plt.show()
        else:
            fig = plt.imshow(img_list[index][1],cmap ='gray')
            plt.show()
    else:
        print ("Bye :)")

if __name__ == "__main__":
    main()

