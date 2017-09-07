from django.shortcuts import render

# Create your views here.


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


                context = {
                    'gerechten' : gerechten
                }

                return render(request, 'index.html', context)

            else:
                context = {
                    'gerechten' : gerechten
                }
                return render(request, 'index.html', context)



