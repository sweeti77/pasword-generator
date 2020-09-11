from django.shortcuts import render
import random

def homepage(request):
    return render(request, "homepage.html")

def passwordGenerator(request):
    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')

    randompassword = ''

    if (request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if (request.GET.get('numbers')):
        characters.extend(list('0123456789'))

    if (request.GET.get('specialcharacters')):
        characters.extend(list('!@#$%^&*(_-):"?><,./;{|\][=+]}'))

    for i in range(length):
        randompassword += random.choice(characters)

    return render(request, "passwordGenerator.html", {'therandompassword':randompassword})