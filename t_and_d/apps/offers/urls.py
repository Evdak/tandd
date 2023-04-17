
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path('contact', views.contact_form_view, name="contact_form"),
    path('offer/<int:offer_id>', views.offer_view, name="index"),
]
