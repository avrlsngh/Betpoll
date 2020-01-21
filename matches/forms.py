from django import forms
from . import models

class addMatchForm(forms.ModelForm):
    class Meta:
        model = models.Match
        fields = [
            'game',
            'match_desc',
            'player_1',
            'player_2',
            'match_start_time',
            'match_end_time',
            'match_day',
            'match_coordinators',
            'match_round'
        ]