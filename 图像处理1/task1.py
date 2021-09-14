import cv2 as cv
import numpy as np
# grayImg = cv.imread('picture1.png',cv.IMREAD_GRAYSCALE)  # 灰度图展示
# cv.imwrite('mygray.jpg',grayImg)
'''
cv2.resize(src,dsize,fx,fy,interpolation)
参数含义：
src：原图像
dsize：输出图像所需大小
fx：沿水平轴的比例因子
fy：沿垂直轴的比例因子
interpolation：插值方式
'''
if __name__ == "__main__":
    '''
    利用opencv的接口api 直接调用
    '''
    img = cv.imread('picture1.png',cv.IMREAD_UNCHANGED)  # 原图展示
    print('Original Dimensions : ',img.shape)
    # (810, 1080, 4)
    scale_percent = 30
    width = int(img.shape[1]*scale_percent/100)
    height = int(img.shape[0]*scale_percent/100)
    dim = (width,height)
    resized = cv.resize(img,dim,interpolation=cv.INTER_LINEAR)  # INTER_LINEAR 双线性插值
    cv.imshow("Resized image ",resized)  # 显示图片
    # cv.waitKey(0)  # 图片暂停显示 一直不消失
    # cv.destroyAllWindows() # 关闭所有窗口

    fx = 1.5
    fy = 1.5
    resized1 = cv.resize(resized,dsize=None,fx=fx,fy=fy,interpolation=cv.INTER_NEAREST)  # INTER_NEAREST最近邻插值
    resized2 = cv.resize(resized,dsize=None,fx=fx,fy=fy,interpolation=cv.INTER_LINEAR)  #双线性插值

    print(" Resized image ",resized.shape)

    cv.imshow("INTER_NEAREST image ",resized1)
    cv.imshow("INTER_LINEAR image ",resized2)
    cv.waitKey(0)
    cv.destroyAllWindows()


    '''
    自己手动写
    '''