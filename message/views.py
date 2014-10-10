#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from message.models import Messa
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.POST:
        submit = request.POST['msg']
        new_m = Messa(msg = submit)
        new_m.save()

    all_msg = Messa.objects.all()
#    content = "<p>Hi, there"
    content = {}
    content.update(csrf(request))
    content['name'] = request.user.get_username()
    #content['messages'] = ["hi","Great","Ok"]
    content['messages'] =  all_msg
    return render(request,'msg.html',content)

