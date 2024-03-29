"""
URL configuration for DataFutbolProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from UsersAuth import views
from .views import chatbot


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',chatbot, name='chatbot'),
    path('jugadores/',views.jugadores, name='jugadores'),
    path('registrarJugador/',views.registrarJugador),
    path('jugadores/eliminacionJugador/<int:jugador_id>',views.eliminarJugador),
    path('jugadores/edicionJugador/<int:jugador_id>',views.editarJugador),
    path('editarJugador/',views.editarJugadorTemplate),
    path('equipos/',views.equipos, name='equipos'),
    path('competiciones/',views.competiciones, name='competiciones')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
