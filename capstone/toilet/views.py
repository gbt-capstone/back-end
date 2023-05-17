import requests
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Toilet

# Create your views here.
# def main(request):
#     toilet = Toilet.objects.get(pk=1)

#     return render(request, 'index.html', {'toilet': toilet})
def fetch_and_save_toilet_data(request):
    # api에서 화장실 데이터 가져옴
    response = requests.get('https://api.odcloud.kr/api/15060017/v1/uddi:9be26c73-d883-42cf-ab36-d1a4de6cb092?page=1&perPage=50&serviceKey=%2Fr4EMvr%2B1K44b3jdeB%2F78h%2Bw5bgCuRfDyrtyezEInpi5irEh42HBoZOPmgEPx89imCkox5yNu0FLDA292aC2gA%3D%3D')
    toilets = response.json()

    print(toilets)

    return HttpResponse(toilets)
    # toilet 모델에 데이터 저장
    # for toilet in toilets:
    #     model = Toilet()
    #     model.