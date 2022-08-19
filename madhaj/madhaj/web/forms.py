from django.forms import ModelForm, TextInput, NumberInput

from .models import Counseling
# Create your forms here.

class CounselingForm(ModelForm):
    class Meta:
        model = Counseling
        fields = ['name', 'number']
        widgets = {
            'name': TextInput(attrs={
                'class': "login__input",
                'style': 'width: 100%;background: var(--container-color);color: var(--text-color);font-size: var(--normal-font-size);padding: .25rem .5rem .5rem 0;'
            }),
            'number': NumberInput(attrs={
                'class': "login__input",
                'style': 'width: 100%;background: var(--container-color);color: var(--text-color);font-size: var(--normal-font-size);padding: .25rem .5rem .5rem 0;'
            }),
        }       