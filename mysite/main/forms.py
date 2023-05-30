from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=500)
    check = forms.BooleanField(required=False)

class CreateNewPost(forms.Form):
    textfield = forms.CharField(label="textfield", widget=forms.Textarea(attrs={'rows': 5, 'cols': 90, "style": "resize: none"}))


 