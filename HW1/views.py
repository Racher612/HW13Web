import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *
from .international import *

language = "english"

@csrf_exempt
def changeLanguage(request):
    data = json.loads(request.body)
    global language
    language = list((set(languages.keys()) - set([language])))[0]

    return redirect(reverse('startpage'))




def ExternalData(request):
    try:
        taglist = Tag.objects.hottestTags()
    except:
        taglist = []
    try:
        members = Profile.objects.random10()
    except:
        members = []

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
            'members' : members} | languages[language]


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


def handler404(request, *args, **argv):
    return render(request, "404.html", ExternalData(request))


def handler500(request, *args, **argv):

    return render(request, "500.html", ExternalData(request))

def PRODquestionById(request, question_id):
    mainquestion = Question.objects.questionById(question_id)[0]
    commentlist = Comment.objects.commentbyquestion(mainquestion)

    page_obj = paginator(request, commentlist)

    if request.method == "POST":
        text = request.POST.get("comment")
        comment = Comment(user = request.user.profile,
                          question = mainquestion,
                          description = text,
                          isuseful = False,
                          likenum = 0,
                          dislikenum = 0,
                          )
        Comment.objects.bulk_create([comment])
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return render(request, "HW1/question.html", ExternalData(request) | {'pages': page_obj["pages"],
                                                                  'mainquestion': mainquestion,
                                                                  'commentlist': page_obj["page_obj"],
                                                             })

def PRODquestions(request):

    page_obj = paginator(request, Question.objects.all())

    return render(request, "HW1/index.html", ExternalData(request) |
                  {"questionlist" : page_obj["page_obj"],
                  "pages" : page_obj["pages"]})

def PRODaddquestion(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        data = json.loads(request.body)


        tags = list(filter(lambda x: x != '', [data[f"tag{i + 1}"] for i in range(7)]))
        tags = [Tag.objects.createTag(item) for item in tags]

        question = Question(user = request.user.profile,
                            question_name = data["title"],
                            question_description = data["text"],
                            date = date.today(),
                            likenum = 0,
                            dislikenum = 0)

        q = Question.objects.bulk_create([question])[0]

        q.taglist.set(tags)
        return redirect(reverse('questionById', args=[q.id]))

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

def PRODquestionBySearch(request, search):
    questionsByDescr = Question.objects.filter(question_description__startswith=search)
    questionsByName = Question.objects.filter(question_name__startswith=search)
    questionlist = list(questionsByName) + list(questionsByDescr)

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/questionBySearch.html", ExternalData(request) |
                  {"questionlist": page_obj["page_obj"],
                  "pages": page_obj["pages"],
                  "search": search})

def Login(request):
    if request.method == "POST":
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

        if user is not None:
            profile = Profile.objects.filter(user = user)[0]
            questionlikes = Questionlikes.objects.filter(user=profile)
            questionlist = list(map(lambda x: x.question, questionlikes))

            for item in questionlist:
                like = list(filter(lambda x: x.question == item, questionlikes))
                is_liked = False
                is_disliked = False
                if like:
                    rate = like[0].like
                    if rate:
                        is_liked = True
                    else:
                        is_disliked = True

                item.is_liked = is_liked
                item.is_disliked = is_disliked
                item.save(update_fields=["is_liked", "is_disliked"])

            del questionlist
            del questionlikes

            commentlikes = Commentlikes.objects.filter(user = profile)
            commentlist = list(map(lambda x: x.comment, commentlikes))
            i = 0

            for item in commentlist:
                like = list(filter(lambda x: x.comment == item, commentlikes))
                is_liked = False
                is_disliked = False
                if like:
                    rate = like[0].like
                    if rate:
                        is_liked = True
                    else:
                        is_disliked = True

                item.is_liked = is_liked
                item.is_disliked = is_disliked
                item.save(update_fields=["is_liked", "is_disliked"])
                i+=1

            login(request, user)
            return redirect(reverse('startpage'))
    return render(request, "HW1/login.html", ExternalData(request))

def log_out(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user = request.user)[0]
        commentlikes = Commentlikes.objects.filter(user=profile)
        questionlikes = Questionlikes.objects.filter(user=profile)
        logout(request)

        questionlist = list(map(lambda x: x.question, questionlikes))
        commentlist = list(map(lambda x: x.comment, commentlikes))
        for item in questionlist:
            item.is_liked = False
            item.is_disliked = False
            item.save(update_fields=["is_liked", "is_disliked"])

        for item in commentlist:
            item.is_liked = False
            item.is_disliked = False
            item.save(update_fields=["is_liked", "is_disliked"])

    return redirect(reverse('startpage'))

@login_required
def settings(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.method == "GET":
        form = settingsForm(initial = model_to_dict(request.user), instance = request.user)

    elif request.method == "POST":
        form = settingsForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save(request)

    else:
        form = settingsForm(instance=request.user)

    return render(request, "HW1/settings.html", ExternalData(request) | {"form" : form})

def profileById(request, profile_id):
    profile = Profile.objects.filter(user_id = profile_id)[0]
    questionlist = Question.objects.filter(user = profile)
    commentnum = Comment.objects.filter(user = profile).count()

    return render(request, "HW1/profileByID.html", ExternalData(request) | {"profile" : profile,
                                                                            "questionlist" : questionlist,
                                                                            "commentnum" : commentnum,
                                                                            "questionum" : len(questionlist)})
@login_required
@csrf_exempt
def like(request):
    data = json.loads(request.body)
    like = data.get('like')
    id = int(data.get('question_id'))
    profile = Profile.objects.filter(user = request.user)[0]
    question = Question.objects.get(id = int(id))
    values = Questionlikes.objects.toggle_like(user = profile, question = question, like = like)
    if like:
        question.is_liked = True
        question.is_disliked = False
        question.save(update_fields = ["is_liked", "is_disliked"])
    else:
        question.is_disliked = True
        question.is_liked = False
        question.save(update_fields = ["is_disliked", "is_liked"])

    return JsonResponse(values)

@login_required
@csrf_exempt
def commentlike(request):
    data = json.loads(request.body)
    like = data.get('like')
    id = int(data.get('comment_id'))
    profile = Profile.objects.filter(user = request.user)[0]
    comment = Comment.objects.get(id = int(id))
    values = Commentlikes.objects.toggle_like(user = profile, comment = comment, like = like)
    if like:
        comment.is_liked = True
        comment.is_disliked = False
        comment.save(update_fields = ["is_liked", "is_disliked"])
    else:
        comment.is_disliked = True
        comment.is_liked = False
        comment.save(update_fields = ["is_disliked", "is_liked"])

    return JsonResponse(values)

@csrf_exempt
def search(request):
    inp = json.loads(request.body).get("search")

    questionsByDescr = Question.objects.filter(question_description__startswith = inp)
    questionsByName = Question.objects.filter(question_name__startswith = inp)
    questionlist = sorted(list(questionsByDescr) + list(questionsByName),
                          key = lambda x: x.likenum + x.dislikenum)

    return JsonResponse({"FoundQuestions" : list(map(lambda x: x.question_name, questionlist))})

