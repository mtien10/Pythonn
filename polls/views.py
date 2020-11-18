from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Question
def index(resquet):
    myname = "Jersey"
    ny     = ["NY", "New Jersey" , "Đào", "Hảo"]
    a      = {"name" : myname, "nyc" : ny}
    return render(resquet,"polls/index.html",a)
def viewlist(resquet):
    list_question = Question.objects.all()
    context = {"dsquest":list_question}
    return render(resquet, "polls/question_list.html", context)
def detailView(resquet , question_id):
    q = Question.objects.get(pk=question_id)
    return render(resquet,"polls/detail_question.html",{"qs":q})
def vote(resquet,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = resquet.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Erorr no have choice")
    c.votes = c.votes + 1
    c.save()
    return render(resquet, "polls/result.html", {"q":q})



# Create your views here.
