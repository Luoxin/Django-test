# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse   #用于重定向
from django.shortcuts import render
from myXM import models
import uuid
import json
from myModel.loginModel import loginModel
from myModel import ciYunModel
from myModel.ticketModel import Buy_Tickets
from myModel.ticketModel2 import but_ticket_obj
from PIL import Image
from os import path
from myModel import caiPiaoModel
from myModel import caiPiaoModel2
import urllib2
import urllib
from myXM.myPaChong.spider_man import Spider_man
from myPaChong2.spider_men import Spider_men
from myPaChong3.spider_man import Spider_main
# Create your views here.

def index(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"loginPage.html")
def registerPage(request):
    return render(request,"registerPage.html")
def error(request):
    return render(request,"error.html")
def loginOn(request):
   user= request.POST['user']
   pwd= request.POST['pwd']
   lgM=loginModel()
   result=lgM.loginOn(user,pwd)
   if result==1:
       return HttpResponseRedirect("/myXM/mainPage/")
   else:
       return HttpResponseRedirect("/myXM/error/")

def registerOn(request):
   user= request.POST['user']
   pwd= request.POST['pwd']
   lgM=loginModel()
   result=lgM.registerOn(user,pwd)
   if result==1:
       return HttpResponseRedirect("/myXM/")
   else:
       return HttpResponseRedirect("/myXM/error/")

def mainPage(request):
    return render(request,"mainPage.html")

def ciYunPage(request):
    return render(request,"ciYunPage.html")

def validUserName(request):
    userName=request.POST["userName"]
    lgM = loginModel()
    result = lgM.validUserName(userName)
    ress={}
    if result > 0:
        ress['resultCode']=1
        ress['resultMsg']='用户名重复'
    else:
        ress['resultCode'] = 0
        ress['resultMsg'] = '用户名可以使用'
    return HttpResponse(json.dumps(ress))
#json.dumps : dict转成str
#json.loads:str转成dict

def makeCiYun(request):
   wenBen= request.POST['wenBen']
   myTu= request.FILES['tuPian']
   result=ciYunModel.makeIt(myTu,wenBen)
   img = Image.open(myTu)
   savePath = path.join(path.dirname(__file__), "static/img/yuan.jpg")
   img.save(savePath)
   return HttpResponseRedirect("/myXM/ciYunPage")

def buyTicketPage(request):
    return render(request,"ticketPage.html")

def buyTicket(request):
    # 用户名
    username = 'axj5562880'
    # 密码
    password = 'AXJ5562880'
    # 车次选择，0代表所有车次
    order = 0
    # 乘客名，比如passengers = ['安飞', '安飞']
    # 学生票需注明，注明方式为：passengers = ['安飞(学生)', '安飞']
    passengers = ['安飞']
    # 日期，格式为：'2018-01-20'
    dtime = '2018-02-14'
    # 出发地(需填写cookie值)
    # 这2个cookie 可以通过浏览器查看
    starts = '%u54C8%u5C14%u6EE8%2CHBB'  # 哈尔滨
    # 目的地(需填写cookie值)
    ends = '%u9F50%u9F50%u54C8%u5C14%2CQHX'  # 昂昂溪
    # 车次
    bt=Buy_Tickets(username, password, order, passengers, dtime, starts, ends)
    result=bt.start_buy()
    if result==1:
        return HttpResponse('ok了')
    else:
        return HttpResponse('失败了')


