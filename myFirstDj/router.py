# coding:utf-8
from django.shortcuts import HttpResponse,redirect

def DynamicRouter(request,**kwargs):
    app = kwargs.get('app', None)   #接收app
    function=kwargs.get('function',None) #接收function
    print(app,function)
    try:
        appObj = __import__("%s" % app)  # 引入对应的app
        viewObj = getattr(appObj, "views")  # 引入对应app的视图层
        funObj = getattr(viewObj, function)  # 引入对应视图层文件的方法
        result = funObj(request)  # 调用对应的方法
        print ("找到对应方法,目前操作成功")
    except (ImportError,AttributeError),e:
        # 导入失败时，自定义404错误
        print ("导入模块错误")
        return HttpResponse('404 页面不知到飞哪去了')
    except Exception,e:
        print ("出现异常,操作失败")
        return redirect('/myDj/error/')
    return result