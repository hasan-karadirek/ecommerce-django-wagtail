from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)
from .models import Product,Category
from django.contrib import admin

class ProductAdmin(ModelAdmin):
    model=Product
    menu_label='Products'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","category")
    search_fields=("name","category")
class CategoryAdmin(ModelAdmin):
    model=Category
    menu_label='Category'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("name","description")
    search_fields=("name")

modeladmin_register(ProductAdmin)
modeladmin_register(CategoryAdmin)