def buyTicket2(request):
    # 用户名
    # username = 'abc47213522@126.com'
    username = 'axj5562880'
    # 密码
    # password = 'abc7890076123'
    password = 'AXJ5562880'
    # 车次选择，0代表所有车次
    order = 4  #这是对应那个车有硬座的id  他是第4行的预订
    # 乘客名，比如passengers = ['安飞', '安飞']
    # 学生票需注明，注明方式为：passengers = ['安飞(学生)', '安飞']
    # passengers = ['逄逢']
    passengers = ['安雪军(学生)', '安飞']
    # 日期，格式为：'2018-01-20'
    dtime = '2018-02-14'
    # 出发地(需填写cookie值)
    # 这2个cookie 可以通过浏览器查看
    starts = '%u54C8%u5C14%u6EE8%2CHBB'  # 哈尔滨
    # 目的地(需填写cookie值)
    ends = '%u9F50%u9F50%u54C8%u5C14%2CQHX'  # 齐齐哈尔
    bt=but_ticket_obj(username, password, order, passengers, dtime, starts, ends)
    flag=bt.buy_ticket()
    if flag:
        return HttpResponse("恭喜你抢到了")
    else:
        return HttpResponse("失败了")

def future3dPage(request):
    return render(request,"future3d.html")
def future3d(request):
    neirong = request.POST['neirong']
    jieGuo, luJing = caiPiaoModel.caiPiao(neirong)
    content = {}
    content["jieGuo"] = jieGuo
    content["luJing"] = luJing
    content_json = json.dumps(content)
    return HttpResponse(content_json, content_type="application/json")

def future4dPage(request):
    return render(request,"future4d.html")

def future4d(request):
    neirong = request.POST['neiRong']
    result,luJing=caiPiaoModel2.test3d(neirong)
    content={}
    content["jieGuo"]=result
    content["luJing"]=luJing
    # dumps是将dict转化成str格式，loads是将str转化成dict格式。
    # dump和load也是类似的功能，只是与文件操作结合起来了。
    content_json=json.dumps(content)
    return HttpResponse(content_json, content_type="application/json")




def jiQiRenPage(request):
    return render(request,"jiQiRenPage.html")
def jiQiRenPage2(request):
    return render(request,"jiQiRenPage2.html")

def myJiQiRen(request):
    neirong = request.POST['neirong'].encode("utf-8")
    print neirong
    API_KEY = '853919de78624f8c9ca81843bd74fbb9'
    raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY
    TULINURL = "%s%s" % (raw_TULINURL, urllib2.quote(neirong))
    req=urllib2.Request(url=TULINURL) #准备好一个请求
    result=urllib2.urlopen(req).read() #发送请求,并直接读出结果
    return HttpResponse(result)

def myJiQiRen2(request):
    neirong = request.POST['neirong'].encode("utf-8")
    API_KEY = '853919de78624f8c9ca81843bd74fbb9'
    raw_TULINURL = "http://www.tuling123.com/openapi/api"
    send_content={}
    send_content["key"]=API_KEY
    send_content["info"]=neirong
    send_content["userid"]="1112"
    data = urllib.urlencode(send_content)  # 适用urllib对数据进行格式化编码
    req=urllib2.Request(url=raw_TULINURL,data=data)
    result=urllib2.urlopen(req).read()
    return HttpResponse(result)


# =======================================================爬虫1=========================================
def paChongPage(request):
    return render(request,"paChongPage.html")
def paYiPa(request):
    wangZhi = request.POST['wangZhi']
    obj_spider = Spider_man()
    # # 调用pa方法开启爬虫
    result = obj_spider.pa(wangZhi)
    return HttpResponse(result, content_type="application/text")
def jieGuoPage(request):
    return render(request,"paChongResult1.html")
# =======================================================爬虫2=========================================
def paYiPa2(request):
    wangZhi = request.POST['wangZhi']
    obj_spider=Spider_men()
    result=obj_spider.pa(wangZhi)
    return HttpResponse(result, content_type="application/text")
def jieGuoPage2(request):
    return render(request,"paChongResult2.html")
# =======================================================爬虫3=========================================
def paYiPa3(request):
    wangZhi = request.POST['wangZhi']
    pingFen = request.POST['pingFen']
    obj_spider=Spider_main()
    result=obj_spider.pa(wangZhi,pingFen)
    return HttpResponse(result, content_type="application/text")
def jieGuoPage3(request):
    return render(request,"paChongResult3.html")