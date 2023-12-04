

def main(ratio):

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
        User(username = fake.unique.user_name(),
             email = fake.email(),
             password = fake.password(special_chars=False, length = random.randint(8, 16),  upper_case = True))
        for i in range(ratio)]
    User.objects.bulk_create(users)

    print("users succesfully generated")

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

    del users
    gc.collect()

    print("profiles generated")
    print(f"there are ${Profile.objects.count()} profiles now")

    #Generation of questions
    questionum = 10
    questions = [Question(user=profiles[i//10],
                     question_name=fake.text(max_nb_chars=16),
                     question_description = fake.text(),
                 date = datetime.date(random.randint(2010, 2024), random.randint(1, 12), random.randint(1, 28)),
                          likenum = 0,
                          dislikenum = 0)
                 for i in range(ratio * questionum)]

    print("questions generated")


    #Generating questionlikes
    questionlikes = []
    corner = 0
    questionlikesnum = 100
    for i in range(ratio * questionlikesnum * questionum):
        if i % 1000000 == 0:
            Question.objects.bulk_create(questions[corner : i])
            corner = i
            Questionlikes.objects.bulk_create(questionlikes)
            questionlikes = []
            print("cleaned")
        like = bool(random.randint(0, 2))
        questionlikes.append(Questionlikes(user = profiles[i // questionlikesnum // questionum],
                     question = questions[i // questionlikesnum],
                     like = like))
        if like:
            questions[i//questionlikesnum].likenum += 1
        else:
            questions[i//questionlikesnum].dislikenum += 1

    if questions[corner: ratio * questionlikesnum * questionum]:
        Question.objects.bulk_create(questions[corner : ratio * questionlikesnum * questionum])
    if questionlikes:
        Questionlikes.objects.bulk_create(questionlikes)

    print(f"there are ${Question.objects.count()} questions now")
    print("question likes successfully generated")
    print(f"there are ${Questionlikes.objects.count()} questionlikes now")

    del questionlikes
    gc.collect()

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

    del questions
    gc.collect()

    print("comments generated")


    # Generationg commentlikes
    corner = 0
    commentlikes = []
    commentnum = 10
    for i in range(ratio * 100 * commentnum):

        if i % 1000000 == 0:
            Comment.objects.bulk_create(comments[corner : i])
            corner = i
            Commentlikes.objects.bulk_create(commentlikes)
            commentlikes = []
            print("cleaned")
        like = bool(random.randint(0, 2))
        commentlikes.append(Commentlikes(user=profiles[i // 1000],
                                         comment=comments[i // commentnum],
                                         like=like))
        if like:
            comments[i // commentnum].likenum += 1
        else:
            comments[i // commentnum].dislikenum += 1

    if comments[corner : ratio * 100 * 10]:
        Comment.objects.bulk_create(comments)
    if commentlikes:
        Commentlikes.objects.bulk_create(commentlikes)

    print(f"there are ${Comment.objects.count()} comments now")
    print(f"commentlikes successfully created")
    print(f"there are ${Commentlikes.objects.count()} commentlikes now")
    print(f"everything successfully created")

if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HW.settings")
    application = get_wsgi_application()
    import time
    import random
    import datetime
    import gc
    from faker import Faker
    from HW1.models import *

    start_time = time.time()

    main(1000)
    print("--- %s seconds ---" % (time.time() - start_time))