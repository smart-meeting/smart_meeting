from django.shortcuts import render
from .models import Schedule

# 현재 사용자에 해당하는 일정을 표시
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        user = request.user
        sche = Schedule.objects.filter(user=request.user)
        return render(request, 'main/index.html', {
            'sche':sche,
            'user':user
        })
