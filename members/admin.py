from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    image_display = AdminThumbnail(image_field='image')
    image_display.short_description = 'Image'
    search_fields = ['name', 'member_id', 'nickname', 'parent_member__member_id']
    list_filter = ['level']

    readonly_fields = ['image_display']
    

admin.site.register(Member,MemberAdmin)
