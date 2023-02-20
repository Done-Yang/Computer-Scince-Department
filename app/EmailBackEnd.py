from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwangs):
        UserModle = get_user_model()
        try:
            user = UserModle.objects.get(username=username)
        except UserModle.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None