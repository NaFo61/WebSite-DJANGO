from django.shortcuts import render
from .models import Developers
from datetime import datetime as dt


def first_page(request):
    context = {
        'date': dt.now().date(),
        # 'developers': Developers.objects.filter(id__in=[1])
        'developers': Developers.objects.order_by('birthday')
    }
    return render(request, 'first_page.html', context=context)
