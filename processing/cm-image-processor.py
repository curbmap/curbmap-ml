import glob
import cv2
from shutil import move

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
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    kp = orb.detect(cv_image, None)
    kp, des = orb.compute(cv_image, kp)
    img2 = cv2.drawKeypoints(cv_image, kp, None, color=(0, 255, 0), flags=0)
    cv2.imwrite(newfilepath, img2)
