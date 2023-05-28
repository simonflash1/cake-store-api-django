from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .models import Cake
from django.views.decorators.csrf import csrf_exempt

def get_all_cakes(request):
    cakes = Cake.objects.all()
    data = []
    for cake in cakes:
        cake_data = {
            'id': cake.id,
            'name': cake.name,
            'description': cake.description,
            'price': str(cake.price),
        }
        data.append(cake_data)
    return JsonResponse(data, safe=False)

def get_cake(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    data = {
        'id': cake.id,
        'name': cake.name,
        'description': cake.description,
        'price': str(cake.price),
    }
    return JsonResponse(data)

@csrf_exempt
def create_cake(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        cake = Cake.objects.create(name=name, description=description, price=price)
        
        data = {
            'id': cake.id,
            'name': cake.name,
            'description': cake.description,
            'price': str(cake.price),
        }
        
        return JsonResponse(data, status=201)
    
    return render(request, 'create_cake.html')

def update_cake(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        cake.name = name
        cake.description = description
        cake.price = price
        cake.save()

        data = {
            'id': cake.id,
            'name': cake.name,
            'description': cake.description,
            'price': str(cake.price),
        }
        return JsonResponse(data, status=200)

    data = {
        'id': cake.id,
        'name': cake.name,
        'description': cake.description,
        'price': str(cake.price),
    }
    return render(request, 'update_cake.html', {'cake': cake})

@csrf_exempt
def delete_cake(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cake.delete()
    return JsonResponse({'message': 'Cake deleted successfully'}, status=204)
