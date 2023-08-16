import uuid

from django.apps import AppConfig
from yookassa import Payment


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'


payment = Payment.create({
    "amount": {
        "value": "2.00",
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.example.com/return_url"
    },
    "description": "Заказ №72"
}, str(uuid.uuid4()))

# get confirmation url
confirmation_url = payment.confirmation.confirmation_url
