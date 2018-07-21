# coding:utf-8
class UrlCon(object):
    # 1.第一初始化方法 思考 我们要管理新的url,还有爬取过的旧的url
    # 那么就需要2个集合  而有可能发生重复的url所以选择set
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self, new_urls):
        # 4 也是先判断吧 如果为None 或者为空的就不添加了
        if new_urls is None or len(new_urls) == 0:
            return
        # 5.这里就可以批量添加了 其实就调用上面写好的单个添加就行了 我们使用for循环处理
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
       return len(self.new_urls) !=0

    def get_new_url(self):
        # 7.这里要考虑的是从新的里拿出来的同时把他移入到我们的旧urls的集合里
        new_url = self.new_urls.pop()  # 这个方法是从集合里获取一个返回来 并且移除调这个元素
        self.old_urls.add(new_url)  # 这个是把url添加到old里 让他不再爬取
        return new_url  # 将这个url返回就可以
        # 那这个模块就搞定了  下面去写html_downloader吧
