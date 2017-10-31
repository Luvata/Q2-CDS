
from PIL import Image
from glob import glob
import os


def convert_ppm_to_JPG(img_name):
    # anh se co ten img_name.ppm
    im = Image.open(img_name+".ppm")
    im.save(img_name+".jpg")
    os.remove(img_name+".ppm")

# list tat ca cac file co extension la ppm
a = glob("*.ppm")
# lay filename cua cac file do
a = [x.split(".")[0] for x in a]
# Magic
for x in a:
    convert_ppm_to_JPG(x)

