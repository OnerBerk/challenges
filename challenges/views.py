from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "something in January"
    elif month == 'february':
        challenge_text = "something in february"
    elif month == 'march':
        challenge_text = "something in march"
    elif month == 'april':
        challenge_text = "something in april"
    elif month == 'may':
        challenge_text = "something in may"
    else:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)
