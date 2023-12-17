from django.conf.urls.static import static
from django.urls import path

from HW import settings
from . import views

urlpatterns = [
    # path()
    path('question/<int:question_id>', views.PRODquestionById, name = "questionById"),
    path('Addquestion', views.PRODaddquestion, name = "Addquestion"),
    path('question/<str:tag>/', views.PRODquestionByTag, name = "questionByTag"),
    path('signup', views.PRODconstructregistration, name = "registration"),
    path('login', views.Login, name = "login"),
    path('logout', views.log_out, name='logout'),
    path('profile/<int:profile_id>', views.profileById, name = "profileById"),
    path('settings', views.settings, name='settings'),
    path('', views.PRODquestions, name = 'startpage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)