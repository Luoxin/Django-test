# coding:utf-8
import url_controller
import html_downloader
import html_parser
import html_outputer


class Spider_men(object):
    def __init__(self):
        self.urls = url_controller.UrlControl()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def pa(self, root_url):
        try :
            self.urls.add_new_url(root_url)
            count = 1
            while self.urls.has_new_url():
                new_url=self.urls.get_new_url()
                print "第{0[0]}次爬取,地址是{0[1]}".format([count,new_url])
                html_content=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_content)
                # print new_urls,new_data
                self.outputer.collect_data(new_data) # 存数据
                self.urls.add_new_urls(new_urls) #存url
                if count==5:
                    break
                count+=1
            self.outputer.output_html()
            return 1
        except:
            return 0