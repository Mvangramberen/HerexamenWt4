from django.shortcuts import render

# Create your views here.


# Get from database

'''
from recepten.models import Gerecht


dbgerecht = Gerecht(naam='fish and chips', ingredienten="vis en frieten", bereidtijd="1 uur", calorieen="teveel")
dbgerecht.save()

gerechtenDbEntry = Gerecht.objects.all()

'''
gerechten= [
    {"naam":"pannekoeken", "ingredienten":"eieren, suiker, melk", "bereidtijd":"15 min", "calorieen":"750"},
    {"naam":"ommelet", "ingredienten":"eieren, zout, peper", "bereidtijd":"10 min", "calorieen":"200"},
    {"naam":"Koeken", "ingredienten":"eieren, suiker, melk", "bereidtijd":"30 min", "calorieen":"800"},
    {"naam":"Noedels", "ingredienten":"Aiki", "bereidtijd":"5 min", "calorieen":"1500"}
]

def recept(request):

            if request.method == 'POST':

                naam = request.POST.get('naam')
                ingredienten = request.POST.get('ingredienten')
                bereidtijd = request.POST.get('bereidtijd')
                calorieen = request.POST.get('calorieen')

                gerechten.append({'naam':naam, 'ingredienten': ingredienten, 'bereidtijd':bereidtijd, 'calorieen':calorieen})

                '''
                dbgerecht = Gerecht(naam=naam, ingredienten=ingredienten, bereidtijd=bereidtijd, calorieen=calorieen)
                dbgerecht.save()

                gerechtenDbEntry = Gerecht.objects.all()
                '''

                context = {

                # 'gerechten' : gerechtenDbEntry
                    'gerechten' : gerechten

                }

                return render(request, 'index.html', context)

            else:
                context = {

                    # 'gerechten' : gerechtenDbEntry
                    'gerechten' : gerechten
                }
                return render(request, 'index.html', context)



