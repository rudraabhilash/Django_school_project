
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect,render
from .models import award_winners
from .models import games
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def award_winners_page(request):
  template = loader.get_template('award_winnersdata.html')
  return HttpResponse(template.render())





@csrf_exempt
def submitform(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        game_won_id = request.POST.get('game_won_id')
        date = request.POST.get('date')
        level = request.POST.get('level')
        medal_type = request.POST.get('medal_type')
        achivements = request.POST.get('achivements')

        temp = award_winners(student_id=student_id, game_won_id=game_won_id, date=date, level=level, medal_type=medal_type, achivements=achivements)
        temp.save()


        return redirect('award_data/')
    else:
        return HttpResponse("Invalid requests method.")
    



@csrf_exempt
def award_data(request):
     fetched_data = award_winners.objects.all().values()
     template = loader.get_template('data.html')
     context= {
        'boy': fetched_data,
     }

     return HttpResponse(template.render(context,request))

        
    
@csrf_exempt
def game_data(request):
     any_data = games.objects.all().values()
     template = loader.get_template('gamedata.html')
     context= {
        'cur': any_data,
     }

     return HttpResponse(template.render(context,request))

def home_page(request):
    return render(request,'home_page.html')
        

