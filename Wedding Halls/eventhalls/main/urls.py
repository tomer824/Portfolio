from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.main, name = 'main'),
    path('accounts/', include('django.contrib.auth.urls')),
]

