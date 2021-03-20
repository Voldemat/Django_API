from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Create your views here.

from .models import Poll

def polls_list(request):
    max_objects = 20
    polls = Poll.objects.all()[:max_objects]
    data = {"result":list(polls.values("question","created_by__username", "pub_date"))}
    return JsonResponse(data, status = 200)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk = pk)
    data = {
        "results":{
            "question":poll.question,
            "created_by":poll.created_by.username,
            "pub_date":poll.pub_date,
        }
    }
    return JsonResponse(data, status = 200)