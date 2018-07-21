# coding:utf-8
import os
import xlrd
from sklearn import linear_model  # 导入线性模型
import numpy as np
import matplotlib.pyplot as plt



def caiPiao(neirong):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获得模块路径
    SHUJU_DIR = os.path.abspath(os.path.join(BASE_DIR, "static/wenDang/x3d.xls"))   #获得文档路径
    bk = xlrd.open_workbook(SHUJU_DIR)  #读取excel表格
    sh = bk.sheet_by_name("3d") # 获得3d那个sheet
    nrows = sh.nrows # 获取行数
    ncols = sh.ncols # 获取列数
    row_list = [] # 准备个列表准备装数据
    for i in range(1, nrows):  #拿出每行数据
        row_data = sh.row_values(i)
        xinShuJu=[]  #准备一个小列表 一会放到大列表里
        k = ""
        for j in row_data[1:]:
            k+=j
        xinShuJu.append(int(k.encode('raw-unicode-escape'))) #转型 拼接 存入
        row_list.append(xinShuJu)
    #然后准备训练数据  X表示前一天 Y表示今天
    X = row_list[0:len(row_list) - 1]
    Y = row_list[1:]
    print(u'全部数据：%s' % row_list)
    print(u'输入数据：%s' % X)
    print(u'结果数据：%s' % Y)
    # =================================================数据获取完===================================================
    # 回归训练
    clf = linear_model.LinearRegression()  # 使用线性回归
    clf.fit(X,Y)
    res = clf.predict(np.array(int(neirong)).reshape(-1, 1))[0]  # 预测结果
    print(u'今天的开奖号是：%s' % res)
    print(u'今天的开奖号取整后是：%s' % round(res, 0))
    jieGuo = round(res, 0)
    # =================================================开奖号码预测完===================================================
    X2 = X  # 以x为基准数  预测所有的y 用于画图
    Y2 = clf.predict(X)  #得到x,y  作为中心线

    # 绘制线性回归图形
    plt.figure()
    plt.title(u'my test')  # 标题
    plt.xlabel(u'历史',fontproperties='SimHei')  # x轴坐标
    plt.ylabel(u'new')  # y轴坐标
    plt.axis([0, 1000, 0, 1000])  # 显示区间
    plt.grid(True)  # 显示网格
    plt.plot(X, Y, 'r.', label="$%s$" % "ycsj")  # 绘制训练数据集散点图  xy红色的点
    plt.plot(X2, Y2, 'g-', label="$%s$" % "jgsj")  # 绘制预测数据集直线  绿色的实线
    plt.legend() #出图
    CAIPIAO_DIR = os.path.abspath(os.path.join(BASE_DIR, "static/img/caiPiao.jpg")) #要存图片
    plt.savefig(CAIPIAO_DIR) #存下图片
    return jieGuo, "/static/img/caiPiao.jpg" # 返回值