from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.sign_in, name = 'login'),
    path('logout/', views.sign_out, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search_results, name='search_results'),
    path('profile/', views.user_profile, name='user_profile'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)