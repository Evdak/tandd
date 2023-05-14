from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib import messages

from offers import models
from tgbot import models as tgbot_models
from telegram_bot import bot


def index_view(request: HttpRequest, data: dict = {}):
    offers = models.Offer.objects.all()
    reviews = models.Review.objects.order_by("-id").filter(is_active=True).all()
    data.update(
        {
            "offers": offers,
            "reviews": reviews,
        }
    )

    return render(request, "index.html", data)


def offer_view(request: HttpRequest, offer_id: int):
    offer = models.Offer.objects.filter(id=offer_id).first()
    if offer:
        return render(
            request,
            "offer.html",
            {
                "offer": offer,
            },
        )


def contact_form_view(request: HttpRequest):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    email = request.POST.get("email")

    _request = models.Request.objects.create(
        name=name,
        phone=phone,
        message=message,
        email=email,
    )
    _request.save()

    _msg = f"""🔥НОВАЯ ЗАЯВКА {_request.id}🔥\n---------\n👤Имя: {name if name else '-'}\n📞Телефон: {phone if phone else '-'}\n📧Email: {email if email else '-'}\nСообщение: {message if message else '-'}\n---------\n"""

    for user in tgbot_models.TGUser.objects.filter(is_admin=True).all():
        bot.send_message(
            user.tg_id,
            _msg,
        )

    return index_view(request, {"alert": "Ваша заявка принята"})


def add_review(request: HttpRequest):
    name = request.POST.get("name")
    text = request.POST.get("text")

    print(name, text)

    if not text:
        return HttpResponseBadRequest("Не удалось добавить отзыв")

    if not name:
        name = "Аноним"

    rev = models.Review.objects.create(
        name=name,
        text=text,
        is_active=False,
    )

    rev.save()

    messages.success(request, "Отзыв отправлен на модерацию!")
    # return redirect("index")
    return JsonResponse({"result": "Отзыв отправлен на модерацию!"})
