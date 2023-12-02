from django.urls import path
from . import views

urlpatterns = [
    # path()
    path('question/<int:question_id>', views.PRODquestionById, name = "questionById"),
    path('Addquestion', views.PRODaddquestion, name = "Addquestion"),
    path('question/<str:tag>', views.PRODquestionByTag, name = "questionByTag"),
    path('signup', views.PRODconstructregistration, name = "registration"),
    path('login', views.PRODconstructlogin, name = "login"),
    path('', views.PRODquestions, name = 'startpage')
]
