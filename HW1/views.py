from django.shortcuts import render
import random
from django.core.paginator import Paginator
from .models import *

name = "Tyler"
src = ["../static/HW1/img/Tyler.jpg"]
src = "none"
taglist = ["tag1", "tag2", "tagtag3",
               "tag4", "tagtagtag5", "tag6",
               "tagtag7", "tag8", "tag9"]
members = ["member1", "member2", "member3",
               "member4", "member5", "member6",
               "member7", "member8", "member9", "member10"]
likenum = 67
dislikenum = 56

class question:
    id = 0
    question_name = "How to get out of here?"
    question_description = "I do really wonder how can I get OUT of here"
    answers_count = 7
    src = "../static/HW1/img/Tyler.jpg"
    taglist = ["tag1", "tag2", "tagtag3",
               "tag4", "tagtagtag5", "tag6",
               "tagtag7", "tag8", "tag9"]

class comment:
    id = 0
    likenum = 7
    dislikenum = 5
    src = "../static/HW1/img/Tyler.jpg"
    question_description = "Dear friend, you can simply use the frontdoor next to you"
    isuseful = False

def getdata():
    data = []
    for i in range(50):
        item = question()
        item.id = i + 1
        item.taglist = item.taglist[random.randint(0,3) : random.randint(3,9)]
        item.likenum = random.randint(1, 200)
        item.dislikenum = random.randint(1, 100)
        data.append(item)
    return data

def getcomments():
    data = []
    for i in range(50):
        item = comment()
        item.id = i + 1
        item.likenum = random.randint(1, 200)
        item.dislikenum = random.randint(1, 100)
        if i % 4 == 0:
            item.isuseful = True
        data.append(item)
    return data
def ConstructIndex(request):

    questionlist = getdata()

    paginator = Paginator(questionlist, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "HW1/index.html", {'name' : name,
                                              'link' : src,
                                              'taglist': taglist,
                                              'page_obj': page_obj,
                                              'members': members,
                                              'questionlist' : page_obj.object_list})

def questionById(request, question_id):
    questionlist = getdata()
    commentlist = getcomments()

    paginator = Paginator(commentlist, 20)

    print('\n\n\n\n')
    print(Question.objects.questionById())
    print('\n\n\n\n')

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "HW1/question.html",
                  {'name' : name,
                   'link' : src,
                   'taglist' : taglist,
                   'page_obj' : page_obj,
                   'members' : members,
                   'mainquestion' : questionlist[0],
                   'commentlist' : page_obj.object_list})

def AddQuestion(request):
    questionlist = getdata()

    return render(request, "HW1/Addquestion.html", {'name' : name,
                                              'link' : src, 'taglist': taglist,
                                              'members': members,
                                              })

def ConstructRegistration(request):
    questionlist = getdata()

    return render(request, "HW1/registration.html", {'name' : name,
                                              'link' : src, 'taglist': taglist,
                                              'members': members,
                                              })

def ConstructLogin(request):
    questionlist = getdata()

    return render(request, "HW1/login.html", {'name' : name,
                                              'link' : src,
                                              'taglist': taglist,
                                              'members': members,
                                              })

def questionByTag(request, tag):

    questionlist = getdata()

    paginator = Paginator(questionlist, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print('\n\n\n\n')
    # print(tag)
    # print('\n\n\n\n')

    return render(request, "HW1/questionByTag.html", {'name': name,
                                              'link': src, 'taglist': taglist,
                                              'page_obj': page_obj,
                                              'members': members,
                                              'tag' : tag,
                                              'questionlist': list(filter(lambda x: tag in x.taglist, page_obj.object_list))})


def fun2(request):
    return render(request, 'HW1/base.html')