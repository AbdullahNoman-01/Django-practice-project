from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('frist_app/', include("frist_app.urls")),
    path('',views.index),
]
