from django.contrib import admin

from django.urls import path

from rotinew import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.disp),
    path('navigate', views.dispnav),
    path('registration',views.memo),
    path('login',views.memory)
]
