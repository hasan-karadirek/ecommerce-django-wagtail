from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel
from customer.models import Customer
from product.models import Product
from wagtail.core.models import ParentalKey,Orderable,Page
from modelcluster.models import ClusterableModel

class CustomFieldPanel(FieldPanel):
    
    def render_as_field(self):
        return ""
class Order(ClusterableModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    cart_total=models.IntegerField(default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    panels=[
        FieldPanel("date_ordered"),
        FieldPanel("transaction_id"),
        FieldPanel("customer"),
        FieldPanel("complete"),
        FieldPanel("cart_total"),
        InlinePanel("order_items"),
        
    ]
    def __str__(self):
        return str(self.id)
    def cart_total(self):
        self.cart_total=self.get_cart_total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
class OrderItem(Orderable):
    page=ParentalKey("order.Order", related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    item_total=models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    panels=[
        FieldPanel("product"),
        FieldPanel("quantity"),
        FieldPanel("item_total"),
    ]
    def item_total_amount(self):
        self.item_total_amount=self.get_total
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
class CheckoutPage(Page):
    templates="checkout/checkout.html"
    intro=models.CharField(max_length=50)
class CartPage(Page):
    templates="order/cart.html"
    intro=models.CharField(max_length=50)