from distutils.core import setup
from setuptools import find_packages
setup(name='uq05itim',
      version='0.1',
      author='DSSS',
      author_email='tuhin.mallick@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])
