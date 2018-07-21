# coding:utf-8
import os
import xlrd
from sklearn import linear_model  # 导入线性模型
import numpy as np
import matplotlib.pyplot as plt

plt.figure()  #
def test3d(neiRong):
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获得模块路径
    SHUJU_DIR = os.path.abspath(os.path.join(BASE_DIR, "static/wenDang/x3d.xls"))  # 获得文档路径
    bk=xlrd.open_workbook(SHUJU_DIR)
    ndata=bk.sheet_by_name("3d")
    nrows=ndata.nrows
    ncols=ndata.ncols
    li=[]
    for i in range(1,nrows):
        row_data=ndata.row_values(i)
        k=""
        new_data=[]
        for j in row_data[1:]:
            k+=j
        new_data.append(int(k.encode("raw-unicode-escape")))
        li.append(new_data)
    print li

    X=li[0:-1]
    Y=li[1:]
    print X
    print Y
#  =========================================================数据准备完成==============================================
    lr = linear_model.LinearRegression()  # 使用线性回归
    lr.fit(X, Y)
    print np.array(int(neiRong)).reshape(-1, 1)
    print  lr.predict(np.array(int(neiRong)).reshape(-1, 1))
    # print  clf.predict(np.array(int(neiRong)))
    jg=lr.predict(int(neiRong))[0][0]
    result=int(jg)
    print result
#  =========================================================画图==============================================
    X2=X
    Y2=lr.predict(X2)
    # 绘制线性回归图形


    plt.title(u'my test')  # 标题
    plt.xlabel(u'历史', fontproperties='SimHei')  # x轴坐标
    plt.ylabel(u'new')  # y轴坐标
    plt.axis([0, 1000, 0, 1000])  # 显示区间
    plt.grid(True)  # 显示网格
    plt.plot(X, Y, 'r.', label="$%s$" % "ycsj")  # 绘制训练数据集散点图  xy红色的点
    plt.plot(X2, Y2, 'g--', label="$%s$" % "jgsj")  # 绘制预测数据集直线  绿色的实线
    plt.legend()  # 出图
    CAIPIAO_DIR = os.path.abspath(os.path.join(BASE_DIR, "static/img/caiPiao.jpg"))  # 要存图片
    plt.savefig(CAIPIAO_DIR)  # 存下图片

    return result, "/static/img/caiPiao.jpg"  # 返回值

# if __name__=="__main__":
#     test3d("213")