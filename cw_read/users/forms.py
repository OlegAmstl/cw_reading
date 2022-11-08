from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreatingForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = (
            'username',
            'email',
        )
