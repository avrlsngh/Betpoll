from django.db import models
from django.contrib.auth.models import User
from .choices import GAME_CHOICES, DATE_CHOICES
# from accounts.models import User


class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    game = models.CharField(max_length=15, choices=GAME_CHOICES, default='Kabaddi')
    player_1 = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    player_1_votes = models.IntegerField(default=0, null=True)
    player_2 = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    player_2_votes = models.IntegerField(default=0, null=True)
    match_start_time = models.CharField(max_length=10, default=None, null=False, blank=False)
    match_end_time = models.CharField(max_length=10, default=None, null=False, blank=False)
    match_day = models.CharField(max_length=50, choices=DATE_CHOICES, default='2020-01-22')
    match_coordinators = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    match_round = models.CharField(
        max_length=250, default=None, null=False, blank=False)
    match_desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.game)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    match = models.ForeignKey(
        'matches.Match', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(
        max_length=1500, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.match) + " - " + str(self.user)

class UserRight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Votes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    vote_side = models.IntegerField(default=None, null=True)
    match = models.ForeignKey(Match, on_delete = models.CASCADE, default=None)

    def __str__(self):
        return str(self.match) + " - " + str(self.user)

