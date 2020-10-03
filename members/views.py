from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member

def index(request):
    latest_member_list = Member.objects.order_by('-member_id')
    template = loader.get_template('members/index.html')
    context = {
        'latest_member_list': latest_member_list,
    }
    return HttpResponse(template.render(context, request))

def member(request, member_id):
    member = Member.objects.get(member_id=member_id)
    template = loader.get_template('members/member.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

class IDCardGenerating:
    def generate_idcard(self, member):

        if member.level == 'VIP':
            foreground = Image.open('VIP.jpg')
        else:
            foreground = Image.open('start.jpg')
        background = Image.open(member.image)
