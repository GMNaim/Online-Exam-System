from rest_framework import serializers
from apps.core.account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new user """
        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            middle_name=validated_data.get('middle_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            mobile_number=validated_data.get('mobile_number'),
            gender=validated_data.get('gender'),
            is_active=validated_data.get('is_active'),
            country=validated_data.get('country'),
            address=validated_data.get('address'),
        )
        if self.context['request'].data.get('file_profile_picture') is not None:
            user.profile_picture = self.context['request'].data['file_profile_picture']
        if self.context['request'].data.get('file_signature') is not None:
            user.signature = self.context['request'].data['file_signature']
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validate_data):
        """ Update and return an existing User instance """
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.middle_name = validate_data.get('middle_name', instance.middle_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.email = validate_data.get('email', instance.email)
        instance.username = validate_data.get('username', instance.username)
        instance.mobile_number = validate_data.get('mobile_number', instance.mobile_number)
        instance.gender = validate_data.get('gender', instance.gender)
        instance.is_active = validate_data.get('is_active', instance.is_active)
        instance.country = validate_data.get('country', instance.country)
        instance.address = validate_data.get('address', instance.address)

        if 'password' in validate_data:
            instance.set_password(validate_data.get('password'))
        if self.context['request'].data.get('file_profile_picture') is not None:
            if self.context['request'].data.get('file_profile_picture') == 'null':
                instance.profile_picture = None
            else:
                instance.profile_picture = self.context['request'].data['file_profile_picture']
        if self.context['request'].data.get('file_signature') is not None:
            if self.context['request'].data.get('file_signature') == 'null':
                instance.signature = None
            else:
                instance.signature = self.context['request'].data['file_signature']
        instance.save()
        return instance

