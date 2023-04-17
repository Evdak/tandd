from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from offers import models


def index_view(request: HttpRequest, data: dict = {}):
    print(data)
    offers = models.Offer.objects.all()
    data.update(
        {
            "offers": offers,
        }
    )

    print(data)

    return render(
        request,
        'index.html',
        data
    )


def offer_view(request: HttpRequest, offer_id: int):
    offer = models.Offer.objects.filter(id=offer_id).first()
    if offer:
        return render(
            request,
            'offer.html',
            {
                "offer": offer,
            }
        )


def contact_form_view(request: HttpRequest):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    return index_view(request, {"alert": "Ваша заявка принята"})
