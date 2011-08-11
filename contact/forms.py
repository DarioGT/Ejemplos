from django import forms

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
        
    subject = forms.CharField(max_length=100, min_length=5)
    email = forms.EmailField(required=True, label='e-mail')
    message = forms.CharField(widget=forms.Textarea,required=False)
    cc_myself = forms.BooleanField(required=False)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message    
    
    
from django.forms.formsets import formset_factory 
ContactFormSet = formset_factory(ContactForm, extra =2)

