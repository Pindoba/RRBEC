from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count, F
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime

import datetime



from comandas.models import ProductComanda
from orders.models import Order
from payments.models import Payments
from gestaoRaul.decorators import group_required

@group_required(groupName='Gerente')
def home(request):
    try:
        total_pagamentos = Payments.objects.aggregate(total=Sum('value'))['total']
        qdt_pagamentos = Payments.objects.aggregate(total=Count('value'))['total']
        pagamentos = Payments.objects.all()
        ticekMedio = total_pagamentos / qdt_pagamentos

        produtos_mais_vendidos = ProductComanda.objects.values('product').annotate(
        quantidade=Count('product'),
        nome=F('product__name') ).order_by('-quantidade')[:5]
        return render(request, 'home.html', {'total_pagamentos': total_pagamentos, 'pagamentos': pagamentos, 'qdt_pagamentos': qdt_pagamentos, 'produtos_mais_vendidos': produtos_mais_vendidos, 'ticekMedio': ticekMedio, })
    except:
        return render(request, 'home.html')


@group_required(groupName='Gerente')
def chartCuisine(request,dateStart,dateEnd):
    try:
        dateStart = parse_datetime(dateStart+' 07:00:00')
        dateEnd = parse_datetime(dateEnd+' 07:00:00')+ datetime.timedelta(days=1)
    except:
        dateStart = parse_datetime('2025-01-01 07:00:00')
        dateEnd = datetime.datetime.now()
    # print(request.user.groups.all())
    # print(request.user.is_authenticated)
    # fulano = User()
    tFila = []
    tPreparando = []
    tFinalizado = []

    orders = Order.objects.filter(delivered__isnull=False, queue__gt=dateStart, queue__lt=dateEnd)
    try:
        for order in orders:
            tFila.append((order.preparing - order.queue).total_seconds())
            tPreparando.append((order.finished - order.preparing).total_seconds())
            tFinalizado.append((order.delivered - order.finished).total_seconds())

        mediaFila = int((sum(tFila) / len(tFila))/60)
        mediaPreparando = int((sum(tPreparando) / len(tPreparando))/60)
        mediaFinalizado = int((sum(tFinalizado) / len(tFinalizado))/60)

        return JsonResponse({
            'mediaFila': mediaFila,
            'mediaPreparando': mediaPreparando,
            'mediaFinalizado': mediaFinalizado,
            })
    except:
        return JsonResponse({
            'mediaFila': 0,
            'mediaPreparando': 0,
            'mediaFinalizado': 0,
            })
