from setuptools import find_packages, setup

setup(
   name='augmentationlib',
   packages=find_packages(include=['augmentationlib']),
   version='0.1.0',
   description='Various image processing performed using NumPy functions. Uses Pillow to read and save image files',
   author='Eujin',
   license='MIT',
   install_requires=[],
   setup_requires=['pytest-runner'],
   tests_require=['pytest==4.4.1'],
   test_suite='tests',
)


