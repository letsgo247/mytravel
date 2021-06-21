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
# print(all_fields)
# Entity.objects.filter(id=5).delete()  # record 삭제



# identifier url로 받아서 countriesArray load하는 함수
def identifier_to_countriesArray(identifier):
    countriesArray=[]
    # print(identifier)
    entity = Entity.objects.get(identifier=identifier)
    all_fields = Entity._meta.fields
    # print(entity)
    # print(all_fields)
    for i in all_fields:
        alpha3 = i.name
        boolean = entity.__getattribute__(alpha3)
        if boolean == True:
            for k in data_json:
               if k['alpha3'] == alpha3:
                   countriesArray.append(k['name'])
    # print(countriesArray)
    return countriesArray

# countries to list
def countriesArray_to_liArray(countriesArray):
    liArray = []

    for name in countriesArray:
        for k in data_json:
            if k['name'] == name:
                line = f"<img src='{k['url']}' alt='{name}'> {k['nameKr']}"
                # print(line)
                liArray.append(line)

    return liArray

def all_to_countArray(all):
    countArray = []
    for entity in all:
        count = 0
        for field in all_fields:
            if entity.__getattribute__(field.name) == True:
                count += 1
        countArray.append(count)

    countArray.sort(reverse=True)     
    return countArray


def count_rank(identifier,all):
    countArray = all_to_countArray(all)
    participants = all.count()

    me = Entity.objects.get(identifier=identifier)
    meCount = 0
    for field in all_fields:
        if me.__getattribute__(field.name) == True:
                meCount += 1

    index = countArray.index(meCount)

    rank = round((index+1) / participants *100, 2)
    return rank




# DB 출력 및 base 필요값 계산
def base_contexts():
    all = Entity.objects.all()
    participants = all.count()

    countriesDict = {}

    for k in data_json:
        alpha3 = k['alpha3']

        rows = Entity.objects.filter(**{alpha3: True})  # https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
        count = rows.count()
        countriesDict[alpha3] = count

    # print(countriesDict)
    totalCount = sum(countriesDict.values())
    averageCount = round(totalCount / participants, 2)

    ratioDict = countriesDict.copy()

    for i,j in countriesDict.items():
        ratioDict[i] = round(j/totalCount*100,2)
        
    sortedRatioDict = sorted(ratioDict.items(), reverse=True, key=lambda x:x[1])[0:10]
    return all, averageCount, sortedRatioDict


# countriesArray 로부터 각종 contexts 생성
def countriesArray_to_contexts(countriesArray):
    visitedArea = 0

    continentsCountDict = {'Asia':0, 'Europe':0, 'Oceania':0, 'North America':0, 'South America':0, 'Africa':0, 'Antarctica':0}
    continentsCountArray = []
    
    for country in countriesArray:
        for obj in data_json:
            if obj['name'] == country:  # 있으면
                visitedArea += obj['area']     # 선택 면적 합계
                continentsCountDict[obj['continent']] += 1   # 대륙별 집계

    for value in continentsCountDict.values():
            continentsCountArray.append(value)  # chart 용 array 생성

    visitedNumber = len(countriesArray)
    numberRatio = round(visitedNumber / countriesNumber * 100, 2)   # %로 소수점 2자리까지 출력
    areaRatio = round(visitedArea / 149390550.0 * 100, 2)

    return visitedNumber, visitedArea, numberRatio, areaRatio, continentsCountArray

# entity 생성 (w/o save)
def make_entity(countriesArray, identifier):
    entity = Entity()
    
    entity.identifier = identifier
    print(entity.identifier)

    for country in countriesArray:  # entity 만들기
        # print(country)
        for k in data_json:
            if k['name'] == country:    # 찾아서
                alpha3 = k['alpha3']
                # print(alpha3, entity.__getattribute__(alpha3))
                entity.__setattr__(alpha3, True)    # field value 변경
                # print(alpha3, entity.__getattribute__(alpha3))

    return entity





def index(request):
    # all, averageCount, sortedRatioDict = base_contexts()

    return render(request, 'main/body.html')






def result(request):
    if request.method == 'POST' :
        countriesArray = request.POST['countriesArray']
        countriesArray = countriesArray.split(",")    # string to array

        identifier = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        
        entity = make_entity(countriesArray, identifier)
        entity.save()
        
        return redirect(f"/result/{identifier}")





def load_result(request, identifier):
    all, averageCount, sortedRatioDict = base_contexts()

    countriesArray = identifier_to_countriesArray(identifier)

    liArray = countriesArray_to_liArray(countriesArray)

    visitedNumber, visitedArea, numberRatio, areaRatio, continentsCountArray = countriesArray_to_contexts(countriesArray)

    rank = count_rank(identifier, all)


    

    return render(request, 'main/result.html', context={
            # to result
            'liArray':liArray, 
            'countriesArray':countriesArray, 
            'visitedNumber':visitedNumber, 
            'visitedArea':visitedArea, 
            'numberRatio':numberRatio, 
            'areaRatio':areaRatio, 
            'continentsCountArray':continentsCountArray,
            'identifier':identifier,
            'rank': rank,
            
            # to base
            'all':all, 
            'averageCount':averageCount, 
            'sortedRatioDict': sortedRatioDict,
            })