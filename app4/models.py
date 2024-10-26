from django.db import models


class UserBaseInfo(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=20)
    status = models.CharField(verbose_name='状态', max_length=1)
    createdate = models.DateTimeField(
        verbose_name='创建日期', db_column='createDate'
    )

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        managed = False
        verbose_name = '人员基本信息'
        db_table = 'UserBaseInfo4'


class DepartInfo(models.Model):
    id = models.AutoField(verbose_name='部门编号', primary_key=True)
    departname = models.CharField(verbose_name='部门名称', max_length=30)
    createname = models.DateTimeField(
        verbose_name='创建日期', db_column='createDate'
    )


class UserExtraInfo(models.Model):
    id = models.AutoField(verbose_name='拓展编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30)
    truename = models.CharField(verbose_name='真是姓名', max_length=30)
    sex = models.IntegerField(verbose_name='性别')
    salary = models.DecimalField(
        verbose_name='薪水', max_length=8, decimal_places=2
    )
    age = models.IntegerField(verbose_name='年龄')
    department = models.CharField(verbose_name='部门', max_length=20)
    status = models.CharField(verbose_name='状态', max_length=1)
    createdate = models.DateTimeField(
        verbose_name='创建日期', db_column='createDate'
    )
    memo = models.TextField(verbose_name='备注', blank=True, null=True)
    user = models.OneToOneField(UserBaseInfo, on_delete=models.CASCADE)
    depart = models.ForeignKey(
        DepartInfo, default='', on_delete=models.DO_NOTHING
    )


class SkillInfo(models.Model):
    id = models.AutoField(verbose_name='技能编号', primary_key=True)
    skillname = models.CharField(verbose_name='特长', max_length=30)
    createdate = models.DateTimeField(
        verbose_name='创建日期', db_column='createDate'
    )
    user = models.ManyToManyField(UserExtraInfo, db_table='user_skill')
