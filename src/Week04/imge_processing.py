import cv2
import numpy as num
from typing import Dict

def imgprocess(cnt:int,height:int,width:int) -> str:
    x={} ; y={}
    x,y=get_target_points(img=binary,height=height,width=width)
    return dir

def get_target_points(img:num.ndarray,height:int,width:int) -> dict[str,int]:
    coordinates_x={}
    coordinates_y={}
    temp=num.where(binary==255)
    coordinates_x["top"]=temp[1][0]
    coordinates_y["top"]=temp[0][0]
    binary=cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp=num.where(binary==255)
    coordinates_x["left"]=temp[0][0]
    coordinates_y["left"]=abs(height-temp[1][0])
    binary=cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)
    binary=cv2.rotate(binary,cv2.ROTATE_90_CLOCKWISE)

    temp=num.where(binary==255)
    coordinates_x["right"]=abs(width-temp[0][0])
    coordinates_y["right"]=temp[1][0]
    return coordinates_x
    

