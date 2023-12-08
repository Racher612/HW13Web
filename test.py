

def authen():
    user = User.objects.filter(id = 3)
    au = authenticate(username = user.username, password = user.password)
    print(au)

if __name__ == "__main__":
    import os

    # from django.core.wsgi import get_wsgi_application
    os.environ.setdefault("INSTALLED_APPS", "HW.settings")
    from django.contrib.auth import login, authenticate, logout
    from django.contrib.auth.models import User
    from django.core.files import File
    from django.db import models

    authen()