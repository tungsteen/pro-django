from django import forms


class AgeField(forms.fields.IntegerField):
    default_error_messages = {
        'out_of_range': u'Age cannot be negative.',
    }

    def clean(self, value):
        value = super(AgeField, self).clean(value)
        if value < 0:
            msg = self.error_messages['out_of_range']
            raise forms.utils.ValidationError(msg)
        return value


class TitleForm(forms.Form):
    type_some_chars = forms.CharField(required=False)
    custom = AgeField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
