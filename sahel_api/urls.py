# 📘 sahel_api/urls.py
# Ce fichier est comme la carte 🗺️ de tout ton site web Django.
# Il décide quelle page montrer quand quelqu'un visite un lien particulier.

<<<<<<< HEAD
from django.contrib import admin  # 👨‍💼 Importe le panneau d'administration
from django.urls import path, include  # 📍 Importe les outils pour créer des chemins
from django.http import HttpResponse  # 📝 Importe l'outil pour écrire une réponse simple
=======

from django.contrib import admin  # 👨‍💼 Importe le panneau d'administration
from django.urls import path, include  # 📍 Importe les outils pour créer des chemins
from django.http import HttpResponse  # 📝 Importe l'outil pour écrire une réponse simple
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)

# 🏠 Crée une petite fonction qui dit "Bienvenue !" quand on visite la page d'accueil
def root_home(request):
    return HttpResponse("Welcome to Sahel Stories!")

# 🗺️ Liste de tous les chemins (URLs) que ton site comprend
urlpatterns = [
    # 👨‍💼 Quand quelqu'un va vers /admin/, montre le panneau d'administration
    path('admin/', admin.site.urls),
    
<<<<<<< HEAD
=======
    
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)
    # 🏠 Quand quelqu'un va sur la page d'accueil (juste /), montre le message de bienvenue
    path('', root_home, name='root_home'),
    
    # 📖 Quand quelqu'un va vers /stories/, regarde dans le fichier urls.py de l'app "stories"
    path('stories/', include('stories.urls')),      # pages du site web
    
    # 🔌 Quand quelqu'un va vers /api/, regarde dans le fichier urls_api.py de l'app "stories"
    path('api/', include('stories.urls_api')),      # points de terminaison d'API
<<<<<<< HEAD
]
=======
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)
