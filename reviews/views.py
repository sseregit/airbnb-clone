from django.shortcuts import redirect, reverse
from rooms import models as room_models
from . import forms

# Create your views here.
def create_review(request, room):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        room = room_models.Room.objects.get_or_none(pk=room)
        if not room:
            return redirect(reverse("core:hoome"))
        if form.is_valid():
            pass
