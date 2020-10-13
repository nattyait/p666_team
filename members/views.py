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

    def get(self, request, *args, **kwargs):
        member_id = self.kwargs['member_id']
        member = Member.objects.get(member_id=member_id)
        member_card = self.generate_member_card(member)

        response = HttpResponse(content_type="image/png")
        member_card.save(response, "PNG")
        return response
        

    def generate_member_card(self, member):
        member_card = ''
        level = member.level
        member_card_template, x, y = self.get_profile_image_and_position(level)
        
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

        name, member_id, area, line_id, facebook, tel, x, y = self.get_text_and_position(member)
        # Name
        draw = ImageDraw.Draw(member_card_background)
        red = (139, 99, 40)
        #black = (0, 0, 0)
        text_pos = (x, y)
        text = name
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 40)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # member_id
        draw = ImageDraw.Draw(member_card_background)
        red = (139, 99, 40)
        #black = (0, 0, 0)
        y = y + 86
        text_pos = (x, y)
        text = member_id
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 40)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # area
        draw = ImageDraw.Draw(member_card_background)
        ed = (139, 99, 40)
        #black = (0, 0, 0)
        y = y + 86
        text_pos = (x, y)
        text = area
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 42)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # line_id
        draw = ImageDraw.Draw(member_card_background)
        ed = (139, 99, 40)
        #black = (0, 0, 0)
        y = y + 85
        text_pos = (x, y)
        text = line_id
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 42)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

         # facebook
        draw = ImageDraw.Draw(member_card_background)
        ed = (139, 99, 40)
        #black = (0, 0, 0)
        y = y + 85
        text_pos = (x + 120, y)
        text = facebook
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 35)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

         # tel
        draw = ImageDraw.Draw(member_card_background)
        ed = (139, 99, 40)
        #black = (0, 0, 0)
        y = y + 85
        text_pos = (x + 80, y)
        text = tel
        font = ImageFont.truetype('ThaiSansNeue-Bold.ttf', 42)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        return member_card_background
    
    def get_profile_image_and_position(self, level):
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

    def get_text_and_position(self, member):
        level = member.level
        name = member.name
        member_id = member.member_id
        if level == "Grand Dealer" or level == "Coach":
            member_id = 'P666'
        area = member.area
        line_id = member.line_id
        facebook = member.facebook
        tel = member.tel
        if level == 'Grand Dealer':
            x = 620
            y = 350
        elif level == 'Dealer':
            x = 620
            y = 350
        elif level == 'Super VIP Gold':
            x = 620
            y = 350
        elif level == 'VIP Gold':
            x = 620
            y = 350
        elif level == 'VIP':
            x = 620
            y = 350
        elif level == 'ตัวแทนหลัก':
            x = 620
            y = 350
        elif level == 'ตัวแทนย่อย':
            x = 620
            y = 350
        elif level == 'Start':
            x = 620
            y = 350
        return name, member_id, area, line_id, facebook, tel, x, y

class TeamView(TemplateView):
    template = "team.html"

    def get(self, request, *args, **kwargs):
        member_id = self.kwargs['member_id']
        parent_member = Member.objects.get(member_id=member_id)
        member_list = Member.objects.filter(parent_member__member_id=member_id)
        member_count = Member.objects.filter(parent_member__member_id=member_id).count()
        return render(
            request,
            self.template,
            {
                'parent_member': parent_member,
                'member_list': member_list,
                'member_count': member_count,
            }
        )