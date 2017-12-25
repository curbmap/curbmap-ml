import glob
import csv
from lxml import etree
from os import path

FILES = glob.glob(
    '/home/eli/Documents/Curbmap/datasets/IN/Annotation/n06793231/*')
FILES2 = glob.glob('/home/eli/Documents/Curbmap/datasets/IN/Annotation/n06794110/*')
FILES = FILES + FILES2
CAPTURE = False
IMAGE_NAME = ""
box = [0,0,0,0]
with open('filesize.csv', 'w') as file_size:
    with open('generator.csv', 'w') as generator_file:
        for xmlfilename in FILES:
            with open(xmlfilename) as xml_file:
                parsing = etree.iterparse(xml_file)
                for action, elem in parsing:
                    if elem.tag == "filename":
                        IMAGE_NAME = elem.text
                        if not path.isfile("/home/eli/Documents/Curbmap/datasets/IN/Images/"+IMAGE_NAME+".JPEG"):
                            IMAGE_NAME = ""
                            break
                        file_size.write('/home/eli/Documents/Curbmap/datasets/IN/Images/'+IMAGE_NAME + ".JPEG,")
                    if elem.tag == "width":
                        file_size.write(elem.text + ",")
                    if elem.tag == "height":
                        file_size.write(elem.text + "\n")
                    if CAPTURE:
                        if elem.tag == "xmin":
                        elif elem.tag == "ymin" or elem.tag == "xmax":
                            generator_file.write(elem.text + ",")
                        else:
                            if elem.tag == "ymax":
                                generator_file.write('/home/eli/Documents/Curbmap/datasets/IN/Images/'+IMAGE_NAME + ".JPEG," + elem.text + ",")

                                generator_file.write(elem.text + ",sign\n")
                                CAPTURE = False
                    else:
                        if elem.tag == "xmin":
                            generator_file.write(
                                '/home/eli/Documents/Curbmap/datasets/IN/Images/'+IMAGE_NAME + ".JPEG," + elem.text + ",")
                        elif elem.tag == "ymin" or elem.tag == "xmax":
                            generator_file.write(elem.text + ",")
                        else:
                            if elem.tag == "ymax":
                                generator_file.write(elem.text + ",notsign\n")
                    if elem.tag == "name" and (elem.text == "n06793231" or elem.text == "n06794110"):
                        CAPTURE = True
                    if elem.tag == "annotation":
                        IMAGE_NAME = ""
                    else:
                        pass
