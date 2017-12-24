# curbmap-ml
ML aspects of curbmap


## Image Pipeline
----
Problem: A user uploads a photo of multiple street signs in one image.
1. Preprocess
    1. Verify that upload location indicated is related to EXIF data
    2. Contrast Limited Histogram Equalization of image (CLAHE) of LAB image
    3. Reduce image size to max dimension < 2600 using Lanczos4 interpolation sinc approx
    4. Grayscale image (possibly not right to do since some images have Red nos and such)
2. Bounding boxes for signs (CNN)
    1. [RetinaNet](https://github.com/fizyr/keras-retinanet)
    2. Use [COCO trained weights](https://delftrobotics-my.sharepoint.com/personal/h_gaiser_fizyr_com/_layouts/15/guestaccess.aspx?docid=0386bb358d0d44762a7c705cdac052c2f&authkey=AfdlNvj1hPD8ZPShcqUFUZg&expiration=2017-12-28T16%3A09%3A58.000Z&e=5585e7262ac64651bf59990b54b406cd) (430MB - those are massive weights, I guess ResNet 101 would have been 1GB)
    3. Crop segments from image into sub "signs"
3. Orient/upright/straighten the sign in each box
4. Extract the text in the box
5. Determine meaning from the text


## Determine related map information from nearby information
---
Problem: Given a street, can we predict a similar restricted street
1. 
