import sys, os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from django.views.static import serve

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure the static directory exists
STATIC_DIR = os.path.join(BASE_DIR, 'static')
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

settings.configure(
    DEBUG = True,
    SECRET_KEY = 'django-insecure-!!e_h5x0i3u1=34w3r0r&pz(*&-fzc(@_f1js7&aem$tar_x^6',
    ALLOWED_HOSTS = ['*'],
    ROOT_URLCONF=__name__,
    STATIC_URL='/static/',
    STATICFILES_DIRS=[STATIC_DIR],
)

# Define a common base template
BASE = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="/static/style.css">
    </head>
    <body>
        {content}
    </body>
    </html>
    '''

Name = 'Prag'

def home_view(request, *args, **kwargs):
    content = f'''<h1 class="header">Hello {Name}</h1><br>
                <a href="/about">About Me</a><br>
                <img src="/static/hero.png">
                '''
    return HttpResponse(BASE.format(title='Home', content=content))

def about_view(request, *args, **kwargs):
    content = f'''<h1 class="header">About {Name}</h1><br>
                <p>Proficiency in <br>PHP, Laravel, Python, Django, ORM, MySQL, MariaDB, SQLite3, Oracle 19c, React JS, Git</p><br>
                <a href="/">Return to Home</a>'''
    return HttpResponse(BASE.format(title='About', content=content))

urlpatterns = [
    path('', home_view),
    path('about', about_view),
    path('static/<path:path>', serve, {'document_root': STATIC_DIR}),
]

application = get_wsgi_application()

if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)