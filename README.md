# curbmap-ml
ML aspects of curbmap


## Image Pipeline
----
Problem: A user uploads a photo of multiple street signs in one image.
1. Bounding boxes for signs (CNN)
    1. [Single Shot multibox Detectors (SSD)](https://github.com/pierluigiferrari/ssd_keras)
2. Orient/upright/straighten the image in the box
3. Extract the text in the box
4. Determine meaning from the text


## Determine related map information from nearby information
---
Problem: Given a street, can we predict a similar restricted street
1. 
