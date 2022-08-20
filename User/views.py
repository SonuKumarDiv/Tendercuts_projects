
from . import models 
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class add_orders_api(APIView):
    def get(self,request):
        S_T=list(models.order_detail.objects.all())
        return Response({'success':'true',
                    'error_msg':'',
                    'errors':{},
                    'response':{'Oreder_details':serializers.update_orderd_forms(S_T,many=True).data},
                    },status=status.HTTP_202_ACCEPTED)

    def post(self,request):
        f1=serializers.orders_forms(data=request.POST)
        if f1.is_valid():
            f1.save()
            return Response({'success':'true',
                                'error_msg':'',
                                'errors':{},
                                'response':{},
                                },status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'success':'false',
                                    'error_msg':'',
                                    'errors':'',
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST)    

class Update_order_api(APIView):
    def get(self,request,id):
        try:
            S_T=list(models.order_detail.objects.filter(id=id))
            if S_T==[]:
                return Response({'success':'false',
                                    'error_msg':'Id does not exist',
                                    'errors':{},
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST)
            S_T=S_T[0]
            return Response({'success':'true',
                        'error_msg':'',
                        'errors':{},
                        'response':{'Orders_Details':serializers.update_orderd_forms(S_T).data},
                        },status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({'require':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        try:
            ORD=list(models.order_detail.objects.filter(id=id))
        
            if ORD==[]:
                return Response({'success':'false',
                                    'error_msg':'Id does not exist',
                                    'errors':{},
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST)
            ORD=ORD[0]
            f1=serializers.orders_forms(data=request.POST,instance=ORD)
            if f1.is_valid():   
                f1.save()
                return Response({'success':'true',
                            'error_msg':'',
                            'errors':{},
                            'response':{'Updated_Orders_Details':serializers.update_orderd_forms(ORD).data},
                            },status=status.HTTP_202_ACCEPTED)#
            else:
                return Response({'success':'false',
                                    'error_msg':'',
                                    'errors':{},
                                    'response':{**dict(f1.errors),
                                    }},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'require':str(e)},status=status.HTTP_400_BAD_REQUEST)

class add_stores_api(APIView):
    def get(self,request):
        S_T=list(models.store_detail.objects.all())
        return Response({'success':'true',
                    'error_msg':'',
                    'errors':{},
                    'response':{'Stores_Details':serializers.Add_stores_forms(S_T,many=True).data},
                    },status=status.HTTP_202_ACCEPTED)# 

    def post(self,request):
        f1=serializers.Add_stores_forms(data=request.POST)
        if f1.is_valid():
            f1.save()
            return Response({'success':'true',
                                'error_msg':'',
                                'errors':{},
                                'response':{},
                                },status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'success':'false',
                                    'error_msg':'get worng input',
                                    'errors':'',
                                    'response':{},
                                    },status=status.HTTP_400_BAD_REQUEST) 

class status_change_api(APIView):
    
    def get(self,request,id):
        ord=list(models.order_detail.objects.filter(id=id))
        if ord==[]:
            return Response({'success':'false',
                                'error_msg':'invalid id',
                                'errors':{},
                                'response':{},
                                },status=status.HTTP_400_BAD_REQUEST)
        ord=ord[0]
        ord.order_status=request.POST['order_status']
        ord.save()
        return Response({'success':'true',
                    'error_msg':'',
                    'errors':{},
                    'response':serializers.update_orderd_forms(ord).data,
                    },status=status.HTTP_202_ACCEPTED)#

class pull_all_order_of_a_user(APIView):
    def post(self, request):
        try:
            user=list(models.order_detail.objects.filter(Order_booked_by=request.POST['User_id']))
            if user==[]:
                return Response({'success':'false',
                        'error_msg':"User does not exist",
                        'errors':{},
                        'response':{}
                        },status=status.HTTP_400_BAD_REQUEST) 
            
            return Response({'success':'true',
                        'error_msg':'',
                        'errors':{},
                        'response':{'result':serializers.update_orderd_forms(user, many=True).data},
                        },status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'require':str(e)},status=status.HTTP_400_BAD_REQUEST)

class pul_all_order_of_a_store(APIView):
    def post(self, request):
        try:
            use_r=list(models.order_detail.objects.filter(stores=request.POST['Store_data_id']))
            print(use_r)
            if use_r==[]:
                return Response({'success':'false',
                        'error_msg':"Store_data_id not exist",
                        'errors':{},
                        'response':{}
                        },status=status.HTTP_400_BAD_REQUEST) 
            #use_r=use_r[0]
            return Response({'success':'true',
                        'error_msg':'',
                        'errors':{},
                        'response':{'result':serializers.update_orderd_forms(use_r, many=True).data},
                        },status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'require':str(e)},status=status.HTTP_400_BAD_REQUEST)        










    

            