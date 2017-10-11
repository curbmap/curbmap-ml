# curbmap-ml
ML aspects of curbmap


Pipeline
----
1. Bounding boxes for signs (CNN)
    1. [Single Shot multibox Detectors (SSD)](https://github.com/pierluigiferrari/ssd_keras)
2. Orient/upright/straighten the image in the box
3. Extract the text in the box
4. Determine meaning from the text
