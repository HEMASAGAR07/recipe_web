from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, "home.html")

def recipe_view(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_discription = request.POST.get('recipe_discription')
        recpie_image = request.FILES.get('recpie_image')

        print(recipe_name)
        print(recipe_discription)

        recipe.objects.create(

            recipe_name=recipe_name,
            recipe_discription=recipe_discription,
            recpie_image=recpie_image,)

        return redirect('/recipe')
    recipes = recipe.objects.all()

    if request.GET.get('search'):
        recipes =  recipes.filter(recipe_name__icontains = request.GET.get('search'))
        recipes = recipes.filter(recipe_discription__icontains=request.GET.get('search'))

    return render(request, "recipe.html", {'recipes': recipes})


def update_recipe(request, id):
    recipes = recipe.objects.get(id=id)
    context = {'recipes': recipes}

    if request.method == "POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_discription = request.POST.get('recipe_discription')
        recpie_image = request.FILES.get('recpie_image')

        recipes.recipe_name=recipe_name
        recipes.recipe_discription=recipe_discription

        if recpie_image:
            recipes.recpie_image=recpie_image

        recipes.save()
        return redirect('/recipe')
    return render(request, "update_recipe.html", context)


def delete_recipe(request, id):
    recipes=recipe.objects.get(id=id)
    recipes.delete()




    return redirect('/recipe/')