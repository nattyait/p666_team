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
        print(member_id)
        member = Member.objects.get(member_id=member_id)
        return render(
            request,
            self.template,
            {
            'member': member,
            'member_card': '/card_templates/dealer.jpg',
            }
        )