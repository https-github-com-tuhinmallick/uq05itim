
import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

interact(imshow, resize=widgets.IntSlider(min=-10, max=30, step=1, value=10));

def imshow(X, resize=None):
"""
 You should create a way to resize an image from an array X.
 The use of widgets is optional but you can take a look to interact.
 We should be able to install this package in Google Colab from your Git
 repo.
 """
    image = Image.fromarray(X, 'RGB')
    im_resized = image.resize((width, height))

    create tabs
tab_nest = widgets.Tab()
tab_nest.set_title(0, 'Image Resize')
return im_resized

