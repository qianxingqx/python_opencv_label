# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:25:59 2021
Discription: 读取 csv 格式的标签信息，并绘制矩形框显示
"""
import cv2
import numpy as np

def cv_rect(data_r, i_xmin, i_xmax, i_ymin, i_ymax):
    """ 根据标签绘制矩形框
    Args:
        data_r: 
        others: 起点终点坐标，必须为整型
    Returns:
        data_rect：绘制矩形框后数据，矩形框位置的数据值为 0
    """
    gx_start, gx_end = i_xmin, i_xmax
    gy_start, gy_end = i_ymin, i_ymax
    data_rect = data_r.copy()
    cv2.rectangle(data_rect, (gx_start, gy_start), (gx_end, gy_end), (0,0,255), 2)
    return data_rect

def main():
    index = 0
    src = cv2.imread("./" + str(index) + ".jpeg")
    src_rect = src.copy()
    label_list = np.loadtxt("./" + str(index) + ".csv", delimiter=",", dtype='int')
    for label in label_list:
        i_xmin, i_ymin, i_xmax, i_ymax = label[0], label[1], label[2], label[3]
        src_rect = cv_rect(src_rect, i_xmin, i_xmax, i_ymin, i_ymax)
    cv2.namedWindow('img', 0)
    cv2.imshow('img', src_rect)

if __name__ == '__main__':
    main()