from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from . import models
from accounts import models as ac_models


class Add_stores_forms(serializers.ModelSerializer):
    class Meta():
        model=models.store_detail
        fields=('__all__')
        depth=1

class orders_forms(serializers.ModelSerializer):
    class Meta():
        model=models.order_detail
        fields=('order_name','item_price','total_amount','order_status','address','Order_booked_by','stores')
        #depth=1
        #exclude=('Order_booked_by','stores')      
# class update_orderd_forms(serializers.ModelSerializer):
#     class Meta():
#         model=models.order_detail
#         fields=('__all__')

class update_orderd_forms(serializers.ModelSerializer):
    class Meta():
        model=models.order_detail
        fields=('id','order_name','item_price','quantity','total_amount','order_status','address','Order_booked_by','stores')
        depth=1