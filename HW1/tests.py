from datetime import date

from django.test import TestCase
from .models import *

class TestClass(TestCase):
    def setUp(self):
        tag1 = Tag(tag = "tag1")
        tag2 = Tag(tag ="tag2")
        Tag.objects.bulk_create([tag1, tag2])

        user = User(username = "User1", password = "AAaa12516")
        User.objects.bulk_create([user])

        profile = Profile(user = user)
        Profile.objects.bulk_create([profile])

        question = Question(user = profile, question_name = "Question1",
                                question_description = "This is question1",
                                date = date(2024, 12, 9),
                                likenum = 0,
                                dislikenum = 0)
        Question.objects.bulk_create([question])

        question.taglist.set([tag1, tag2])
        questionlike = Questionlikes(user = profile, question = question, like = True)

        Questionlikes.objects.bulk_create([questionlike])
        question.likenum += 1
        question.save(update_fields = ['likenum'])

        comment = Comment(user = profile, description = "This is comment", question = question,
                          isuseful = False, likenum = 0, dislikenum = 0)
        Comment.objects.bulk_create([comment])

        commentlike = Commentlikes(user = profile, comment = comment, like = False)
        Commentlikes.objects.bulk_create([commentlike])
        comment.dislikenum += 1
        comment.save(update_fields = ['dislikenum'])

    def test1(self):
        tag = Tag.objects.get(tag = "tag1")
        user = User.objects.filter(username = "User1")[0]
        profile = Profile.objects.filter(user=user)[0]
        question = Question.objects.filter(question_name = "Question1")[0]
        comment = Comment.objects.filter(description = "This is comment")[0]

        self.assertEqual(tag.tag, "tag1")
        self.assertEqual(question.question_name, "Question1")
        self.assertEqual(comment.description, "This is comment")
        self.assertEqual(question.likenum, 1)
        self.assertEqual(comment.dislikenum, 1)

        questionlike = Questionlikes.objects.filter(user = profile, like = True)[0]
        commentlike = Commentlikes.objects.filter(user=profile, comment=comment, like=False)[0]

        Questionlikes.objects.toggle_like(user = profile, question = question, like=True)
        Commentlikes.objects.toggle_like(user = profile, comment = comment, like = False)

        self.assertEqual(question.likenum, 0)
        self.assertEqual(question.dislikenum, 0)


