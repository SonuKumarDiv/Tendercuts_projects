from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import secrets
import bcrypt


class signup__api(APIView):
    def get(self,request):
        f0=serializers.password()
        f1=serializers.create_user_form()

        return Response({**f1.data,**f0.data
                            },status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        f1=serializers.create_user_form(data=request.POST)
        f0=serializers.password()
        if f1.is_valid():
            
            check_list = list(models.User.objects.filter((Q(country_code=request.POST['country_code'])&Q(phone_number=request.POST['phone_number']))|
                                                                        Q(email=request.POST['email'])))
            del_acc=[]
            if check_list != []:
                for i in check_list:
                    if i.country_code==request.POST['country_code'] and i.phone_number==request.POST['phone_number']:
                        return Response({'success':'false',
                                        'error_msg':'This phone number already exists',
                                        'errors':{},
                                        'response':{},
                                        },status=status.HTTP_400_BAD_REQUEST)
                    elif i.email==request.POST['email']:
                        return Response({'success':'false',
                                        'error_msg':'This email already exists',
                                        'errors':{},
                                        'response':{},
                                        },status=status.HTTP_400_BAD_REQUEST)
                    else:
                        del_acc.append(i)
            if del_acc!=[]:
                for i in del_acc:
                    i.delete()

            try:
                uzr=models.User()
                uzr.username=request.POST['username']
                uzr.email=request.POST['email']
                uzr.country_code=request.POST['country_code']
                uzr.phone_number=request.POST['phone_number']
                uzr.user_type=request.POST['user_type']
                uzr.save()
                password=request.POST['password'].encode('utf-8')
                uzr.password=bcrypt.hashpw(password,bcrypt.gensalt())
                uzr.password=uzr.password.decode("utf-8")
                uzr.save()
                return Response({'success':'True',
                                'error_msg':'',
                                'errors':{},
                                'response':'',
                                },status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'success':'false',
                                'error_msg':"Something Bad happened",
                                'errors':{},
                                'response':{str(e)},
                                },status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success':'false',
                                'error_msg':'',
                                'errors':'',
                                'response':{},
                                },status=status.HTTP_400_BAD_REQUEST)

class get_all_user_api(APIView):
    def get(self,request):
        S_T=list(models.User.objects.all())
        return Response({'success':'true',
                    'error_msg':'',
                    'errors':{},
                    'response':{'Stores_Details':serializers.get_all_users(S_T,many=True).data},
                    },status=status.HTTP_202_ACCEPTED)# 