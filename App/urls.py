from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name="App"
urlpatterns = [
    path("",views.index,name="index")
]
