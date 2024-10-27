from django.shortcuts import render
from football.forms import clubform

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def player_view(request):
    return render(request,'player.html')


def club_view(request):
    return render(request,'club.html')


def season_view(request):
    return render(request, 'season.html')

def fixture_view(request):
    return render (request,'fixture.html')

def clubform_view(request):
    if request.method == "POST":
        club_form = clubform(request.post)

        if club_form.is_valid():
            club_form.save()
   


