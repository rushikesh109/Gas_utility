from django.shortcuts import render

def request_list(request):
    return render(request, 'request_list.html')

def request_detail(request):
    return render(request, 'request_detail.html')
