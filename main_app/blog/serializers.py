from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError

from blog.models import BlogPost, Reaction


class BlogPostSerializer(ModelSerializer):

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'content',
            'like',
            'dislike'
        ]
        read_only_fields = ['user',]

    like = SerializerMethodField()
    dislike = SerializerMethodField()

    def get_like(self, obj):
        return BlogPost.objects.get(id=obj.id).reaction.filter(like=True).count()

    def get_dislike(self, obj):
        return BlogPost.objects.get(id=obj.id).reaction.filter(dislike=True).count()

    def create(self, validated_data):
        user_id = User.objects.get(id=self.context['request'].user.id)
        validated_data['user'] = user_id
        return super().create(validated_data)


class  ReactionSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'
        read_only_fields = ['blog_post', 'user']

    def validate(self, attrs):
        like = attrs.get('like')
        dislike = attrs.get('dislike')
        if like and dislike:
            raise ValidationError('You can not like and dislike blog post at the same time')
        return super().validate(attrs)

    def update(self, instance, validated_data):
        like = validated_data.get('like')
        dislike = validated_data.get('dislike')

        if like:
            instance.like = True
            instance.like_date = datetime.now().date()
            if instance.dislike:
                instance.dislike = False
                instance.dislike_date = None
        if not like and like is not None and instance.like:
            instance.like = False
            instance.like_date = None   

        if dislike:
            instance.dislike = True
            instance.dislike_date = datetime.now().date()
            if instance.like:
                instance.like = False
                instance.like_date = None
        if not dislike and dislike is not None and instance.dislike:
            instance.dislike = False
            instance.dislike_date = None
        instance.save()
        return instance
