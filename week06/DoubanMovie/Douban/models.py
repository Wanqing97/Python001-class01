# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MovieInfo(models.Model):
    #id自动创建
    n_star = models.IntegerField()
    comment = models.CharField(max_length=500)

    # 元数据，不属于任何一个字段的数据
    # class Meta:
    #     managed = False
    #     db_table = 'movie_info'

