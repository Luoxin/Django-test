# coding:utf-8
import os
class HtmlOutputer(object):
    # 1.我们需要一个列表  用于存放所有收集的数据 用于循环
    # 并且2个方法都用 所以我们写在初始化里
    def __init__(self):
        self.datas = []
    def collect_data(self, new_data):
        # 将数据添加到列表里
        self.datas.append(new_data)

    def output_html(self):
        BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #myFirstDj
        muBiao_DIR = os.path.abspath(os.path.join(BASE_DIR, "templates/paChongResult1.html"))
        gq = open(muBiao_DIR, "w")
        gq.write("<html><head></head><body><table border=1>")
        for data in self.datas:
            print data
            # gq.write("<tr>")
            # gq.write("<td>%s</td>" % data['url'])
            # gq.write("<td>%s</td>" % data['title'].encode('utf-8')) #进行utf8编码
            # gq.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            # gq.write("</tr>")
            gq.write("<tr><td>{0[title]}</td><td>{0[userName]}</td><td>{0[content]}</td></tr>".format(data))
        gq.write("</table></body></html>")
        gq.close()