import glob
import cv2
from shutil import move

"""
Currently this file takes a photo, reduces its size
then applies Contrast Limited Histogram Equalization
to the intensities in the LAB plane and then reforms
the BGR image.
"""


images = glob.glob("../curbmapbackend-js/processed/*.jpg")
orb = cv2.ORB_create()

for image in images:
    filepath = image.split("/")
    newfilepath = 'postprocessed/' + filepath[-1]
    cv_image = cv2.imread(image)
    print(cv_image.shape)
    if (cv_image.shape[0] < cv_image.shape[1]):
        # Landscape
        ratio = 2600 / cv_image.shape[1]
    else:
        ratio = 2600 / cv_image.shape[0]
    cv_image = cv2.resize(
        cv_image, (int(round(cv_image.shape[1] * ratio)), int(round(cv_image.shape[0] * ratio))), interpolation=cv2.INTER_LANCZOS4)
    lab_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2LAB)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(12, 12))
    lab_planes = cv2.split(lab_image)
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab_image = cv2.merge(lab_planes)
    cv_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)
    cv2.imwrite(newfilepath, cv_image)
