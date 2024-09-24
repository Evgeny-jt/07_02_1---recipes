from django.http import request, HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def menu(request):
    return HttpResponse('Рецеты: omlet, pasta, buter')


def portions(dish, portion):
    context = {}
    recipe = {}
    for ingredient, quantity in dish.items():
        recipe[ingredient] = quantity * portion
    context['recipe'] = recipe
    return context

def omlet(request):
    portion = request.GET.get('servings')
    if portion != None:
        context = portions(DATA['omlet'], int(portion))
    else:
        context = {}
        context['recipe'] = DATA['omlet']
    return render(request, 'calculator/index.html', context)

def pasta(request):
    portion = request.GET.get('servings')
    if portion != None:
        context = portions(DATA['pasta'], int(portion))
    else:
        context = {}
        context['recipe'] = DATA['pasta']
    return render(request, 'calculator/index.html', context)

def buter(request):
    portion = request.GET.get('servings')
    if portion != None:
        context = portions(DATA['buter'], int(portion))
    else:
        context = {}
        context['recipe'] = DATA['buter']
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
