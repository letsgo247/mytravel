from django.shortcuts import render, redirect

# Create your views here.
from main.models import Entity


countries = []
all_fields = Entity._meta.fields  # Entity의 fields name list 생성
# print(all_fields)
for value in all_fields:
    if value.name != 'id':
        countries.append(value.name)
print('countries:',countries)


def index(request):
    if request.method == 'POST' :
        post = request.POST
        print('POST:', post)



        all = Entity.objects.all()
        print('Entity.objects.all()', all)

        entity = Entity()

        print('1.Before')
        for i in countries:     # 일단 default 상태 확인
            print(i, entity.__getattribute__(i))

        for i in post:
            try:
                entity.__setattr__(i,True)
            except:
                pass

        print('2.After')
        for i in countries:     # 일단 default 상태 확인
            print(i, entity.__getattribute__(i))

        # entity.save()

        return redirect('/')

    else:
        all = Entity.objects.all()
        return render(request, 'main/body.html', context={'all':all, 'countries':countries})