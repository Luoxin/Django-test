# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class user(models.Model):
    id=models.CharField(max_length=100,db_column="user_id",primary_key=True)
    userName=models.CharField(max_length=100,db_column="user_name")
    passWord=models.CharField(max_length=100,db_column="user_pass")
    photo=models.CharField(max_length=100,db_column="user_photo")

class Tea(models.Model):
    id = models.CharField(max_length=100, db_column="id", primary_key=True)
    userName = models.CharField(max_length=100, db_column="name")

