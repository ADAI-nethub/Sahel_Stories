# 🗺️ This is the map of our village
urlpatterns = [
    path('admin/', admin.site.urls),       # 👨‍💼 The office for grown-ups who manage the village
    path('', home, name='home'),           # 🏠 The welcome sign at the entrance
    path('stories/', include('stories.urls')),  # 📖 The street where all the storytellers live
    path('api/', include('stories.urls_api')),  # 📡 A secret tunnel for robots (API)
]


#Think of urls.py like a map of your favorite amusement park.
#The map shows where the roller coaster is, where to get cotton candy, and where the bathroom is.
#If there’s no map, everyone gets lost.
#This file is the map for your website!