from django.conf.urls import url
from . import views

app_name = "matches"
urlpatterns = [
    url(r'^$', views.viewMatches, name="viewMatches"),
]