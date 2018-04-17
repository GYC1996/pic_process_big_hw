#-*-coding:utf-8-*-
import cv2
import math

def pro(name,pic,w,h):
    Ori_Image = cv2.imread(name)
    noise_Image = cv2.GaussianBlur(Ori_Image, (3, 3), 10, 10)
    #noise_Image = cv2.blur(Resize_Image, (2, 2))
    cv2.imshow("noise", noise_Image)
    Gray_Image = cv2.cvtColor(noise_Image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", Gray_Image)
    canny_Image = cv2.Canny(Gray_Image, 32, 110)
    #ret,canny_Image = cv2.threshold(Gray_Image,200,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("canny", canny_Image)
    dilate_Image = cv2.dilate(canny_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1)))
    cv2.imshow("dilate",dilate_Image)
    erode_Image = cv2.erode(dilate_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1)))
    cv2.imshow("erode", dilate_Image)
    # name="b"+pic+".jpg"
    # cv2.imwrite(name,dilate_Image)
    image, contours, hierarchy = cv2.findContours(dilate_Image, cv2.RETR_TREE, \
                                                  cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        rect = cv2.minAreaRect(contours[i])
        if(rect[1][0]>rect[1][1]):
            maxer=rect[1][0]
            miner=rect[1][1]
        else:
            maxer=rect[1][1]
            miner=rect[1][0]
        if(maxer>=0.18*w and maxer<=0.30*w)and(miner>=0.04*h and miner<=0.08*h)and(((math.fabs(rect[2])>88) and(rect[1][0]<rect[1][1]))or((math.fabs(rect[2])<2)and(rect[1][0]>rect[1][1])) ):
            box=cv2.boxPoints(rect)
            x1=int(box[0][0])
            y1=int(box[0][1])
            x2=int(box[1][0])
            y2=int(box[1][1])
            x3=int(box[2][0])
            y3=int(box[2][1])
            x4=int(box[3][0])
            y4=int(box[3][1])
            cv2.line(Ori_Image, (x1,y1),(x2,y2), (0,0,255), 2)
            cv2.line(Ori_Image, (x2,y2),(x3,y3), (0,0,255), 2)
            cv2.line(Ori_Image, (x3,y3),(x4,y4), (0,0,255), 2)
            cv2.line(Ori_Image, (x4,y4),(x1,y1), (0,0,255), 2)
    name2="2/b"+pic
    name3="2/c"+pic
    name4="2/d"+pic
    print name2
    # cv2.imshow("123",Ori_Image)
    #cv2.waitKey()
    cv2.imwrite(name2,canny_Image)
    cv2.imwrite(name3,Ori_Image)
    cv2.imwrite(name4,dilate_Image)

if __name__=="__main__":

    list=["q (11).jpg","q (10).jpg","q (9).jpg","5.jpg","1.jpg","10.jpg","20.jpg","50.jpg","100.jpg","q.jpg","q (1).jpg",
          "q (2).jpg","q (3).jpg","q (4).jpg","q (5).jpg","q (6).jpg","q (7).jpg",
          "q (8).jpg","q (12).jpg","q (13).jpg"]
    for pic in (list):
        Ori_Image = cv2.imread(pic)
        if(Ori_Image.shape[0]<Ori_Image.shape[1]):
            Resize_Image = cv2.resize(Ori_Image, (640, 512))
        else:
            Resize_Image = cv2.resize(Ori_Image, (512, 640))
        noise_Image = cv2.GaussianBlur(Resize_Image, (5, 5), 0, 0)
        cv2.imshow("noise", noise_Image)
        Gray_Image = cv2.cvtColor(noise_Image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", Gray_Image)
        canny_Image = cv2.Canny(Gray_Image, 10, 140)
        cv2.imshow("canny", canny_Image)
        dilate_Image = cv2.dilate(canny_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40)))
        erode_Image = cv2.erode(dilate_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40)))
        cv2.imshow("erode", erode_Image)
        image, contours, hierarchy = cv2.findContours(erode_Image, cv2.RETR_TREE, \
                                                      cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            rect = cv2.minAreaRect(contours[i])
            if (rect[1][0] > rect[1][1]):
                maxer = rect[1][0]
                miner = rect[1][1]
            else:
                maxer = rect[1][1]
                miner = rect[1][0]
            if miner > 150 and maxer > 300:
                w=maxer
                h=miner
                box = cv2.boxPoints(rect)
                x1 = int(box[0][0])
                y1 = int(box[0][1])
                x2 = int(box[1][0])
                y2 = int(box[1][1])
                x3 = int(box[2][0])
                y3 = int(box[2][1])
                x4 = int(box[3][0])
                y4 = int(box[3][1])
                cv2.line(Resize_Image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.line(Resize_Image, (x2, y2), (x3, y3), (0, 0, 255), 2)
                cv2.line(Resize_Image, (x3, y3), (x4, y4), (0, 0, 255), 2)
                cv2.line(Resize_Image, (x4, y4), (x1, y1), (0, 0, 255), 2)
                if (rect[1][0] >= rect[1][1]):
                    angle = rect[2]  # 负数，顺时针旋转
                else:
                    angle = 90 - math.fabs(rect[2])  # 正数，逆时针旋转
                M = cv2.getRotationMatrix2D((rect[0][0], rect[0][1]), angle, 1)
                Spin_Image = cv2.warpAffine(Resize_Image, M, (int(1.5*Resize_Image.shape[0]),
                                                          int(Resize_Image.shape[1])))
        name="2/a"+pic
        cv2.imwrite(name,Spin_Image)
        pro(name,pic,w,h)