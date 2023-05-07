# Import OS packages
import os
# Import time
from datetime import datetime
# Import streams
from io import BytesIO
# Import computer vision
from PIL import Image
from PIL.ExifTags import TAGS
_TAGS_r = dict(((v, k) for k, v in TAGS.items()))


# def read_img_meta():


#     return x, y, w, h


def get_meta(img_path: str) -> None:
# def get_meta(img_bytes) -> None:
    """
    The functions extracts exif metadata from image
    Arguments
    ---------
    img_path: str
        relative image path
    
    Output
    ------
    long : float
        image center longitude in WGS
    lat : float
        image center lattitude in WGS
    height : float
        height above sea level
    """
    
    # Reading image from string
    img = Image.open(img_path)
    # Get EXIF data 
    exifd = img._getexif()
    # Getting keys of EXIF data
    keys = list(exifd.keys())

    # Remove MakerNote tag because these can be too long
    keys.remove(_TAGS_r["MakerNote"])

    # Get key values from img exif data
    keys = [k for k in keys if k in TAGS]

    # GPS
    gpsinfo = exifd[_TAGS_r["GPSInfo"]]

    # Decimal part of longitude
    decimal_long = (float(gpsinfo[2][1]) * 60 + float(gpsinfo[2][2]))/3600

    # Longitude
    long = float(gpsinfo[2][0]) + decimal_long

    # Decimal part of latitude
    decimal_lat = (float(gpsinfo[4][1]) * 60 + float(gpsinfo[4][2]))/3600

    # Latitude
    lat = float(gpsinfo[4][0]) + decimal_lat

    # Height above sea level
    height = gpsinfo[6]


    return long, lat, height