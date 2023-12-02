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

def ExternalData():
    # taglist = tagManager.all()
    # members = profileManager.best()
    return {'name' : name,
            'link' : src,
            'taglist' : taglist,
            'members' : members,}


class question:
    id = 0
    question_name = "How to get out of here?"
    question_description = "I do really wonder how can I get OUT of here"
    answers_count = 7
    src = "../static/HW1/img/Tyler.jpg"
    tag1 = "tag1"
    tag2 = "tagtag2"
    tsg3 = "tagtagtag3"
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


def paginator(request, structure):
    paginator = Paginator(structure, 20)

    pagenum = request.GET.get('page')
    if pagenum == None:
        pagenum = 1

    page_obj = paginator.get_page(pagenum)
    pages = paginator.page_range
    length = len(pages)

    symbols = ["1", "<", pagenum, ">", str(length)]
    requiredpages = list(map(str, [pages[0], max(int(pagenum) - 1, 1), int(pagenum), min(int(pagenum) + 1, length), length]))


    return {"page_obj" : page_obj,
            "pages" : [{"sym" : symbols[i], "val" : requiredpages[i]} for i in range(5)]}

def PRODquestionById(request, question_id):
    mainquestion = Question.objects.questionById(question_id)[0]
    commentlist = Comment.objects.commentbyquestion(mainquestion)

    page_obj = paginator(request, commentlist)

    return render(request, "HW1/question.html", ExternalData() | {'pages': page_obj["pages"],
                                                                  'mainquestion': mainquestion,
                                                                  'commentlist': page_obj["page_obj"],
                                                             })

def PRODquestions(request):
    questionlist = Question.objects.all()

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/index.html", ExternalData() | {"questionlist" : page_obj["page_obj"],
                                                               "pages" : page_obj["pages"]})

def PRODaddquestion(request):
    return render(request, "HW1/Addquestion.html", ExternalData())

def PRODconstructregistration(request):
    return render(request, "HW1/registration.html", ExternalData())

def PRODconstructlogin(request):
    return render(request, "HW1/login.html", ExternalData())

def PRODquestionByTag(request, tag):
    tagname = Tag.objects.tagbyname(tag)
    questionlist = Question.objects.questionByTag(tagname)

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/questionByTag.html", ExternalData() | {"questionlist" : page_obj["page_obj"],
                                                               "pages" : page_obj["pages"],
                                                                       'tag': tag})

def questionByTag(request, tag):

    questionlist = getdata()

    page_obj = paginator(request, questionlist)

    return render(request, "HW1/questionByTag.html", {'name': name,
                                              'link': src, 'taglist': taglist,
                                              'page_obj': page_obj,
                                              'members': members,
                                              'tag' : tag,
                                              'questionlist': list(filter(lambda x: tag in x.taglist, page_obj.object_list))})
def getdata():
    data = []
    for i in range(50):
        item = question()
        item.id = i + 1
        item.taglist = item.taglist[random.randint(0, 3) : random.randint(3, 9)]
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




def fun2(request):
    return render(request, 'HW1/base.html')