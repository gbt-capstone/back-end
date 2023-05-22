import requests
import json
from django.shortcuts import render
from .models import Toilet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
# def main(request):
#     toilet = Toilet.objects.get(pk=1)

#     return render(request, 'index.html', {'toilet': toilet})

@csrf_exempt
def fetch_and_save_toilet_data(request):
    
    if request.method == 'POST':
    
        # api에서 화장실 데이터 가져옴           
        url = 'https://api.odcloud.kr/api/15060017/v1/uddi:9be26c73-d883-42cf-ab36-d1a4de6cb092'
        params = {
            'page' : '1',
            'perPage' : '55',
            'serviceKey' : 'Yjfhlzh4/q093RDD02gGdgsyNS5/0zTokDDakWMiQadcJNTpwPsw0eXqseRBNBhNnqO47gOUyXmAs+VC9TqdTQ=='
        
        }
    
        response = requests.get(url, params=params)
    
        if response.status_code == 200:
            data = response.json()
            toilets = data['data']
    
            for toilet_data in toilets:
                toilet = Toilet(
                    id = toilet_data['연번'],
                    area = toilet_data['지역'],
                    name = toilet_data['명칭'],
                    address = toilet_data['소재지'],
                    using = toilet_data['주용도'],
                    bellYN = toilet_data['비상벨 여부']
                )
                toilet.save()
                
            return JsonResponse({'message' : 'Success'})        

        elif response.status_code == 401:
            return JsonResponse({'message': 'Error'})
    
        else:
            return JsonResponse({'message': 'API request failed'})

@csrf_exempt
def create_toilet(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get("id")
        area = data.get("area")
        name = data.get("name")
        address = data.get("address")
        using = data.get("using")
        bellYN = data.get("bellYN")
        
        if Toilet.objects.filter(id=id).exists():
            response_data = {
                'message': 'Error',
                'error': 'Already exist ID'
            }
            return JsonResponse(response_data, status=400)

        toilet = Toilet(
            id=id,
            area=area,
            name=name,
            address=address,
            using=using,
            bellYN=bellYN
        )
        toilet.save()
        
        response_data = {
            'message' : 'Success'
        }
        
        return JsonResponse(response_data)
    
@csrf_exempt
def get_toilet(request):
    toilet_id = request.GET.get('id')
    if toilet_id:
        try:
            toilet = Toilet.objects.get(id=toilet_id)
            toilet_data = {
                'id': toilet.id,
                'area': toilet.area,
                'name': toilet.name,
                'address': toilet.address,
                'using': toilet.using,
                'bellYN': toilet.bellYN
            }
            return JsonResponse(toilet_data)
        except Toilet.DoesNotExist:
            return JsonResponse({'message': 'Toilet not found'}, status=404)
    else:
        return JsonResponse({'message': 'Missing toilet_id parameter'}, status=400)


@csrf_exempt
def get_all_toilets(request):
    if request.method == 'GET':
        toilets = Toilet.objects.all()
        toilet_list = []
        for toilet in toilets:
            toilet_data = {
                'id': toilet.id,
                'area': toilet.area,
                'name': toilet.name,
                'address': toilet.address,
                'using': toilet.using,
                'bellYN': toilet.bellYN
            }
            toilet_list.append(toilet_data)
        return JsonResponse(toilet_list, safe=False)

@csrf_exempt
def update_toilet(request):
    toilet_id = request.GET.get('id')
    if toilet_id:
        try:
            toilet = Toilet.objects.get(id=toilet_id)
            if 'area' in request.GET:
                toilet.area = request.GET.get('area')
            if 'name' in request.GET:
                toilet.name = request.GET.get('name')
            if 'address' in request.GET:
                toilet.address = request.GET.get('address')
            if 'using' in request.GET:
                toilet.using = request.GET.get('using')
            if 'bellYN' in request.GET:
                toilet.bellYN = request.GET.get('bellYN')
            toilet.save()
            return JsonResponse({'message': 'Success'})
        except Toilet.DoesNotExist:
            return JsonResponse({'message': 'Toilet not found'}, status=404)
    else:
        return JsonResponse({'message': 'Missing toilet_id parameter'}, status=400)

@csrf_exempt
def delete_toilet(request):
    toilet_id = request.GET.get('id')
    if toilet_id:
        try:
            toilet = Toilet.objects.get(id=toilet_id)
            toilet.delete()
            return JsonResponse({'message': 'Success'})
        except Toilet.DoesNotExist:
            return JsonResponse({'message': 'Toilet not found'}, status=404)
    else:
        return JsonResponse({'message': 'Missing toilet_id parameter'}, status=400)