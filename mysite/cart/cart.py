from decimal import Decimal
from django.conf import settings
from store.models import Service


class Cart:
    def __init__(self, request):
        '''инициализация корзины'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, service, quantity=1, override_quantity=False):
        '''добавить товар в корзину либо обновить его колв-во'''
        service_id = str(service.id)
        if service_id not in self.cart:
            self.cart[service_id] = {'quantity': 0, 'price': str(service.price)}

        if override_quantity:
            self.cart[service_id]['quantity'] = quantity
        else:
            self.cart[service_id]['quantity'] += quantity
        self.save()

    def save(self):
        # пометить сеант как "изменённый", чтобы обеспечить его сохранение
        self.session.modified = True

    def remove(self, service):
        '''удаление товара из корзины'''
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]
            self.save()

    def __iter__(self):
        '''Прокрутить товарные позиции корзины в цикле и получить товары из базы данных'''
        service_ids = self.cart.keys()
        # получить объекты услуги и добавить их в корзину
        services = Service.objects.filter(id__in=service_ids)
        cart = self.cart.copy()
        for service in services:
            cart[str(service.id)]['service'] = service
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''подсчитать все товарные позиции в корзине'''
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        '''очистка корзины'''
        del self.session[settings.CART_SESSION_ID]
        self.save()
