from PIL import Image,ImageChops
import requests
from io import BytesIO
import sys
import time
from multiprocessing import Pool
import os
import warnings
warnings.filterwarnings('ignore')

import flickr_api
flickr_api.set_keys(api_key = 'a2379ef967ec31bd8deb6c906214b3c2', api_secret = '3656592701e2c5c2')

def is_greyscale(im):
    """
    Check if image is monochrome (1 channel or 3 identical channels)
    """
    if im.mode not in ("L", "RGB"):
        raise ValueError("Unsuported image mode")

    if im.mode == "RGB":
        rgb = im.split()
        if ImageChops.difference(rgb[0],rgb[1]).getextrema()[1]<50: 
            return True
        if ImageChops.difference(rgb[1],rgb[2]).getextrema()[1]<50: 
            return True
        if ImageChops.difference(rgb[0],rgb[2]).getextrema()[1]<50: 
            return True
    else:
        return True
    return False

def download_u(url):
    try:
        response = requests.get(url, stream=True, verify=False)
        img = Image.open(BytesIO(response.content))
        if is_greyscale(img):
            img.save("grayscale/"+os.path.basename(url).split('.')[0]+".jpg")
        else:
            img.save("color/"+os.path.basename(url).split('.')[0]+".jpg")
    except:
        pass

for k in range(21,31):
    photos = flickr_api.method_call.call_api(method="flickr.groups.pools.getPhotos", group_id="70823775@N00", per_page="500", 
                                             page=str(k), extras="url_l,date_taken")["photos"]["photo"]
    urls = []
    for photo in photos:
        if "url_l" in photo and "datetaken" in photo and photo["datetaken"] > '2010':
            urls.append(photo["url_l"])
    
    with Pool(5) as p:
        p.map(download_u, urls)