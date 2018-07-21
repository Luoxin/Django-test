# coding:utf-8




#2.定义主类
from myXM.myPaChong3 import html_downloader
from myXM.myPaChong3 import html_outputer
from myXM.myPaChong3 import html_parser
from myXM.myPaChong3 import url_controller

class Spider_main(object):
    #3 编写构造方法
    def __init__(self):
        # 给我的spider_main添加初始化属性 注意引文件和起类名
        self.urls=url_controller.UrlCon()
        self.downloader=html_downloader.Downloader()
        self.parser = html_parser.HtmlParser()  # 这里别引入错了 会有一个django自带的html包
        self.outputer = html_outputer.HtmlOutputer()

    def pa(self, root_url,pingFen):
        try:
            # 给我们的urls定义一个添加新url的方法 传入root_url
            self.urls.add_new_url(root_url)
            count=1
            while self.urls.has_new_url():
                # 如果有,我们获取一个新的url
                new_url = self.urls.get_new_url()
                print "爬取第{0[0]}个url,是{0[1]}".format([count, new_url])
                # 我们启动下载器 下载这个页面 传入新url  这是下载一个的下载器
                html_cont = self.downloader.download(new_url)
                # 下载好后 利用解析器 解析这个数据 获取信息和新的url和新的数据,并且利用评分筛选
                new_urls, new_dataS = self.parser.parse(new_url, html_cont, pingFen)
                # 这里利用我们上面得到的连接 再进入去下载页面 找到播放地址 上面这个地址不是播放地址而是详情页面
                new_dataS_xiangQing = self.downloader.download_S(new_dataS)
                #解析我们的详情页面的代码  返回一个更新后的带有播放地址的列表
                new_dataS_BoFangDiZhi = self.parser.parse_xiangQing(new_dataS_xiangQing)
                # 将新url添加到url的管理器里 这个方法和上面的不一样,是添加多个url
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_dataS_BoFangDiZhi)
                print "==================="
                # 加个判断 比如爬取20个url 那么就在这加判断
                if count == 2:
                    break
                    # 加完判断后 你会发现 有的部分会爬取错 那么项目会卡住 为了避免 那我们就加入try就可以了
                count += 1
            # 循环结束后 调用output 输出我们的数据  当然写到这 我们记得要把上上面的方法实现
            self.outputer.output_html()
            # 然后我们思考 想在控制台看见都爬取了谁 并且是第几个 所以去while外面加个变量 然后让变量加加就ok了
            return 1
        except:
            return 0
# # 1.编写运行程序
# if __name__=="__main__":
#     #设置入口url
#     root_url="https://movie.douban.com/top250"
#     #实例化主类
#     obj_spider=Spider_main()
#     #调用pa方法开启爬虫
#     obj_spider.pa(root_url)