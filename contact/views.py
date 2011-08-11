from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from contact.forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = form.cleaned_data['subject']
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
             initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact/contact_form.html', {'form': form})