import glob
import cv2
from PIL import Image, ImageFilter
from shutil import move
import openloacationcode

"""
This file checks a file's name with Open Location Code
and EXIF GPS data to confirm it has been taken and uploaded
from the location it was taken
"""

images = glob.glob("../curbmapbackend-js/uploads/*.jpg")
for image in images:
    pil_image = Image.open(image)
    exif = pil_image._getexif()
    if exif is not None and len(exif[34853].keys()) >= 4:
        GPS_T = exif[34853]
        lat = GPS_T[2][0][0] + GPS_T[2][1][0] / 60 + \
            GPS_T[2][2][0] / (60 * 60 * GPS_T[2][2][1])
        if GPS_T[1] != "N":
            lat = -1 * lat
        lng = GPS_T[4][0][0] + GPS_T[4][1][0] / 60 + \
            GPS_T[4][2][0] / (60 * 60 * GPS_T[4][2][1])
        if GPS_T[3] == "W":
            lng = -1 * lng
        new_filename = image.split("/")
        filname_sub = new_filename[-1].split("-")
        OLC = filname_sub[-1].split(".")[0]
        decode = openloacationcode.decode(OLC)
        if decode.latitudeLo - 0.075 < lat < decode.latitudeHi + 0.075 and decode.longitudeLo - 0.075 < lng < decode.longitudeHi + 0.075:
            # HxW pixels
            new_path = "/".join(new_filename[:-2]) + \
                "/processed/" + \
                "-".join(filname_sub[:-1]) + '-' + OLC + '-' + \
                str(exif[40962]) + "x" + str(exif[40963]) + ".jpg"
        else:
            new_path = "/".join(new_filename[:-2]) + \
                "/excluded/" + new_filename[-1]
        move(image, new_path)
