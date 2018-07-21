# coding:utf-8
import url_controller
import html_downloader
import html_parser
import html_outputer

class Spider_man(object):
    def __init__(self):
        # 给我的spider_main添加初始化属性 注意引文件和起类名
        self.urls=url_controller.UrlControl()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def pa(self,root_url):
        try:
            self.urls.add_new_url(root_url)
            count=1  #定义要爬多少次
            while self.urls.has_new_url():
                new_url=self.urls.get_new_url()
                print "爬取第{0[0]}个url,是{0[1]}".format([count, new_url])
                # 启动下载器 下载页面 传入url
                html_cont = self.downloader.download(new_url)
                # 下载好后 利用解析器 解析这个数据 获取信息和新的url和新的数据
                new_urls, new_data=self.parser.parse(new_url,html_cont)
                # 将新url添加到url的管理器里 这个方法和上面的不一样,是添加多个url
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                # 加个判断 比如爬取20个url 那么就在这加判断
                if count == 3:
                    break
                    # 加完判断后 你会发现 有的部分会爬取错 那么项目会卡住 为了避免 那我们就加入try就可以了
                count += 1
            # 循环结束后 调用output 输出我们的数据  当然写到这 我们记得要把上上面的方法实现
            self.outputer.output_html()
            return 1
        except:
            return 0