from django.db import models
from django.contrib.auth.models import User


class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    match_name = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    game = models.CharField(max_length=250, default=None,
                            null=False, blank=False)
    player_1 = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    player_2 = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    match_start_time = models.DateTimeField()
    match_end_time = models.DateTimeField()
    match_day = models.IntegerField(default=None, null=False, blank=False)
    match_coordinators = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    match_round = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    match_desc = models.TextField(blank=True)
    created_at = created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    match = models.ForeignKey(
        'matches.Match', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(
        max_length=1500, default=None, null=True, blank=True)
