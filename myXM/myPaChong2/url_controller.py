# coding:utf-8
class UrlControl(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def add_new_url(self, root_url):
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def has_new_url(self):
        return self.new_urls.__len__()>0

    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, new_urls):
        for url in new_urls:
            self.add_new_url(url)