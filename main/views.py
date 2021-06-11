from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

with open("./main/static/main/js/data.json", 'rt', encoding='UTF8') as json_file:
    dataJson = json.load(json_file)

# Create your views here.
from main.models import Entity


countries = []
all_fields = Entity._meta.fields  # Entity의 fields name list 생성
# print(all_fields)
for value in all_fields:
    if value.name != 'id':
        countries.append(value.name)
# print('countries:',countries)



def index(request):
    if request.method == 'POST' :
        post = request.POST
        print('POST:', post)
        list = request.POST.array
        print('list:',list)


        all = Entity.objects.all()
        print('Entity.objects.all()', all)

        entity = Entity()

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

        print('괜히 지랄 ㅎㅎ')

        return redirect('/')

    else:
        all = Entity.objects.all()
        return render(request, 'main/body.html', context={'all':all, 'countries':countries})



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
            for obj in dataJson:
                if country == obj['name']:  # 있으면
                    area += obj['area']     # 선택 면적 합계
                    continents[obj['continent']] += 1   # 대륙별 집계

        # print(area)
        # print(continents)


        # 비율 계산하는 함수
        continentsRatio = []
        continentsTotal = sum(continents.values())
        for (value) in continents.values():
            ratio = round(value/continentsTotal * 100, 2)
            continentsRatio.append(ratio)

        # print(continentsRatio)


        number = len(array)
        # print(number)
        ratio1 = round(number / 177 * 100, 2)   # %로 소수점 2자리까지 출력
        ratio2 = round(area / 149390550.0 * 100, 2)

        all = Entity.objects.all()

        return render(request, 'main/result.html', context={'array':array, 'array2':array2, 'all':all, 'number':number, 'ratio1':ratio1, 'ratio2':ratio2, 'continentsRatio':continentsRatio})