from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel,StreamFieldPanel,PageChooserPanel

from wagtail.core.models import Page
from product.models import Product


class HomePage(Page):
    templates="home/index.html"
    intro=models.CharField(max_length=50)
    products=Product.objects.all()
    content_panels=Page.content_panels+[
    FieldPanel("intro"),
     
    ]