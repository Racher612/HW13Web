from django.urls import path, include
from . import views

urlpatterns = [
    # path()
    path('question/<int:question_id>', views.questionById, name = "questionById"),
    path('Addquestion', views.AddQuestion, name = "Addquestion"),
    path('question/<str:tag>', views.questionByTag, name = "questionByTag"),
    path('signup', views.ConstructRegistration, name = "registration"),
    path('login', views.ConstructLogin, name = "login"),
    path('', views.ConstructIndex, name = 'startpage')
]
