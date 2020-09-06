# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from nntplib import ArticleInfo
from django.db import models


class PhoneInfo(models.Model):
    #id自动创建
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    sell_time = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating_worthy_num = models.IntegerField()
    rating_unworthy_num = models.IntegerField()
    description = models.CharField(max_length=500)
    log_date = models.DateTimeField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'phone_info'


class CommentsInfo(models.Model):
    #id自动创建
    id = models.CharField(max_length=100, primary_key=True)
    comments_id = models.CharField(max_length=100)
    phone_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=20)
    content = models.CharField(max_length=2000)
    log_date = models.DateTimeField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'comments_info'


class Sentiments(models.Model):
    index = models.IntegerField()
    id = models.CharField(max_length=100, primary_key=True)
    comments_id = models.CharField(max_length=100)
    phone_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=20)
    content = models.CharField(max_length=2000)
    log_date = models.DateTimeField()
    sentiments = models.FloatField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'sentiments'

