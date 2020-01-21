from django.contrib import admin
from .models import Match, Chat, UserRight, Votes

admin.site.register(Match)
admin.site.register(Chat)
admin.site.register(UserRight)
admin.site.register(Votes)
