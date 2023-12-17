import random

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
import random

class questionManager(models.Manager):
    def questionById(self, question_id):
        return self.filter(id = question_id)

    def questionByTag(self, tagname):
        try:
            return self.filter(taglist__in = [tagname])
        except:
            return []

    def allquestions(self):
        return self.all()

    def like(self, id):
        quest = self.filter(id = id + 1)[0]
        quest.likenum += 1
        quest.save()

    def dislike(self, id):
        quest = self.filter(id=id + 1)[0]
        quest.dislikenum += 1
        quest.save()


class profileManager(models.Manager):
    def allprofiles(self):
        return self.all()

    def best(self):
        return self.all()[0:6]

    def random10(self):
        return random.choices(self.all(), k = 10)

class tagManager(models.Manager):

    def hottestTags(self):
        return random.sample(list(self.all()), 10)
    def alltags(self):
        return self.all()
    def firstten(self):
        try:
            return self.all()[:6]
        except:
            return self.all()

    def tagbyname(self, tagname):
        try:
            return self.filter(tag = tagname)[0]
        except:
            return ''
    def createTag(self, tagname):
        try:
            return self.filter(tag = tagname)[0]
        except:
            self.create(tagname)
            return self.filter(tag = tagname)[0]

class commentManager(models.Manager):

    def allcomments(self):
        return self.all()

    def commentbyquestion(self, question):
        return self.filter(question = question)

class CommentlikesManager(models.Manager):
    def allcomments(self):
        return self.all()

class QuestionlikesManager(models.Manager):
    def allquestions(self):
        return self.all()


class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    avatar = models.ImageField(null=True, blank=True, default = "default", upload_to = r"HW1\static\HW1\img\avatars")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = profileManager()


    def __str__(self):
        return self.user.__str__()

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20)

    objects = tagManager()
    def __str__(self):
        return self.tag

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_name = models.CharField(max_length=200)
    question_description = models.TextField()

    user = models.ForeignKey(Profile, on_delete = models.SET_NULL, null=True)
    taglist = models.ManyToManyField(Tag, unique = False)
    date = models.DateField(blank=True, null = True)

    likenum = models.IntegerField()
    dislikenum = models.IntegerField()

    objects = questionManager()

    def __str__(self):
        return self.question_name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True)
    description = models.TextField()
    isuseful = models.BooleanField()

    likenum = models.IntegerField()
    dislikenum = models.IntegerField()

    objects = commentManager()

    def __repr__(self):
        return self.description[:50]

    def __str__(self):
        return self.description[:50]

class Commentlikes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, models.PROTECT, null = True)
    comment = models.ForeignKey(Comment, models.PROTECT, null = True)
    like = models.BooleanField()

    objects = CommentlikesManager()

    def __repr__(self):
        return self.user.user.username + self.comment.description[0:50]

    def __str__(self):
        return self.user.user.username + self.comment.description[0:50]

class Questionlikes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, models.PROTECT, null = True)
    question = models.ForeignKey(Question, models.PROTECT, null = True)
    like = models.BooleanField()

    objects = QuestionlikesManager()

    def __repr__(self):
        return self.user.user.username + self.question.question_description[0:50]

    def __str__(self):
        return self.user.user.username + self.question.question_description[0:50]


