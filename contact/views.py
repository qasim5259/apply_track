from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        # Pre-fill name and email if user is logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.username,
                'email': request.user.email
            }
        form = ContactForm(initial=initial_data)

    return render(request, 'contact/contact.html', {'form': form})
