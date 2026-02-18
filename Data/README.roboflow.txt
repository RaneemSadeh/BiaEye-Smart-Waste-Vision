
Trash Detection For RP - v1 2024-12-07 4:46pm
==============================

This dataset was exported via roboflow.com on December 7, 2024 at 1:51 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 491 images.
Trash are annotated in YOLOv11 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 50 percent of the image
* Random rotation of between -39 and +39 degrees
* Random shear of between -22° to +22° horizontally and -20° to +20° vertically
* Salt and pepper noise was applied to 8.22 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 28 percent of the bounding box
* Random shear of between -10° to +10° horizontally and -10° to +10° vertically
* Random brigthness adjustment of between -20 and +20 percent


