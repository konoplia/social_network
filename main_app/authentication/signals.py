from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from authentication.models import User


@receiver(post_save, sender=OutstandingToken)
def last_login_record(sender, **kwargs):
    current_user = User.objects.get(id=kwargs['instance'].user_id)
    current_user.last_jwt_login = datetime.now()
    current_user.save()
