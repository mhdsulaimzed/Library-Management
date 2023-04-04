from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from aoi.serializer import UserSerializer,UserDetailSerializer,BookSerializer,UserBookSerializer
from rest_framework.viewsets import ModelViewSet
from aoi.models import UserDetails,Books,UserBook
from rest_framework import authentication,permissions
from rest_framework import serializers

# Create your views here.
class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
    def create(self,request,*args,**kw):
        sz=UserSerializer(data=request.data)
        if sz.is_valid():
            usr=User.objects.create_user(**sz.validated_data)
            sz=UserSerializer(usr,many=False)
            return Response(data=sz.data)
        else:
            return Response(data=sz.errors)
        
#Userdetails view is to give more information about user and it can be only added if the user is loged in /authenticated        
        
class UserDetailView(ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = UserDetails.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
  
    
    #can add or update query
    def get_queryset(self):
        return UserDetails.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        
        prof=self.get_object()
        if prof.user != request.user:
            return serializers.ValidationError("method not allowed")
        else:
            return super().destroy(request,)
        
class BookView(ModelViewSet):
    serializer_class=BookSerializer
    queryset=Books.objects.all()


class UserBookView(ModelViewSet):
    serializer_class=UserBookSerializer
    queryset=UserBook.objects.all()

    def perform_create(self, serializer):
        id=self.get(id=id)
        books=Books.objects.get(0)
        books.isactive=True
        return super().perform_create(serializer)


        
