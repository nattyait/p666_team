from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    member_id  = models.CharField(max_length=10)
    area = models.CharField(max_length=200)
    line_id = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)

