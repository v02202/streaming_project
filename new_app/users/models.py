from django.contrib.auth.models import User

def get_user_obj(user_id):
    user_obj = User.objects.get(pk=user_id)
    return user_obj