from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'名稱')
