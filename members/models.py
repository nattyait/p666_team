from django.db import models
from .overwritestorage import OverwriteStorage
from django.core.exceptions import ValidationError

def content_file_name(instance, filename):
    return '/'.join(['member_images', str(instance.member_id) + '.jpg'])

class Member(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.5
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    class Level(models.TextChoices):
        COACH = "Coach"
        GRAND_DEALER = "Grand Dealer"
        DEALER = "Dealer"
        SUP_VIP = "Super VIP Gold"
        VIP_GOLD = "VIP Gold"
        VIP = "VIP"
        LEVEL2 = "ตัวแทนหลัก"
        LEVEL1 = "ตัวแทนย่อย"
        START = "Start"
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True)
    member_id  = models.CharField(max_length=10, unique=True)
    area = models.CharField(max_length=200)
    line_id = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.START)
    parent_member = models.ForeignKey("self", on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to = content_file_name, 
        default = 'member_images/no-img.jpg',
        validators=[validate_image])

    def __str__(self):
            return self.member_id + ": " + self.nickname + " - " + self.name + " -> " + self.level + " ทีม" + self.parent_member.nickname

class Order(models.Model):
    order_date = models.DateField()
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.order_date) + ": " + self.member.nickname + " - " + self.member.name + " -> " + self.product.name + " = " + str(self.amount)