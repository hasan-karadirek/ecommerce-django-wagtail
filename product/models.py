from django.db import models
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel,StreamFieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page,ParentalKey,Orderable
from modelcluster.models import ClusterableModel
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=1000,null=True,blank=True)
    parent_category=models.ForeignKey("product.category", verbose_name=("Parent Category"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Product(ClusterableModel):
    name=models.CharField( max_length=120, null=False,blank=False)
    description=models.TextField(max_length=1000,null=True,blank=True)
    old_price=models.IntegerField(null=False,blank=False,default=0)
    current_price=models.IntegerField(null=False,blank=False,default=0)
    category=models.ForeignKey("product.category", verbose_name=("category"), on_delete=models.CASCADE)
    product_code=models.CharField(max_length=50,null=True,blank=True)
    image=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    panels=[
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("old_price"),
        FieldPanel("current_price"),
        FieldPanel("product_code"),
        FieldPanel("category"),
        ImageChooserPanel("image"),
        InlinePanel("product_images")
    ]
    def __str__(self):
        return self.name
class ProductImages(Orderable):
    image=models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    page=ParentalKey("product.Product",related_name="product_images")
    panels=[
        ImageChooserPanel("image")
    ]
