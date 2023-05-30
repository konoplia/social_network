from blog.models import Post


def get_disliked_user_ids(obj):
    dis_liked_user = Post.objects.get(id=obj.id).dis_likes.all()
    return [user.id for user in dis_liked_user]


def get_liked_user_ids(obj):
    liked_user = Post.objects.get(id=obj.id).likes.all()
    return [user.id for user in liked_user]
