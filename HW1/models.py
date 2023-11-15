from django.contrib.auth.models import User
from django.db import models

class questionManager(models.Manager):
    def questionById(self):
        return self.all()

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    login = models.CharField(max_length=25)
    avatar = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    nickname = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_name = models.CharField(max_length=200)
    question_description = models.TextField()

    user = models.ForeignKey(Profile, on_delete = models.SET_NULL, null=True)
    tag1 = models.OneToOneField(Tag, models.SET_NULL, null = True, related_name="tag1")
    tag2 = models.OneToOneField(Tag, models.SET_NULL, null = True, related_name="tag2")
    tag3 = models.OneToOneField(Tag, models.SET_NULL, null = True, related_name="tag3")

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

    def __repr__(self):
        return self.description[:50]

    def __str__(self):
        return self.description[:50]

class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, models.PROTECT, null = True)
    comment = models.ForeignKey(Comment, models.PROTECT, null = True)
    like = models.BooleanField()

    def __repr__(self):
        return self.user.nickname + self.comment.description[0:50]

    def __str__(self):
        return self.user.nickname + self.comment.description[0:50]


