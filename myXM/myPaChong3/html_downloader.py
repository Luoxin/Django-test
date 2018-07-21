# coding:utf-8
import urllib2


class Downloader(object):


    def download(self, new_url):
        # 先进行判断吧 万一url是none呢
        if new_url is None:
            return None  # 返回个None 表示什么都没有下载下来
        # 下面是模拟我们的相应头 其实如果一些简单的网站是可以直接通过我们
        # 的 urllib2直接打开的 但糗事百科这个必须模拟浏览器了
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        headers = {'User-Agent': user_agent}
        req_timeout = 5
        # 将写好的头信息 传入我们的request里
        try:  #这里是因为我爬到的路径有的却点不开了 所以我加上try 保证可以跳过
            request = urllib2.Request(new_url, headers=headers)
            response = urllib2.urlopen(request,None,req_timeout)  # 这里会有一个返回值 是我们的响应
            # 我们判断如果不是200就返回None 否则就如数据就行了
            if response.getcode() != 200:
                return None
        except:
            return None
        # 从响应中读取页面数据
        else:
            return response.read()
        # 这里下载就完成了 那么该解析了 所以去写html的parser吧

    def download_S(self, new_dataS):
        #还是验证一下
        print "进到二次循环了"
        if len(new_dataS) ==0:
            return
        for new_data in new_dataS:  #循环
            xiangQing_url=new_data["xiangQing_href"] #拿出刚才存的
            print xiangQing_url
            xingQing_cont=self.download(xiangQing_url)   #调用本类的下载方法
            new_data["yuanMa"]=xingQing_cont #将内容存入字典里
        return new_dataS  #返回这个字典