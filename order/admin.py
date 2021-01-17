from wagtail.contrib.modeladmin.options import(

    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup, 
)
from .models import Order
from django.contrib import admin
from wagtail.contrib.modeladmin.helpers import PermissionHelper
class ValidationPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True  
    def user_can_create(self, user):
        return False
    def user_can_edit_obj(self, user, obj):
        return False
    def user_can_delete_obj(self, user, obj):
        return False

class OrderAdmin(ModelAdmin):
    model=Order
    menu_label='Orders'
    menu_icon="placeholder"
    menu_order=1
    add_to_settings_menu=False
    exclude_from_explorer=False
    list_display=("transaction_id","customer")
    search_fields=("customer")
    permission_helper_class = ValidationPermissionHelper
    inspect_view_enabled = True

modeladmin_register(OrderAdmin)

# Register your models here.
