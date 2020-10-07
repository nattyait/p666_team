from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
        member_card = ''
        level = member.level
        if level == 'Grand Dealer':
            member_card = '/card_templates/grand_dealer.jpg'
        elif level == 'Dealer':
            member_card = '/card_templates/dealer.jpg'
        elif level == 'Super VIP Gold':
            member_card = '/card_templates/sup_VIP_gold.jpg'
        elif level == 'VIP Gold':
            member_card = '/card_templates/VIP_gold.jpg'
        elif level == 'VIP':
            member_card = '/card_templates/VIP.jpg'
        elif level == 'ตัวแทนหลัก':
            member_card = '/card_templates/level2.jpg'
        elif level == 'ตัวแทนย่อย':
            member_card = '/card_templates/level1.jpg'
        elif level == 'Start':
            member_card = '/card_templates/start.jpg'
        return render(
            request,
            self.template,
            {
            'member': member,
            'member_card': member_card,
            }
        )
        
    '''
    Todo if level, choose template, then open image and put on the level template, and render
    '''