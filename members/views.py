from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

def index(request):
    latest_member_list = Member.objects.order_by('-member_id')
    output = ', '.join([q.name for q in latest_member_list])
    return HttpResponse(output)

def member(request, member_id):
    member = Member.objects.get(member_id=member_id)
    return HttpResponse("You're looking at member %s." % member.name)
