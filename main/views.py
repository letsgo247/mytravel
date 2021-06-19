from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
import random
import string

# Create your views here.
from main.models import Entity



# json load하는 함수
def load_json(path):
    with open(path, 'rt', encoding='UTF8') as json_file:
        return json.load(json_file)

data_json = load_json("./main/static/main/js/data.json")



# DB 접근
all_fields = Entity._meta.fields  # Entity의 fields name list 생성
countriesNumber = len(all_fields)   # db에 등록된 국가 수 count
# Entity.objects.filter(id=5).delete()  # record 삭제





# DB 출력 및 필요값 계산
all = Entity.objects.all()
participants = all.count()
# print('all=', all)

countriesDict = {}

for k in data_json:
    alpha3 = k['alpha3']

    rows = Entity.objects.filter(**{alpha3: True})  # https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
    count = rows.count()
    countriesDict[alpha3] = count

# print(countriesDict)
totalCount = sum(countriesDict.values())
# print(totalCount)
averageCount = round(totalCount / participants, 2)
# print(averageCount)

ratioDict = countriesDict.copy()

for i,j in countriesDict.items():
    # print(i,j)
    ratioDict[i] = round(j/totalCount*100,2)
    
sortedRatioDict = sorted(ratioDict.items(), reverse=True, key=lambda x:x[1])[0:10]
# print(sortedRatioDict)







def index(request):
    all = Entity.objects.all()
    return render(request, 'main/body.html', context={'all':all, 'averageCount':averageCount, 'sortedRatioDict': sortedRatioDict})
        
        
        
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

        countriesArray = request.POST['countriesArray']
        liArray = request.POST['liArray']
        countriesArray = countriesArray.split(",")    # string to array
        liArray = liArray.split(",")    # string to array

        # print('countriesArray:',countriesArray)
        # print('liArray:',liArray)
        


        entity = Entity()
        # print(entity)
        
        identifier = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        entity.identifier = identifier

        for country in countriesArray:  # entity 만들기
            # print(country)
            
            for k in data_json:
                alpha3 = k['alpha3']
                
                if k['name'] == country:
                    # print('일치!')
                    
                    # print('1.Before')
                    # print(alpha3, entity.__getattribute__(alpha3))
                    entity.__setattr__(alpha3, True)
                    # print('2.After')
                    # print(alpha3, entity.__getattribute__(alpha3))

        # print(entity)
        


        continents = {'Asia':0, 'Europe':0, 'Oceania':0, 'North America':0, 'South America':0, 'Africa':0, 'Antarctica':0}
        continentsCount = []
        # continentsTotal = sum(continents.values())
        # print(continentsTotal)

        visitedArea = 0
        
        for country in countriesArray:
            for obj in data_json:
                if country == obj['name']:  # 있으면
                    visitedArea += obj['area']     # 선택 면적 합계
                    continents[obj['continent']] += 1   # 대륙별 집계

        # print(continents)

        
        for value in continents.values():
            # print(value)
            # ratio = round(value/continentsTotal * 100, 2)
            continentsCount.append(value)

        # print(continentsCount)


        visitedNumber = len(countriesArray)
        numberRatio = round(visitedNumber / countriesNumber * 100, 2)   # %로 소수점 2자리까지 출력
        areaRatio = round(visitedArea / 149390550.0 * 100, 2)

        # all = Entity.objects.all()

        return render(request, 'main/result.html', context={'liArray':liArray, 'countriesArray':countriesArray, 'all':all, 'averageCount':averageCount, 'sortedRatioDict': sortedRatioDict, 'visitedNumber':visitedNumber, 'visitedArea':visitedArea, 'numberRatio':numberRatio, 'areaRatio':areaRatio, 'continentsCount':continentsCount})






def load_result(request, identifier):
    countriesArray=[]
    print(identifier)
    entity = Entity.objects.get(identifier=identifier)
    all_fields = Entity._meta.fields
    print(entity)
    # print(all_fields)
    for i in all_fields:
        alpha3 = i.name
        boolean = entity.__getattribute__(alpha3)
        if boolean == True:
            for k in data_json:
               if k['alpha3'] == alpha3:
                   countriesArray.append(k['name'])
    print(countriesArray)


    
    # countriesArray = request.POST['countriesArray']
    # liArray = request.POST['liArray']
    # countriesArray = countriesArray.split(",")    # string to array
    # liArray = liArray.split(",")    # string to array

    # # print('countriesArray:',countriesArray)
    # # print('liArray:',liArray)



    # entity = Entity()
    # # print(entity)

    # identifier = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    # entity.identifier = identifier

    # for country in countriesArray:  # entity 만들기
    #     # print(country)
        
    #     for k in data_json:
    #         alpha3 = k['alpha3']
            
    #         if k['name'] == country:
    #             # print('일치!')
                
    #             # print('1.Before')
    #             # print(alpha3, entity.__getattribute__(alpha3))
    #             entity.__setattr__(alpha3, True)
    #             # print('2.After')
    #             # print(alpha3, entity.__getattribute__(alpha3))

    # # print(entity)



    # continents = {'Asia':0, 'Europe':0, 'Oceania':0, 'North America':0, 'South America':0, 'Africa':0, 'Antarctica':0}
    # continentsCount = []
    # # continentsTotal = sum(continents.values())
    # # print(continentsTotal)

    # visitedArea = 0

    # for country in countriesArray:
    #     for obj in data_json:
    #         if country == obj['name']:  # 있으면
    #             visitedArea += obj['area']     # 선택 면적 합계
    #             continents[obj['continent']] += 1   # 대륙별 집계

    # # print(continents)


    # for value in continents.values():
    #     # print(value)
    #     # ratio = round(value/continentsTotal * 100, 2)
    #     continentsCount.append(value)

    # # print(continentsCount)


    # visitedNumber = len(countriesArray)
    # numberRatio = round(visitedNumber / countriesNumber * 100, 2)   # %로 소수점 2자리까지 출력
    # areaRatio = round(visitedArea / 149390550.0 * 100, 2)

    # # all = Entity.objects.all()

    # return render(request, 'main/result.html', context={'liArray':liArray, 'countriesArray':countriesArray, 'all':all, 'averageCount':averageCount, 'sortedRatioDict': sortedRatioDict, 'visitedNumber':visitedNumber, 'visitedArea':visitedArea, 'numberRatio':numberRatio, 'areaRatio':areaRatio, 'continentsCount':continentsCount})

    return render(request, 'main/result.html')