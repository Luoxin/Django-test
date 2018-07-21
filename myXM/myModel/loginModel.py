# coding:utf-8
from myXM import models
import uuid

class loginModel(object):
    def loginOn(self,user,pwd):
        try:
            result=models.user.objects.get(userName=user)
            print result.passWord
            if result.passWord==pwd:
                return 1
            else:
                return 0
        except :
            return -1
    def registerOn(self,user,pwd):
        try:
            models.user.objects.create(id=uuid.uuid4(),userName=user, passWord=pwd)
            return 1
        except :
            return -1
    def validUserName(self,userName):
        result = models.user.objects.filter(userName=userName)
        return  result.__len__()