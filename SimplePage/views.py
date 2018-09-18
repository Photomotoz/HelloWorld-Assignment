from django.shortcuts import render
from .forms import RegisterForm
from .models import Member


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return confirmation(request)
    else:
        form = RegisterForm()

    return render(request, 'SimplePage/registration.html', {'form': form})


def confirmation(request):
    return render(request, 'SimplePage/confirmation.html')


def report(request):
    return render(request, 'SimplePage/report.html', {'users': Member.objects.all().order_by('created_at')})


def handle_404(request):
    return render(request, 'SimplePage/404.html', status=404)


def handle_500(request):
    return render(request, 'SimplePage/500.html', status=500)
