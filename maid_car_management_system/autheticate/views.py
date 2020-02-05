from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from django.utils.timezone import now, timedelta
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets,status

import traceback
from django.contrib.auth import authenticate, login
class RegisterViewSet(viewsets.ViewSet):
    def list(self,request):
        try:
            user=MyUser.objects.all()
            user_list=[]
            for user in user:
                user_list.append({
                    'id':user.id,
                    'name':user.name,
                    'email':user.email,
                    
                    'maid_choices':user.maid_choices
                })
            return Response({'response':user_list,'message':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
    def create(self,request):
        try:
            user=MyUser()
            user.name=request.data.get('name')
            user.email=request.data.get('email')
            user.set_password(request.data.get('password'))
            user.maid_choices=request.data.get('maid_choices')
            user.is_active = True
            user.save()
            app = Application.objects.create(user=user)
            token = generate_token()
            refresh_token = generate_token()
            expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
            scope = "read write"
            access_token = AccessToken.objects.create(user=user,
                                                application=app,
                                                expires=expires,
                                                token=token,
                                                scope=scope,
                                                )
            print("access token ------->", access_token)
            RefreshToken.objects.create(user=user,
                                        application=app,
                                        token=refresh_token,
                                        access_token=access_token
                                        )
            response = {
                'access_token': access_token.token,
                'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
                'token_type': 'Bearer',
                'refresh_token': access_token.refresh_token.token,
                'client_id': app.client_id,
                'client_secret': app.client_secret
                }
        
        
            return Response({"response":response,'status':status.HTTP_200_OK,'success':True})
        except Exception as error:
            traceback.print_exc()
            return Response({'message':str(error),'status':status.HTTP_200_OK,'success':False})
    def retrieve(self,request,pk=None):
        try:
                
            myuserdata=MyUser.objects.get(id=pk)
            myuserdatalist=[{
                'id':myuserdata.id,
                'name':myuserdata.name,
                'email':myuserdata.email,
                'maid_choices':myuserdata.maid_choices

            }]
        
            return Response({'response':myuserdatalist,'message':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})

    def update(self,request,pk=None):
        try:
                
            myuserdata=MyUser.objects.get(id=pk)
            name=request.data.get('name')
            if not name:
                return Response({'response':'please enter the name','message':True,'status':status.HTTP_200_OK})
            myuserdata.name=name
            email=request.data.get('email')
            if not email:
                return Response({'response':'please enter the email','message':True,'status':status.HTTP_200_OK})
            myuserdata.email=email
            maid_choices=request.data.get('maid_choices')
            if not maid_choices:
                return Response({'response':'please enter the maid_choices','message':True,'status':status.HTTP_200_OK})
            myuserdata.maid_choices=maid_choices
            password=request.data.get('password')
            if not password:
                return Response({'response':'please enter the password','message':True,'status':status.HTTP_200_OK})
            myuserdata.password=password
            myuserdata.save()
            # myuserdatalist=[{
            #     'id':myuserdata.id,
            #     'name':myuserdata.name,
            #     'email':myuserdata.email,
            #     'choices':myuserdata.maid_choices

            # }]
        
            return Response({'response':'your regitration profiles is updated','message':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
    def destroy(self,request,pk=None):
        try:
            myuserdata=MyUser.objects.get(id=pk).delete() 
            return Response({'response':'data deleted successfully','success':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})
class LoginViewSet(viewsets.ViewSet):
   def create(self, request): 
        try:
            email = request.data.get('email')
            print('eeeeeeeeee',email)
            password=(request.data.get('password'))
            print('password',password)
            user = authenticate(email=email, password=password)
            print('ppppppp',user)
            if user is not None:
                app = Application.objects.get(user=user)  
                token = generate_token()
                refresh_token = generate_token()
                expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
                scope = "read write"
                access_token = AccessToken.objects.create(user=user,
                                                        application=app,
                                                        expires=expires,
                                                        token=token,
                                                        scope=scope,
                                                        )
                
                RefreshToken.objects.create(user=user,
                                        application=app,
                                        token=refresh_token,
                                        access_token=access_token
                                        )
                response = {
                    'access_token': access_token.token,
                    'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
                    'token_type': 'Bearer',
                    'refresh_token': access_token.refresh_token.token,
                    'client_id': app.client_id,
                    'client_secret': app.client_secret
                }
            
                return Response({"response":response,'success':True,'status':status.HTTP_200_OK}) 
            
            else:
            
                return Response("excess denied")
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'success':False,'status':status.HTTP_200_OK})

       
# class LogoutViewSet(viewsets.ViewSet):
#     def destroy(self,request,pk=None):
#         data=MyUser.objects.get(id=pk)
#         print('ppppppppp',request.user)

#         return Response({'response':'deleted successfully'})

class Logout(viewsets.ViewSet):
    def list(self, request, pk=None):
        pass
        # # simply delete the token to force a login
        # aa=AccessToken.objects.filter(request.user)
        # return Response({'response':aa})