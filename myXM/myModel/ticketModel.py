# coding:utf-8
#安装splinter：
#  pip install splinter
# 2. 第二种使用git：
#  git clone git://github.com/cobrateam/splinter.git
#  cd splinter
#  python setup.py install
# 3. 第三种直接下载zip文件
#  https://pypi.python.org/pypi/splinter/   python官网下载
#  cd splinter
#  python setup.py install
# 使用方法
# http://blog.csdn.net/lanchunhui/article/details/50243669 csdn使用案例
# http://splinter.readthedocs.io/en/latest/drivers/chrome.html#using-chrome-webdriver  英文安装网站
# http://splinter.readthedocs.io/en/0.7.3/#getting-started  英文使用网站
# http://blog.csdn.net/windanchaos/article/details/54898354  csdn有人写的api
# 谷歌驱动下载   http://chromedriver.storage.googleapis.com/index.html
# 谷歌浏览器版本对应 http://blog.csdn.net/huilan_same/article/details/51896672
from splinter.browser import Browser  #引入splinter的borwser对象
from time import sleep  #引入sleep 做休眠用

class Buy_Tickets(object):
    def __init__(self,username, passwd, order, passengers, dtime, starts, ends):
        self.username = username  #用户名
        self.passwd = passwd      #密码
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.xb = xb
        # self.pz = pz
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'  #12306首页
        self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'   #登录成功的地址
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'    #购票的路径
        self.driver_name = 'chrome'
        self.executable_path = 'F:\cro\chromedriver.exe'
    # 登录功能实现
    def login(self):
        self.driver.visit(self.login_url) #访问地址栏
        self.driver.fill('loginUserDTO.user_name', self.username) # 通过name 添加用户名
        # sleep(1)
        self.driver.fill('userDTO.password', self.passwd)       #通过name添加密码
        # sleep(1)
        print('请输入验证码...')
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break  #结束后 才会走下面的代码
    # 买票功能实现
    def start_buy(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        # 窗口大小的操作
        self.driver.driver.set_window_size(1200, 800)
        self.login()
        self.driver.visit(self.ticket_url)  #进入买票的页面
        try:
            print u"购票页面开始..."
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count = 0
            while self.driver.url == self.ticket_url:
                count += 1
                self.driver.find_by_text(u"查询").click()
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                # 这是我找到我要买的那个票的有无 的那个标签的id  然后获取里面的value 二哥要的YW_13000K483303
                # 测试YZ_0h000K705705无的  测试有的YZ_01000K708310
                tarVal = self.driver.find_by_id('YZ_0h000K705705').value
                print tarVal
                if tarVal == u'有':
                    if self.order != 0:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                    else:
                        self.driver.find_by_text(u"预订")[0].click()
                    break
                else:
                    continue
            print u"开始预订..."
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print u'开始选择用户...'
            for user in self.users:
                self.driver.find_by_text(user).click()
            print u"提交订单..."
            sleep(1)
            # #这里是买票种  1 成人  2 儿童 3 学生 4 残疾  参数是name
            self.driver.find_by_xpath('//select[@id="ticketType_1"]/option[@value="1"]')._element.click()
            sleep(1)
            # # 席座  1硬座   3 硬卧   4软卧   9商务座  O是二等座(是o不是0)  M一等座
            self.driver.find_by_xpath('//select[@id="seatType_1"]/option[@value="1"]')._element.click()
            sleep(1)
            # =======================================
            # 提交订单
            print u"提交订单..."
            self.driver.find_by_id('submitOrder_id').click()
            sleep(1.5)
            print u"确认选座..."
            self.driver.find_by_id('qr_submit_id').click()
            return 1
        except Exception as e:
            print e
            return -1