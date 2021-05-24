from django.shortcuts import render


def index(request):
    """
    This view returns the index page
    """
    return render(request, 'home/index.html')
