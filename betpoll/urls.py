from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^matches/', include('matches.urls')),
]

urlpatterns += staticfiles_urlpatterns()
