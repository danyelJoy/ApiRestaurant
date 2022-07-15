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
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            restaurants = list(Restaurant.objects.filter(id=id).values())
            if len(restaurants) > 0:
                company = restaurants[0]
                datos = {'message': "Success", "companies": company}
            else:
                datos = {'message': "Companies not found.."}
            return  JsonResponse(datos)
        else:
            companies = list(Restaurant.objects.values())
            if len(companies) > 0:
                datos = {'message': "Succes", 'companies': companies}
            else:
                datos = {'message': "Companies not found.."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        Restaurant.objects.create(name=jd['name'], type_restaurant=jd['type_restaurant'], address=jd['address'], phone=jd['phone'] )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            restaurant = Restaurant.objects.get(id=id)
            restaurant.name = jd['name']
            restaurant.type_restaurant = jd['type_restaurant']
            restaurant.address = jd['address']
            restaurant.phone = jd['phone']
            restaurant.save()
            datos = {'message': "Succes"}
        else:
            datos = {'message': "Companies not found.."}
        return  JsonResponse(datos)

    def delete(self, request, id):
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            Restaurant.objects.filter(id=id).delete()
            datos = {'message': "Succes"}
        else:
            datos = {'message': "Companies not found.."}
        return JsonResponse(datos)