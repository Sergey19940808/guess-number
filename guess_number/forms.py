from django import forms

__all__ = [
    'NumberForm',
]


class NumberForm(forms.Form):
    number = forms.CharField(label='number', max_length=100)

    def clean_number(self):
        number = self.cleaned_data['number']
        if (len(number) != 2) or (int(number) < 10 or int(number) > 99):
            raise forms.ValidationError('Вы ввели не двухзначное число')
        return number
