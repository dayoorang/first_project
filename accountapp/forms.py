from django.contrib.auth.forms import UserCreationForm

class AccountCreationForm(UserCreationForm):
    def __init__(self ,*args, **kwargs): # overriding 하기 위함.
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

