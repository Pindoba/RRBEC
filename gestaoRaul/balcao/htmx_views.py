from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay


def listProduct(request, comanda_id):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products,'comanda_id':comanda_id})

def addProduct(request, product_id, comanda_id):
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total})


def removeProductComanda(request, productComanda_id):
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    consumo = ProductComanda.objects.filter(comanda=product_comanda.comanda)
    product_comanda.delete()
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total})


def paymentComanda(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    comanda = Comanda.objects.get(name='VENDA BALCÃO')
    total = 0
    for produto in consumo:
        total += produto.product.price
        removeProductComanda(request, produto.id)
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description='VENDA BALÃO')
    pagamento.save()
    comanda.save()
    return redirect('comandas')

