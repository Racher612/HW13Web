import datetime


def main(ratio):
    ratio = 10
    fake: Faker = Faker()

    #Generation of tags
    tags = [
        Tag(tag = fake.unique.pystr(max_chars = 7))
        for i in range(ratio)
    ]
    Tag.objects.bulk_create(tags)

    print("tags successfully generated")

    #Generation of users
    users = [
        User(username=fake.unique.user_name(),
             email=fake.email(),
             password=fake.password(special_chars=False, length = random.randint(8, 16),  upper_case = True))
        for i in range(ratio)]
    User.objects.bulk_create(users)

    #Generating profles
    path1 = "HW1/static/HW1/img/avatars/"
    path2 = "HW1/img/avatars/"
    filelist = os.listdir(path1)
    length = len(filelist)
    profiles = [
        Profile(user=users[i],
                avatar = path2 + filelist[random.randint(0, length - 1)])
        for i in range(ratio)]
    Profile.objects.bulk_create(profiles)

    print("profiles generated")
    print(f"there are ${Profile.objects.count()} now")

    #Generation of questions
    questions = [Question(user=profiles[i//10],
                     question_name=fake.text(max_nb_chars=16),
                     question_description = fake.text(),
                 date = datetime.date(random.randint(2010, 2024), random.randint(1, 12), random.randint(1, 28)),
                          likenum = 0,
                          dislikenum = 0)
                 for i in range(ratio * 10)]

    #Generating questionlikes
    questionlikes = []
    for i in range(ratio * 10 * 100):
        like = bool(random.randint(0, 2))
        questionlikes.append(Questionlikes(user = profiles[i // 1000],
                     question = questions[i // 100],
                     like = like))
        if like:
            questions[i//100].likenum += 1
        else:
            questions[i//100].dislikenum += 1

    Question.objects.bulk_create(questions)
    Questionlikes.objects.bulk_create(questionlikes)
    print("questions generated")
    print(f"there are ${len(Question.objects.all())} questions now")
    # Setting Tags
    for question in Question.objects.all():
        question.taglist.set([fake.random_element(tags) for i in range(random.randint(3, 6))])
    print("tags successfully set")

    # Generating comments
    comments = [
        Comment(user=profiles[i // 100],
                description=fake.text(),
                question=fake.random_element(questions),
                isuseful=fake.pybool(),
                likenum=0,
                dislikenum=0)
        for i in range(ratio * 100)
    ]

    # Generationg commentlikes
    commentlikes = []
    for i in range(ratio * 100 * 100):
        like = bool(random.randint(0, 2))
        commentlikes.append(Commentlikes(user=profiles[i // 10000],
                                         comment=comments[i // 1000],
                                         like=like))
        if like:
            comments[i // 100].likenum += 1
        else:
            comments[i // 100].dislikenum += 1
    Comment.objects.bulk_create(comments)
    Commentlikes.objects.bulk_create(commentlikes)

    print(f"everything successfully created")

    print(f"there are ${len(Comment.objects.all())} comments now")

if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HW.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker
    from HW1.models import *

    main(10)