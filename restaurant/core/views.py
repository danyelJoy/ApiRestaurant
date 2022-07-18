import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Restaurant

class RestaurantView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): #Modifica el comportamiento y salte restriccion
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            restaurants = list(Restaurant.objects.filter(id=id).values())
            if len(restaurants) > 0: #Si la longitud de restaurant
                restaurant = restaurants[0]
                datos = {'message': "Success", "restaurant": restaurant}
            else:
                datos = {'message': "Not found.."}
            return JsonResponse(datos)
        else:
            restaurants = list(Restaurant.objects.values()) #Serializamos json
            if len(restaurants) > 0:
                datos = {'message': "Succes", 'restaurants': restaurants}
            else:
                datos = {'message': "Companies not found.."}
            return JsonResponse(datos)

    def post(self, request):
        jdata = json.loads(request.body)
        Restaurant.objects.create(name=jdata['name'],
                                  type_restaurant=jdata['type_restaurant'],
                                  address=jdata['address'], phone=jdata['phone'] )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jdata = json.loads(request.body)
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            restaurant = Restaurant.objects.get(id=id)
            restaurant.name = jdata['name']
            restaurant.type_restaurant = jdata['type_restaurant']
            restaurant.address = jdata['address']
            restaurant.phone = jdata['phone']
            restaurant.save()
            datos = {'message': "Succes"}
        else:
            datos = {'message': "Not found.."}
        return JsonResponse(datos)

    def delete(self, request, id):
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            Restaurant.objects.filter(id=id).delete()
            datos = {'message': "Succes"}
        else:
            datos = {'message': "Companies not found.."}
        return JsonResponse(datos)