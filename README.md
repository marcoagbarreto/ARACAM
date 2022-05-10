# ARACAM

## A RGB-D Multi-View Photogrammetry System for Lower Limb 3D Reconstruction Applications
---
## Dependencies:
---
Aracam uses different libraries, install dependencies using PyPi. 

```python
pip install nbimporter
pip install opencv-contrib-python
pip install matplotlib
pip install scikit-image
pip install open3d
pip install pandas
pip install pyvista
pip install pymeshfix
pip install pymeshlab
pip install plotly
pip install kaleido
```

## Pipeline
---
The [main.ipynb](main.ipynb) notebook contains the pipeline of the project and it is structured as follows:

1. [segmentation_color.ipynb](segmentation_color.ipynb) - Selects the desired object by means of depth and color.

2. [to_pointcloud.ipynb](to_pointcloud.ipynb) - Transforms all color and depth pair information into 3D point cloudls.

3. [pointcloud_process.ipynb](pointcloud_process.ipynb) - Reconstructs all poinclouds using ICP algorithm

4. [3D_validation.ipynb](3D_validation.ipynb) - Compares the original mesh obtained from a CT vs the ARACAM


## Model comparisson
---
<b>Original model obtained from a CT image</b> <b>Model obtained from the ARACAM system</b> 
![M1_Original_model](model_demo/M1_Original_model.gif) ![M1_ARACAM_model](model_demo/M1_ARACAM_model.gif)

Comparing models using Hausdorff distances to determine the worst case scenarios. For this model, everything above the cutline is relevant for the comparisson only. 
![hausdorff_model_comparisson](hausdorff_model_comparisson.png)

## Citing 
---
If you use the ARACAM work for a scientific purpose, please cite the following paper.

@Article{s22072443,
AUTHOR = {Barreto, Marco A. and Perez-Gonzalez, Jorge and Herr, Hugh M. and Huegel, Joel C.},
TITLE = {ARACAM: A RGB-D Multi-View Photogrammetry System for Lower Limb 3D Reconstruction Applications},
JOURNAL = {Sensors},
VOLUME = {22},
YEAR = {2022},
NUMBER = {7},
ARTICLE-NUMBER = {2443},
URL = {https://www.mdpi.com/1424-8220/22/7/2443},
PubMedID = {35408058},
ISSN = {1424-8220},
ABSTRACT = {In the world, there is a growing need for lower limb prostheses due to a rising number of amputations caused primarily, by diabetic foot. Researchers enable functional and comfortable prostheses through prosthetic design by integrating new technologies applied to the traditional handcrafted method for prosthesis fabrication that is still current. That is why computer vision shows to be a promising tool for the integration of 3D reconstruction that may be useful for prosthetic design. This work has the objective to design, prototype, and test a functional system to scan plaster cast molds, which may serve as a platform for future technologies for lower limb reconstruction applications. The image capture system comprises 5 stereoscopic color and depth cameras, each with 4 DOF mountings on an enveloping frame, as well as algorithms for calibration, segmentation, registration, and surface reconstruction. The segmentation metrics of dice coefficient and Hausdorff distance (HD) show strong visual similarity with an average similarity of 87% and average error of 6.40 mm, respectively. Moving forward, the system was tested on a known 3D printed model obtained from a computer tomography scan to which comparison results via HD show an average error of &le;1.93 mm thereby making the system competitive against the systems reviewed from the state-of-the-art.},
DOI = {10.3390/s22072443}
}

