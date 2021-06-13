from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from main.models import Entity



# json load하는 함수
def load_json(path):
    with open(path, 'rt', encoding='UTF8') as json_file:
        return json.load(json_file)

data_json = load_json("./main/static/main/js/data.json")



# DB 접근
all_fields = Entity._meta.fields  # Entity의 fields name list 생성
CountriesNumber = len(all_fields)   # db에 등록된 국가 수 count
# Entity.objects.filter(id=5).delete()  # record 삭제




def index(request):
    all = Entity.objects.all()
    return render(request, 'main/body.html', context={'all':all})
        
        
        
    # if request.method == 'POST' :
    # post = request.POST
    # print('POST:', post)
    # list = request.POST.array
    # print('list:',list)


    # all = Entity.objects.all()
    # print('Entity.objects.all()', all)

    # entity = Entity()

    # print('1.Before')
    # for i in countries:     # 일단 default 상태 확인
    #     print(i, entity.__getattribute__(i))

    # for i in post:
    #     try:
    #         entity.__setattr__(i,True)
    #     except:
    #         pass

    # print('2.After')
    # for i in countries:     # 일단 default 상태 확인
    #     print(i, entity.__getattribute__(i))

    # entity.save()

    # print('괜히 지랄 ㅎㅎ')

    # return redirect('/')
        



def result(request):
    if request.method == 'POST' :
        continents = {'Asia':0, 'Europe':0, 'Oceania':0, 'North America':0, 'South America':0, 'Africa':0, 'Antarctica':0}

        array = request.POST['array']
        array2 = request.POST['array2']
        # print('array:',array)
        # print('array2:',array2)
        array = array.split(",")    # string to array
        array2 = array2.split(",")    # string to array

        # for (i,k) in enumerate(array2):
        #     print(type(k))
        #     array[i] = k

        # print(dataJson)
        print('array:',array)
        print('array2:',array2)

        area = 0
        
        # for obj in dataJson:
        #     try:
        #         print(obj['area'])
        #         area += obj['area']
        #     except:
        #         pass

        for country in array:
            for obj in data_json:
                if country == obj['name']:  # 있으면
                    area += obj['area']     # 선택 면적 합계
                    continents[obj['continent']] += 1   # 대륙별 집계

        # print(area)
        # print(continents)


        # 비율 계산하는 함수
        continentsCount = []
        # continentsTotal = sum(continents.values())
        # print(continentsTotal)
        for value in continents.values():
            # ratio = round(value/continentsTotal * 100, 2)
            continentsCount.append(value)

        # print(continentsCount)


        number = len(array)
        # print(number)
        ratio1 = round(number / CountriesNumber * 100, 2)   # %로 소수점 2자리까지 출력
        ratio2 = round(area / 149390550.0 * 100, 2)

        all = Entity.objects.all()

        return render(request, 'main/result.html', context={'array':array, 'array2':array2, 'all':all, 'number':number, 'area':area, 'ratio1':ratio1, 'ratio2':ratio2, 'continentsCount':continentsCount})