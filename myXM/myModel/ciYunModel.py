# coding:utf-8
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud,ImageColorGenerator
from os import path
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def makeIt(image,wenBen):
    tags = jieba.analyse.textrank(wenBen, topK=1000, withWeight=True)  # 虽然算法不同但基本内容相似
    keywords={}
    for i in tags:
        keywords[i[0]]=i[1]
    myImg=Image.open(image)
    graph=np.array(myImg)
    print 111111
    BasePath=os.path.dirname(os.path.dirname(__file__))
    fontPath=os.path.abspath(BasePath+"/static/fonts/simhei.ttf")
    print 22222222222
    wc =WordCloud(font_path=fontPath,background_color='white',max_words=1000,mask=graph)
    print 3333333333333
    wc.generate_from_frequencies(keywords)  # 传入词频
    print 4444444
    image_color = ImageColorGenerator(graph) #从背景图片生成颜色值
    print 5555555
    wc.recolor(color_func=image_color)  # 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
    print 6666666666
    wc.to_file(path.join(BasePath, "static/img/gq.jpg"))  # 将图片存起来
    return 1