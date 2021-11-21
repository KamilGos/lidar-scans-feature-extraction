
<!-- image -->
<div align="center" id="top"> 
    <img src=images/Figure_1.png width="350" />
  <img src=images/Figure_6.png width="350" />
  &#xa0;
</div>

<h1 align="center"> lidar-scans-feature-extraction </h1>
<h2 align="center"> Gradient based feature extraction for laser scans </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
    <img alt="Repository size" src="https://img.shields.io/github/languages/code-size/KamilGos/lidar-scans-feature-extraction?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#microscope-tests">Tests</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#eyes-implementation">Implementation</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>


## :dart: About ##
Script for extracting features (corners) in laser data (eg. 360 lidar scans). Script is based on gradient technique. The designed algorithm works very good with corner detection task. The examples show that the algorithm finds the corners correctly. There is only one user-adjusted variable to set - the threshold. It is possible to implement a version of this algorithm with adaptive threshold adjustment, but this could affect its execution speed. The presented algorithm is good for feature-based localisation.


## :package: Content
[features_detection.py](./features_detection.py) - main script
[data](data) - directory with example data

## :microscope: Tests ##
<h2 align="left">'step.json' dataset </h1>
<div align="center" id="step"> 
  <img src=images/step.png width="500" />
  &#xa0;
</div>

---

<h2 align="left">'wall.json' dataset </h1>
<div align="center" id="wall"> 
  <img src=images/wall.png width="500" />
  &#xa0;
</div>

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/KamilGos/lidar-scans-feature-extraction

# Access
$ cd lidar-scans-feature-extraction

# Run the project
$ sudo python3 features_detection.py
```

## :eyes: Implementation ##
To extract corners from given sets of data the gradient-based algorithm was used. The first step was to plot the data in polar scale to see the data that we have to deal with. The data refer to the situation when robot is next to the box. The box is a cube, that has a notch in the middle. On the left there is a wall. In the next step, the data was presented in relation of distance to angle.

Knowing, that the data satisfy the assumptions of the function, then the gradient ofeach measurement was calculated. It can be observed that the gradient local extremescorresponds to the corners. Next step was to filter the gradient values using the thresholdfunction (true value correspond to success corner detection)

```bash
True if gradinet > threshold or gradinet < - threshold
False else
```

The last step is to translate the data from polar to Cartesian coordinate system:

<div align="center" id="inventor"> 
  <img src=images/Figure_3.png width="230" />
  <img src=images/Figure_4.png width="230" />
  <img src=images/Figure_6.png width="230" />
  &#xa0;
</div>

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>