from django.conf.urls import url
from . import views

app_name = "matches"
urlpatterns = [
    url(r'^$', views.viewMatches, name="viewMatches"),
    url(r'^voteMatch/$', views.voteMatch, name="voteMatch"),
    url(r'^addmatch/$', views.addMatch, name="addMatch"),
    url(r'^addComment/(?P<status>[\w-]+)/$', views.addComment, name="addComment"),
    url(r'^(?P<id>[\w-]+)/$', views.detailMatch, name="detailMatch"),
]