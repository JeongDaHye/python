
from django.contrib import admin
from django.urls import path
import boot.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', boot.views.index, name="index"),
]
