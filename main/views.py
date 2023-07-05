from django.shortcuts import render
from .forms import SubscribeForm
from .models import Subscriber
def coming_soon(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber = Subscriber.objects.create(email=email)
            subscriber.save()
            return render(request, 'main/thank_you.html')
    return render(request, 'main/coming_soon.html', {'form': form})