from backend.wsgi import applicationimport os
import sys

# Add the directory containing your Django project to the Python path
django_project_path = "/home/shashankpathe1/realyou"
sys.path.append(django_project_path)

# Set the environment variable to tell Django which settings module to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Set the application object
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
