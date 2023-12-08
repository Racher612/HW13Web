from datetime import date

from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import random
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from .forms import *
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

def ExternalData(request):
    taglist = Tag.objects.hottestTags()
    members = ["member1", "member2", "member3",
               "member4", "member5", "member6",
               "member7", "member8", "member9", "member10"]

    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.filter(user = request.user)[0]
            name = request.user.username
            src = profile.avatar
        except:
            name = "unregistered"
            src = "none"
    else:
        name = "unregistered"
        src = "none"
    return {'name' : name,
            'link' : src,
            'taglist' : taglist,
            'members' : members,}

def paginator(request, structure):
    paginator = Paginator(structure, 20)

    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1

    page_obj = paginator.get_page(pagenum)
    pages = paginator.page_range
    length = len(pages)

    symbols = ["1", "<", pagenum, ">", str(length)]
    requiredpages = list(map(str, [pages[0], max(int(pagenum) - 1, 1),
                                   int(pagenum), min(int(pagenum) + 1, length), length]))


    return {"page_obj" : page_obj,
            "pages" : [{"sym" : symbols[i], "val" : requiredpages[i]} for i in range(5)]}

def PRODquestionById(request, question_id):
    mainquestion = Question.objects.questionById(question_id)[0]
    commentlist = Comment.objects.commentbyquestion(mainquestion)

    page_obj = paginator(request, commentlist)

    return render(request, "HW1/question.html", ExternalData(request) | {'pages': page_obj["pages"],
                                                                  'mainquestion': mainquestion,
                                                                  'commentlist': page_obj["page_obj"],
                                                             })

def PRODquestions(request):
    questionlist = Question.objects.all()

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/index.html", ExternalData(request) |
                  {"questionlist" : page_obj["page_obj"],
                  "pages" : page_obj["pages"]})

def PRODaddquestion(request):

    # if request.method == "POST":
    #     tags = Tag.objects.tagbyname(request.POST.get("tags"))
    try:
        print(request.POST)
    except:
        pass
    # tags = [request.POST.get(f"tag${i + 1}") for i in range(7)]
    # for i in range(7):
    #     if Tag.objects.tagbyname(tags[i]) == '\n\n\n\n':
    #         Tag.objects.create()


    # question = Question(question_name = request.POST.get("title"),
    #                     question_description = request.POST.get("text"),
    #                     taglist = tags,
    #                     likenum = 0,
    #                     dislikenum = 0,
    #                     date = date.today())

    return render(request, "HW1/Addquestion.html",
                  ExternalData(request) | {"alltagslist" : list(map(lambda x: x.tag, Tag.objects.all()))})

def PRODconstructregistration(request):
    if request.method == "POST":
        user = User(username=request.POST.get("username"),
                    email=request.POST.get("Email"),
                    password=make_password(request.POST.get("password")))
        User.objects.bulk_create([user])
        if request.FILES:
            file = request.FILES[list(request.FILES.keys())[0]]
            file_name = default_storage.save(file.name, file)

            profile = Profile(user = user,
                              avatar = "uploads/" + file.name)

            Profile.objects.bulk_create([profile])
        else:
            profile = Profile(user = user)
            Profile.objects.bulk_create([profile])

        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        login(request, user)
        return redirect(reverse('startpage'))

    return render(request, "HW1/registration.html",
                  ExternalData(request) | {"form" : UploadFileForm})

def PRODconstructlogin(request):
    return render(request, "HW1/login.html", ExternalData(request))

def PRODquestionByTag(request, tag):
    tagname = Tag.objects.tagbyname(tag)
    questionlist = Question.objects.questionByTag(tagname)

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/questionByTag.html", ExternalData(request) |
                  {"questionlist" : page_obj["page_obj"],
                  "pages" : page_obj["pages"],
                  "tag": tag})

def Login(request):
    print(request.POST)
    if request.method == "POST":
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user is not None:
            login(request, user)
            print('logged')
            return redirect(reverse('startpage'))
        else:
            print("not logged")
    return render(request, "HW1/login.html", ExternalData(request))

def log_out(request):
    logout(request)

    return redirect(reverse('startpage'))

def settings(request):

    return render(request, "HW1/settings.html", ExternalData(request) | {"form" : settingsForm})