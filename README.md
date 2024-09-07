# RIP

An automatic tool for Retinal Image Preprocessing.

## Introduction

A preprocessing tool for retinal images.
   
**Author:** Leoch

**Version:** 1.0
   
**Info:**

- filepath: your image folder
- method: 
    1. o = original
    2. c = Contrast-limited adaptive histogram equalization (CLAHE)
    3. g = gray
    4. a = local color average with Gaussian blur removed (LCA)
- scale: your image size, an int
- output path: folder to store your output image array
       
**Output:** image_list_method.pkl     
## Usage

1. Use this tool by typing the below command in your terminal.
```
$ python3 RIP.py
```
2. Then you will get a .pkl file in your output path. Use ```import pickle``` to use it.

```python
import pickle
with open("/out/put/path/yourfile.pkl", "rb") as f:
a = pickle.load(f)
```
## Method comparison
1. original

![o](https://github.com/keepgallop/RIP/blob/master/images/o.png?raw=true)

2. CLAHE

![c](https://raw.githubusercontent.com/keepgallop/RIP/master/images/c.png)

3. gray

![g](https://github.com/keepgallop/RIP/blob/master/images/g.png?raw=true)

4. LCA

![a](https://github.com/keepgallop/RIP/blob/master/images/a.png?raw=true)
