from django import forms

class Add_organ(forms.Form):
        organ_system = forms.ChoiceField(choices=[])
        organ_name = forms.CharField(max_length=40)
        organ_function = forms.CharField(max_length=1200)
        
class Search_organ(forms.Form):
    organ_system = forms.ChoiceField(choices=[], required=False)
    organ_name = forms.CharField(max_length=100, required=False)    