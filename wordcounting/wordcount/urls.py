from django.contrib import admin
from django.urls import path
import counting.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', counting.views.index, name="index"),
    path('about/', counting.views.about, name="about"),
    path('result/', counting.views.result, name="result"),
]
