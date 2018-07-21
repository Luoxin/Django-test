# coding:utf-8
import os

class HtmlOutputer(object):
    # 1.我们需要一个列表  用于存放所有收集的数据 用于循环
    # 并且2个方法都用 所以我们写在初始化里
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        # 参数判断
        if new_data is None:
            return
        # 将数据添加到列表里
        self.datas.append(new_data)

    def output_html(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # myFirstDj
        muBiao_DIR = os.path.abspath(os.path.join(BASE_DIR, "templates/paChongResult3.html"))
        gq=open(muBiao_DIR,"w")
        gq.write('''<html><head> <link rel="stylesheet" href="/static/css/bootstrap.min.css"><script src="/static/js/jquery-2.2.4.min .js"></script><script src="/static/js/bootstrap.min.js"></script></head><body><table border=1>''')
        gq.write('''<tr><td>电影名</td><td>评分</td><td>观看连接</td></tr>''')
        for data in self.datas: #这里循环出来的 是每个页面抓取的所有电影的list
            # gq.write("<tr>")
            # gq.write("<td>%s</td>" % data['url'])
            # gq.write("<td>%s</td>" % data['title'].encode('utf-8')) #进行utf8编码
            # gq.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            # gq.write("</tr>")
            for data2 in data: #这里循环出来的是一个页面里面每一个电影
                try:
                    gq.write("<tr><td>{0[movieName]}</td><td>{0[score]}</td><td><a href='{0[boFangDiZhi]}'>观看连接</a></td></tr>".format(data2))
                except:
                    print "%s的错--没有播放地址" % data2["movieName"]
        gq.write('''</table></body><script>$("table").attr("class","table table-responsive table-striped table-hover")</script></html>''')
        gq.close()

