from django.shortcuts import render

from django.shortcuts import render
import random
import datetime


def hello(request):
    return render(request, 'hello.html')


def fun(request):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    ]
    random_joke = random.choice(jokes)
    return render(request, 'fun.html', {'joke': random_joke})


def main(request):
    current_datetime = datetime.datetime.now()
    return render(request, 'main.html', {'current_datetime': current_datetime})
