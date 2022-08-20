
from django.db import models
from accounts import models as ac_models


class store_detail(models.Model):
    store_owner=models.ForeignKey(ac_models.User,blank=True,on_delete=models.SET_NULL,null=True,related_name='owner')
    store_name=models.TextField(max_length=60,default='')
    store_address=models.CharField(max_length=60)
    def __str__(self):
	    return 'ID='+str(self.id)+'user='+str(self.store_name)

class order_detail(models.Model):
    Order_booked_by=models.ForeignKey(ac_models.User,blank=True,on_delete=models.SET_NULL,null=True,related_name='Order_booked_by')
    stores=models.ForeignKey(store_detail,blank=True,on_delete=models.SET_NULL,null=True,related_name='stores')
    order_name=models.TextField(max_length=60,default='')
    quantity=models.TextField(max_length=60,default='')
    item_price=models.IntegerField(default=0)
    total_amount =models.TextField(max_length=60,default='') # here i taken char fiels but in this field the data store in integer field so for this we 'll use int type conversion in future 
    order_status=models.CharField(max_length=30,default='')
    address=models.TextField(max_length=100,default='')