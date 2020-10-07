from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PIL import Image, ImageDraw, ImageFont

from .models import Member

from django.views.generic import TemplateView

class MemberListView(TemplateView):
    template = "index.html"

    def get(self, request):
        latest_member_list = Member.objects.order_by('-member_id')
        return render(
            request,
            self.template,
            {
                'latest_member_list': latest_member_list,
            }
        )

class MemberView(TemplateView):
    template = "member.html"

    def get(self, request, *args, **kwargs):
        member_id = self.kwargs['member_id']
        member = Member.objects.get(member_id=member_id)
        member_card = self.generate_member_card(member)
        member_card.show()
        #response = HttpResponse(member_card, content_type="image/png")
        #member_card.save(response, "PNG")
        #return response
        return render(
            request,
            self.template,
            {
            'member': member,
            'member_card': member_card,
            }
        )
        
    def get_card_template(self, member):
        member_card = ''
        level = member.level
        member_card, x, y = self.profile_image_position(level)
        return member_card, x, y

    def generate_member_card(self, member):
        member_card_template, x, y = self.get_card_template(member)
        member_card_background = Image.open(member_card_template)
        member_profile_image = Image.open(member.image)
        width, height = member_profile_image.size
        basewidth = 370
        wpercent = (basewidth / float(member_profile_image.size[0]))
        hsize = int((float(member_profile_image.size[1]) * float(wpercent)))
        member_profile_image = member_profile_image.resize((basewidth, hsize), Image.ANTIALIAS)

        member_profile_image.info["dpi"] = (72, 72)
    
        #crop (left, top, right, bottom)
        member_profile_image = member_profile_image.crop((0,0,370,500))
        member_card_background.paste(member_profile_image, (x, y))

        return member_card_background
    
    def profile_image_position(self, level):
        if level == 'Grand Dealer':
            member_card = 'card_templates/grand_dealer.jpg'
            x = 72
            y = 342
        elif level == 'Dealer':
            member_card = 'card_templates/dealer.jpg'
            x = 60
            y = 342
        elif level == 'Super VIP Gold':
            member_card = 'card_templates/sup_VIP_gold.jpg'
            x = 80
            y = 342
        elif level == 'VIP Gold':
            member_card = 'card_templates/VIP_gold.jpg'
            x = 77
            y = 342
        elif level == 'VIP':
            member_card = 'card_templates/VIP.jpg'
            x = 83
            y = 342
        elif level == 'ตัวแทนหลัก':
            member_card = 'card_templates/level2.jpg'
            x = 53
            y = 342
        elif level == 'ตัวแทนย่อย':
            x = 71
            y = 342
            member_card = 'card_templates/level1.jpg'
        elif level == 'Start':
            member_card = 'card_templates/start.jpg'
            x = 60
            y = 342
        return member_card, x, y