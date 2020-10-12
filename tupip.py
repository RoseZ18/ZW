import numpy as np
import math
from time import *
from PIL import Image
import cv2
from request import *
from numpy import average, dot, linalg
olderr = np.seterr(all='ignore')
# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):  # 两重循环，生成9张图片基于原图的位置
        for j in range(0, 3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
# 保存
def save_images(st,image_list):
    index = 1
    for image in image_list:
        image.save(st+str(index) + '.jpg')
        index += 1
#找出9张中不是纯白色也不是纯黑色的图
def shang(img):
    k = 0
    res = 0
    tmp = []
    for i in range(256):
        tmp.append(0)
    for i in range(len(img)):
        for j in range(len(img[i])):
            val = img[i][j]
            tmp[val] = float(tmp[val] + 1)
            k =  float(k + 1)
    for i in range(len(tmp)):
            tmp[i] = float(tmp[i] / k)
    for i in range(len(tmp)):
            if(tmp[i] == 0):
                res = res
            else:
                res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
    return res
#根据图像的一部分匹配图
def model_match(search_image, model_image, threshold):
    search_img = cv2.imread(search_image)
    model_img_gray = cv2.imread(model_image, 0)#读取模板图片的灰度图
    search_img_gray = cv2.cvtColor(search_img, cv2.COLOR_BGR2GRAY)#将搜索图片转化为灰度图
    h, w = model_img_gray.shape
    res = cv2.matchTemplate(search_img_gray, model_img_gray, cv2.TM_CCOEFF_NORMED)#采用标准相关匹配 方法度量相似度
    #print(res.shape)
    loc = np.where(res>threshold)#返回每一个维度的坐标值， 比如返回值为[1, 2, 3],[1, 2, 4] 表明（1， 1）（2， 2）（3， 4）这三个坐标点的相似度大于阈值
    #print(loc)
    flag=0
    for pt in zip(*loc):#zip(*loc)反解析为坐标值
        #print(pt)
        flag=1
        #cv2.rectangle(search_img, pt[::-1], (pt[1] + w, pt[0] + h), (7,249,151), 2) #在搜索图片上绘制矩形框
    return flag
# 将图片转化为RGB
def make_regalur_image(img, size=(64, 64)):
    gray_image = img.resize(size).convert('RGB')
    return gray_image
# 计算直方图
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
    return hist
# 计算相似度
def calc_similar(li, ri):
    calc_sim = hist_similar(li.histogram(), ri.histogram())
    return calc_sim
if __name__=="__main__":
    #题目图片
    fh = open("test.jpg", "wb")
    fh.write(image_data)
    fh.close()
    #切割题目图片并保存到文件夹testtu
    begin_time = time()
    st='testtu/'
    x=-1
    file_name='test.jpg'
    image=Image.open(file_name)
    image_list =cut_image(image)
    save_images(st, image_list)
    for i in range(1,10):
        image = cv2.imread('testtu/'+str(i)+'.jpg', 0)
        img = np.array(image)
        res=shang(img)
        if res>0.7:#尽量选择混乱度高的图
            x=i
            break
    print(x)
    #找原图
    model_image ='testtu/' + str(x) + '.jpg'
    y=-1
    for i in range(1,37):
        search_image='yuantuku/' + str(i) + '.jpg'
        threshold = 0.999
        flag=model_match(search_image, model_image, threshold)
        if flag==1:
            y=i
            break
    print(y)
    #切割原图片并保存到文件夹yuantu
    st = 'yuantu/'
    file_name = 'yuantuku/'+str(y)+'.jpg'
    image = Image.open(file_name)
    image_list = cut_image(image)
    save_images(st, image_list)
    #匹配题目图片中切割后的九张图分别在原图中的什么位置
    arr=[]#保存题目分割成的九张图片在原图的位置
    arr1=[]#记录原图的每个部分是否被匹配到即判断哪一张图被扣掉
    for i in range(0,10):
        arr1.append(0)
    for i in range(1,10):
        image1 = Image.open('testtu/'+str(i)+'.jpg')
        flag=0#是否匹配到图（找白色图片）
        for j in range(1,10):
            image2 = Image.open('yuantu/'+str(j)+'.jpg')
            calc_sim = calc_similar(image1, image2)#计算相似度
            if calc_sim==1:
                flag=1
                arr.append(j)
                arr1[j]=1
                break
        if flag==0:
            arr.append(0)
    #判断哪一块图被扣掉
    z=-1
    for i in range(1,10):
        if(arr1[i]==0):
            z=i
            break
    print(arr)
    print(z)
    end_time = time()
    run_time = end_time - begin_time
    #print('该循环程序运行时间：', run_time)  # 该程序的运行时间
