from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

with open("./staticfiles/main/js/emoji.json", 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)

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
        # post = request.POST
        # print('POST:', post)
        array = request.POST['array']
        array2 = request.POST['array2']
        print('array:',array)
        print('array2:',array2)
        array = array.split(",")    # string to array
        array2 = array2.split(",")    # string to array

        for (i,k) in enumerate(array2):
            print(type(k))
            array[i] = k

        print('array:',array)
        print('array2:',array2)

        number = len(array)
        print(number)
        ratio1 = number / 200 * 100

        
        all = Entity.objects.all()

        return render(request, 'main/result.html', context={'array':array, 'array2':array2, 'all':all, 'number':number, 'ratio1':ratio1})