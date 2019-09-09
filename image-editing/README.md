# Kernal Image Editing

This image editing script uses kernel matrices to edit the pixel values of an image to create a new filtered image. Functionality currently includes blurring, sharpening, desharpening, embossing, and outlining images.

## Getting Started

To run this process locally, you must install all of the prerequisites, which should be a straight forward process.

### Prerequisites

**Step 1:** The first thing that is needed if you don't already have it is Python 3.

[Python3](https://www.python.org/downloads/) - The programming language used

**Step 2:** Install the necessary libraries

An easy way to install libraries is using pip. If you have Python 3.4 or newer, pip should be pre-installed, else you can read the instructions to install pip [here](https://pip.pypa.io/en/stable/installing/)

If you have Python 3.4 or newer, run ```python -m pip install SomePackage``` for the following packages. Else if pip was installed seperately, run ```pip install SomePackage``` for the following packages
```
-Numpy (install as numpy)
-Opencv (install as opencv-python)
```

## Running The Program

**Step 1:** Place the image you want to edit into the image-editing directory

**Step 2:** In a terminal, in the image-editing directory, run ```py editing-script.py```

The terminal will display prompts that you must follow, which should be self explanatory

**Step 3:** Once the run is complete, you should be able to find your newly edited image in the image-editing directory
