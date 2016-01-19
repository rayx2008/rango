#coding:utf-8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from sel.models import Bill
from django.template.context_processors import request
import os,sys
sys.path.insert(0,os.path.abspath(os.curdir))
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response


# Create your views here.

def archive(request):
    posts = Bill.objects.all()
    #t = loader.get_template('arc.html')
    #c = Context('posts',posts)
    #return HttpResponse(t.render(c))
    return render_to_response("arc.html",locals()) 


    