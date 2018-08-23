from django import forms


from .models import Data

class DataForm():

    class Meta:
        model = Data
        fields = ('forward', 'backward','direction','breaker', 'speed')