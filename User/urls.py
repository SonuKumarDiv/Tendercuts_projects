from django.urls import path, re_path
from . import views
app_name='User'

urlpatterns = [
    path('User/add_orders_api',views.add_orders_api.as_view(),name='add_orders_api'),
    path('User/Update_order_api-<id>',views.Update_order_api.as_view(),name='Update_order_api'),
    path('User/add_stores_api',views.add_stores_api.as_view(),name='add_stores_api'),
    path('User/pul_all_order_of_a_store',views.pul_all_order_of_a_store.as_view(),name='pull_all_order_of_a_store'),
    path('User/pull_all_order_of_a_user',views.pull_all_order_of_a_user.as_view(),name='pull_all_order_of_a_user'),
    path('User/status_change_api-<id>',views.status_change_api.as_view(),name='status_change_api')
   
]

