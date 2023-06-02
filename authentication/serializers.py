from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ValidationError

import django.contrib.auth.password_validation as validators

User = get_user_model()


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id','username',
            'password',  'email',
        ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            }

        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

    def validate(self, data):
        password = data.get('password')
        errors = dict() 
        try:
            validators.validate_password(password=password, user=User)
        except ValidationError as error:
            errors['password'] = list(error.messages)

        if errors:
            raise ValidationError(errors)

        return super(CustomUserSerializer, self).validate(data)
