from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):


    def __init__(self, request):
        """
        Initialisation of the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #saving in session the empty cart
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
