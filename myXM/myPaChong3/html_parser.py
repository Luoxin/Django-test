# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()  # 定义集合 用于存新urls的 <a href="?start=25&amp;filter=">2</a>
        links = soup.find_all("a", href=re.compile(r"\?start=\d+&amp;filter="))
        for link in links:
            new_url = link['href']  # 取出这些符合正则的连接
            new_full_url = urlparse.urljoin(page_url, new_url)  # 拼接
            new_urls.add(new_full_url)  # 将新的url存入 set集合new_urls
        return new_urls

    def _get_new_data(self, soup, pingFen):
        # 定义一个列表
        res_dataS = []
        movie_nodeS= soup.find_all("div", class_="item") #找到所有的item节点
        # 将数据存入字典
        for movie_node in movie_nodeS: #遍历每一个节点
            movie_body_node=movie_node.find("div",class_="bd") #拿到每一个body节点
            movie_pingFen=movie_body_node.find("span",class_="rating_num").get_text() #获得评分
            if movie_pingFen >= pingFen:  #判断如果评分大于我想要的 就继续抓
                res_data = {}       #声明一个字典 存抓的值
                res_data["score"]=movie_pingFen # 将评分存进字典里
                movie_head_node=movie_node.find("div",class_="hd") #抓电影节点的head节点
                movie_title_nodeS=movie_head_node.find_all("span") #抓head节点上所有的span
                # 取第一个span里面的内容并写入编码级  然后将名称存入字典
                res_data["movieName"] = movie_title_nodeS[0].get_text().encode("utf-8")
                movie_href_node=movie_head_node.find("a")#找到 电影头里面的a标签
                res_data["xiangQing_href"]=movie_href_node["href"]#获得a标签上的连接并存入字典里
            res_dataS.append(res_data) #在for循环里把抓的内容存入列表里
        return res_dataS

    def parse(self, new_url, html_cont,pingFen):
        # 老道理 先进行参数判断
        if new_url is None or html_cont is None:
            return
        #利用beautifulSoup 安装指令pip install beautifulsoup4
        #这个库是解析我们html页面的 帮助我们利用属性抓取标签的 利用它的解析器是html.parser的  方法是utf8
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        # 第一个是 给每一个页面的路径找到所有的路径可以点进下一页的路径 返回一个集合
        new_urls = self._get_new_urls(new_url, soup)

        # 第二个是 抓取页面上的信息 电影名  评分 和连接
        new_data = self._get_new_data(soup,pingFen)
        # 履行方法 返回新url和新数据 那么我们去写这2个本地方法吧  先生成 并且把这个2个方法放上面吧
        return new_urls, new_data

    def parse_xiangQing(self, new_dataS_xiangQing):
        if len(new_dataS_xiangQing) == 0:
            return
        for new_data_xiangQing in new_dataS_xiangQing:
            try:
                soup = BeautifulSoup(new_data_xiangQing["yuanMa"], "html.parser", from_encoding="utf-8")
                movie_href_nodeS=soup.find("ul",class_="bs").find_all("a",class_="playBtn")
                if len(movie_href_nodeS)!=0:
                    new_data_xiangQing["boFangDiZhi"]=movie_href_nodeS[0]["href"]
                else:
                    new_data_xiangQing["boFangDiZhi"]="未找到播放地址"
            except:
                print "%s在解析时反生错误" % new_data_xiangQing["movieName"]
        return new_dataS_xiangQing