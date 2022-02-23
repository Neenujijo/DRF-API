from rest_framework import serializers

from .models import emplyee_usereg



class UserRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    # confirm_password=serializers.CharField(max_length=200)
    dob = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    gender = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=30)
    phone_no = serializers.IntegerField()
    

    def create(self, validated_data):
        user = emplyee_usereg.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            phone_no=validated_data['phone_no'],
            password=validated_data['password']
        )

        
        user.save()

        return user
    class Meta:
        model=emplyee_usereg
        fields='__all__'


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200)

    class Meta:
        model=emplyee_usereg
        fields=('username', 'password')

    
