from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from main.models import Entity


countries = []
all_fields = Entity._meta.fields  # Entity의 fields name list 생성
# print(all_fields)
for value in all_fields:
    if value.name != 'id':
        countries.append(value.name)
print('countries:',countries)

@csrf_exempt    # decorater. 아래 정의되는 함수를 둘러싸면서, 미리 정의된 기능을 수행. 여기서는 csrf 검사 면제.
def index(request):
    if request.method == 'POST' :
        post = request.POST
        print('POST:', post)
        list = request.POST.getlist('array[]')
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