from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleanLiness",
            "location",
            "check_in",
            "value",
        )

    def save(self, commit=True):
        return super().save(commit=False)
