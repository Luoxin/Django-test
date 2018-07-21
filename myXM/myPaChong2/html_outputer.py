# coding:utf-8
import os
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, new_data):
        self.datas.append(new_data)

    def output_html(self):
        print self.datas
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # myFirstDj
        muBiao_DIR = os.path.abspath(os.path.join(BASE_DIR, "templates/paChongResult2.html"))
        pc=open(muBiao_DIR,"w")
        pc.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body><table>''')
        for data in self.datas:
            pc.write("<tr><td>{0[title]}</td><td>{0[userName]}</td><td>{0[content]}</td></tr>".format(data))
        pc.write('''</table></body></html>''')
        pc.close()