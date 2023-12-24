# neostyle_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from neostyle_app.management.commands.run_telegram_bot import Command


def index(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            # send_mail(
            #     'Новая заявка',
            #     'Поступила новая заявка. Пожалуйста, проверьте панель администратора.',
            #     settings.DEFAULT_FROM_EMAIL,  # Отправитель
            #     ['moonexsoftaim@mail.ru'],  # Получатель
            #     fail_silently=False,
            # )
            # Отправка уведомления в телеграм
            Command.send_telegram_notification(
                name=form.cleaned_data.get('name', ''),
                phone=form.cleaned_data.get('phone', ''),
                email=form.cleaned_data.get('email', ''),
            )
            return JsonResponse({'message': 'Ваша заявка принята, с вами свяжутся в ближайшее время.'})

    return render(request, 'neostyle_app/index.html', {'form': form})

def architecture(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            Command.send_telegram_notification(
                name=form.cleaned_data.get('name', ''),
                phone=form.cleaned_data.get('phone', ''),
                email=form.cleaned_data.get('email', ''),
            )
            return JsonResponse({'message': 'Ваша заявка принята, с вами свяжутся в ближайшее время.'})

    return render(request, 'neostyle_app/architecture.html', {'form': form})

def comerc_interior(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            Command.send_telegram_notification(
                name=form.cleaned_data.get('name', ''),
                phone=form.cleaned_data.get('phone', ''),
                email=form.cleaned_data.get('email', ''),
            )
            return JsonResponse({'message': 'Ваша заявка принята, с вами свяжутся в ближайшее время.'})

    return render(request, 'neostyle_app/comerc-interior.html', {'form': form})


def interior_design(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            Command.send_telegram_notification(
                name=form.cleaned_data.get('name', ''),
                phone=form.cleaned_data.get('phone', ''),
                email=form.cleaned_data.get('email', ''),
            )
            return JsonResponse({'message': 'Ваша заявка принята, с вами свяжутся в ближайшее время.'})

    return render(request, 'neostyle_app/interior-design.html', {'form': form})

def portfolio(request):
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            Command.send_telegram_notification(
                name=form.cleaned_data.get('name', ''),
                phone=form.cleaned_data.get('phone', ''),
                email=form.cleaned_data.get('email', ''),
            )
            return JsonResponse({'message': 'Ваша заявка принята, с вами свяжутся в ближайшее время.'})

    return render(request, 'neostyle_app/portfolio.html', {'form': form})




def employee_dashboard(request):
    requests = Request.objects.all()
    return render(request, 'neostyle_app/employee_dashboard.html', {'requests': requests})

def change_status(request, request_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        request = Request.objects.get(id=request_id)
        request.status = new_status
        request.save()
    return redirect('employee_dashboard')

def delete_request(request, request_id):
    if request.method == 'POST':
        request_to_delete = Request.objects.get(id=request_id)
        request_to_delete.delete()

    return redirect('employee_dashboard')