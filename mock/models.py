from django.db import models


class Project(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False, verbose_name='项目名称')
    desc = models.CharField(max_length=100, null=False, verbose_name='项目描述')

    class Meta:

        db_table = 'Project'


class Api(models.Model):

    method = models.CharField(max_length=10, null=False, verbose_name='请求类型')
    name = models.CharField(max_length=50, null=False, verbose_name='接口名称')
    url = models.CharField(max_length=100, null=False, unique=True, verbose_name='请求路由')
    body = models.TextField(verbose_name='请求体')
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING, verbose_name='关联项目')

    class Meta:

        db_table = 'Api'
