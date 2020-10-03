from django.db import models
from .overwritestorage import OverwriteStorage
from django.core.exceptions import ValidationError

def content_file_name(instance, filename):
    return '/'.join(['member_images', str(instance.id) + '.jpg'])

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
    member_id  = models.CharField(max_length=10, unique=True)
    area = models.CharField(max_length=200)
    line_id = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.START)
    parent_member = models.ForeignKey("self", on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to = content_file_name, 
        storage=OverwriteStorage(), 
        default = 'member_images/no-img.jpg',
        validators=[validate_image])
    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
            return self.member_id + ": " + self.name