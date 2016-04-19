from django.shortcuts import get_object_or_404, render

from .models import Class, Attendance

# ...
def index(request):
    return render(request, 'myapp/index.html')