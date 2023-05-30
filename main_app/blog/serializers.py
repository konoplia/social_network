from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from blog.models import Post
from blog.helpers import get_disliked_user_ids, get_liked_user_ids


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user',]

    likes = SerializerMethodField()
    dis_likes = SerializerMethodField()
    is_liked = SerializerMethodField(read_only=True)
    is_dis_liked = SerializerMethodField(read_only=True)

    def create(self, validated_data):
        user_id = User.objects.get(id=self.context['request'].user.id)
        validated_data['user'] = user_id
        return super().create(validated_data)

    def get_likes(self, obj):
        return Post.objects.get(id=obj.id).likes.count()

    def get_dis_likes(self, obj):
        return Post.objects.get(id=obj.id).dis_likes.count()

    def get_is_liked(self, obj):
        return True if self.context['request'].user.id in get_liked_user_ids(obj) else False

    def get_is_dis_liked(self, obj):
        return True if self.context['request'].user.id in get_disliked_user_ids(obj) else False


class RetrieveUpdateDestroyPostSerializer(PostSerializer):
    pass


class  PostLikeSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['like']

    like = SerializerMethodField()

    def get_like(self, obj):
        dis_liked_user_ids = get_disliked_user_ids(obj)
        liked_user_ids = get_liked_user_ids(obj)
        user_id = self.context['request'].user.id
        like = self.context['request'].data.get('like')
        if like and user_id not in liked_user_ids:
            obj.likes.add(User.objects.get(id=user_id))
            if user_id in dis_liked_user_ids:
                obj.dis_likes.remove(User.objects.get(id=user_id))
        elif like is not None:
            obj.likes.remove(User.objects.get(id=user_id))


class  PostDisLikeSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['dis_like']

    dis_like = SerializerMethodField()

    def get_dis_like(self, obj):
        dis_liked_user_ids = get_disliked_user_ids(obj)
        liked_user_ids = get_liked_user_ids(obj)
        user_id = self.context['request'].user.id
        dis_like = self.context['request'].data.get('dis_like')
        if dis_like and user_id not in dis_liked_user_ids:
            obj.dis_likes.add(User.objects.get(id=user_id))
            if user_id in liked_user_ids:
                obj.likes.remove(User.objects.get(id=user_id))
        elif dis_like is not None:
            obj.dis_likes.remove(User.objects.get(id=user_id))
