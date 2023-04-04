from rest_framework import serializers
from aoi.models import UserDetails,Books,UserBook
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

class UserDetailSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)

    class Meta:
        model=UserDetails
        fields=["user","dob","phone_number","image"]

class BookSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    isactive=serializers.CharField(read_only=True)
    class Meta:
        model=Books
        fields=["bookname","isbn","author","published_on","isactive"]


class UserBookSerializer(serializers.ModelSerializer):
    borrower=serializers.CharField(read_only=True)
    book=serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = "__all__"