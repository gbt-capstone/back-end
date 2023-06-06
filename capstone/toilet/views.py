import requests
import json
from django.shortcuts import render
from .models import Toilet
from .models import Review
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
        for_disabled = data.get("for_disabled")
        separate = data.get("separate")
        toilet_count = data.get("toilet_count")
        washstand = data.get("washstand")
        hand_sanitizer = data.get("hand_sanitizer")
        toilet_paper = data.get("toilet_paper")
        for_children = data.get("for_children")
        diaper_change = data.get("diaper_change")
        women_safe = data.get("women_safe")
        cleanliness = data.get("cleanliness")
        
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
            bellYN=bellYN,
            for_disabled=for_disabled,
            separate=separate,
            toilet_count=toilet_count,
            washstand=washstand,
            hand_sanitizer=hand_sanitizer,
            toilet_paper=toilet_paper,
            for_children=for_children,
            diaper_change=diaper_change,
            women_safe=women_safe,
            cleanliness=cleanliness
            
            
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
                'bellYN': toilet.bellYN,
                'for_disabled' : toilet.for_disabled,
                'separate' : toilet.separate,
                'toilet_count' : toilet.toilet_count,
                'washstand' : toilet.washstand,
                'hand_sanitizer' : toilet.hand_sanitizer,
                'toilet_paper' : toilet.toilet_paper,
                'for_children' : toilet.for_children,
                'diaper_change' : toilet.diaper_change,
                'women_safe' : toilet.women_safe,
                'cleanliness' : toilet.cleanliness
                
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
                'bellYN': toilet.bellYN,
                'for_disabled' : toilet.for_disabled,
                'separate' : toilet.separate,
                'toilet_count' : toilet.toilet_count,
                'washstand' : toilet.washstand,
                'hand_sanitizer' : toilet.hand_sanitizer,
                'toilet_paper' : toilet.toilet_paper,
                'for_children' : toilet.for_children,
                'diaper_change' : toilet.diaper_change,
                'women_safe' : toilet.women_safe,
                'cleanliness' : toilet.cleanliness
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
            if 'for_disabled' in request.GET:
                toilet.bellYN = request.GET.get('for_disabled')
            if 'separate' in request.GET:
                toilet.bellYN = request.GET.get('separate')
            if 'toilet_count' in request.GET:
                toilet.bellYN = request.GET.get('toilet_count')
            if 'washstand' in request.GET:
                toilet.bellYN = request.GET.get('washstand')
            if 'hand_sanitizer' in request.GET:
                toilet.bellYN = request.GET.get('hand_sanitizer')
            if 'toilet_paper' in request.GET:
                toilet.bellYN = request.GET.get('toilet_paper')
            if 'for_children' in request.GET:
                toilet.bellYN = request.GET.get('for_children')
            if 'diaper_change' in request.GET:
                toilet.bellYN = request.GET.get('diaper_change')
            if 'women_safe' in request.GET:
                toilet.bellYN = request.GET.get('women_safe')
            if 'cleanliness' in request.GET:
                toilet.bellYN = request.GET.get('cleanliness')
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
    
@csrf_exempt
def create_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        toilet_id = data.get("toilet")
        user_name = data.get("user_name")
        review_id = data.get("review_id")
        comment = data.get("comment")
        created_at = data.get("created_at")

        try:
            toilet = Toilet.objects.get(id=toilet_id)
        except Toilet.DoesNotExist:
            response_data = {
                'message': 'Error',
                'error': 'Toilet not found'
            }
            return JsonResponse(response_data, status=400)

        if Review.objects.filter(review_id=review_id).exists():
            response_data = {
                'message': 'Error',
                'error': 'Already exist ID'
            }
            return JsonResponse(response_data, status=400)

        review = Review(
            toilet=toilet,
            user_name=user_name,
            review_id=review_id,
            comment=comment,
            created_at=created_at
        )
        review.save()

        response_data = {
            'message': 'Success'
        }

        return JsonResponse(response_data)
        
@csrf_exempt
def get_review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        review_list = []
        for review in reviews:
            review_data = {
                'user_name': review.user_name,
                'review_id': review.review_id,
                'comment': review.comment,
                'created_at': review.created_at,
                'toilet_id' : review.toilet_id,
            }
            review_list.append(review_data)
        return JsonResponse(review_list, safe=False)

@csrf_exempt
def update_review(request):
    review_id = request.GET.get('review_id')
    if review_id:
        try:
            review = Review.objects.get(review_id=review_id)
            if 'user_name' in request.GET:
                review.user_name = request.Get.get('user_name')
            if 'comment' in request.GET:
                review.comment = request.Get.get('comment')
            review.save()
            return JsonResponse({'message : Success'})
        except Review.DoesNotExist:
            return JsonResponse({'message': 'Review not found'}, status=404)
    else:
        return JsonResponse({'message': 'Missing review_id parameter'}, status=400)
    
@csrf_exempt
def delete_review(request):
    review_id = request.GET.get('review_id')
    if review_id:
        try:
            review = Review.objects.get(review_id=review_id)
            review.delete()
            return JsonResponse({'message': 'Success'})
        except Review.DoesNotExist:
            return JsonResponse({'message': 'Review not found'}, status=404)
    else:
        return JsonResponse({'message': 'Missing Review_id parameter'}, status=400)