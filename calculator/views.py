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
}

def show_recipe(request, name):
    count = request.GET.get('servings')
    if count:
        pass
    else:
        count = 1
    if DATA.get(name):
        context = {'recipe': {}}
        print(DATA[name])
        for i, a in DATA[name].items():
            print(context)
            context['recipe'].update({i: a*int(count)})
    else:
        context = DATA.get(name)
    return render(request, 'calculator/index.html', context)


