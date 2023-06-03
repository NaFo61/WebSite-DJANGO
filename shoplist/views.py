from django.shortcuts import render

def shoplist(request):
    context = {}
    return render(request, 'shoplist.html', context=context)