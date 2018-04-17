#-*-coding:utf-8-*-
import cv2
def pro(pic,w,h):
    Ori_Image = cv2.imread(pic)
    Resize_Image = cv2.resize(Ori_Image, (640, 512))
    noise_Image = cv2.GaussianBlur(Resize_Image, (3, 3), 10, 10)
    #noise_Image = cv2.blur(Resize_Image, (2, 2))
    cv2.imshow("noise", noise_Image)
    Gray_Image = cv2.cvtColor(noise_Image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", Gray_Image)
    canny_Image = cv2.Canny(Gray_Image, 30, 110)
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
        if(maxer>=0.16*w and maxer<=0.25*w)and(miner>=0.04*h and miner<=0.075*h):
            box=cv2.boxPoints(rect)
            x1=int(box[0][0])
            y1=int(box[0][1])
            x2=int(box[1][0])
            y2=int(box[1][1])
            x3=int(box[2][0])
            y3=int(box[2][1])
            x4=int(box[3][0])
            y4=int(box[3][1])
            cv2.line(Resize_Image, (x1,y1),(x2,y2), (0,0,255), 2)
            cv2.line(Resize_Image, (x2,y2),(x3,y3), (0,0,255), 2)
            cv2.line(Resize_Image, (x3,y3),(x4,y4), (0,0,255), 2)
            cv2.line(Resize_Image, (x4,y4),(x1,y1), (0,0,255), 2)
    name="b"+pic+".jpg"
    cv2.imwrite(name,Resize_Image)

#for i in range (len(contours)):
if __name__=="__main__":

    list=["1.jpg","5.jpg","10.jpg","20.jpg","50.jpg","100.jpg","q.jpg","q (1).jpg",
          "q (2).jpg","q (3).jpg","q (4).jpg","q (5).jpg","q (6).jpg","q (7).jpg",
          "q (8).jpg","q (9).jpg","q (10).jpg","q (11).jpg","q (12).jpg","q (13).jpg"]
    for pic in (list):
        Ori_Image = cv2.imread(pic)
        Resize_Image = cv2.resize(Ori_Image, (640, 512))
        noise_Image = cv2.GaussianBlur(Resize_Image, (5, 5), 0, 0)
        cv2.imshow("noise", noise_Image)
        Gray_Image = cv2.cvtColor(noise_Image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", Gray_Image)
        canny_Image = cv2.Canny(Gray_Image, 10, 140)
        cv2.imshow("canny", canny_Image)
        dilate_Image = cv2.dilate(canny_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (60, 60)))
        erode_Image = cv2.erode(dilate_Image, cv2.getStructuringElement(cv2.MORPH_RECT, (60, 60)))
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
        pro(pic,w,h)
    #cv2.waitKey()
