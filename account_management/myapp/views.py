from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .forms import CoordinateForm
from .cooldown import calculate_distance_and_wait_time
from .models import User

# Create your views here.
def account_management(request):
    users = User.objects.all()
    return render(request, 'myapp/account_management.html', {'users': users})

def tools(request):
    result = None
    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            lon1 = form.cleaned_data['lon1']
            lat1 = form.cleaned_data['lat1']
            lon2 = form.cleaned_data['lon2']
            lat2 = form.cleaned_data['lat2']
            
            distance, wait_time = calculate_distance_and_wait_time(lon1, lat1, lon2, lat2)
            result = f"距離: {distance:.2f} km\n待機時間: {wait_time}"
    else:
        form = CoordinateForm()
    
    return render(request, 'myapp/tools.html', {'form': form, 'result': result})