from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AutoCharacters, AutoBrand, AutoModels, User, TestDriveModel
from .forms import CarFilterForm, TechnicalServiceForm, TestDriveForm, UserRegisterForm, AddEntryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core import serializers


def home(request):
    cars = AutoCharacters.objects.all()
    form = CarFilterForm(request.POST)
    if form.is_valid():
        if form.cleaned_data["brand"]:
            cars = cars.filter(brand=form.cleaned_data["brand"])
        if form.cleaned_data["model"]:
            cars = cars.filter(model=form.cleaned_data["model"])
        if form.cleaned_data["min_price"]:
            cars = cars.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            cars = cars.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["min_mileage"]:
            cars = cars.filter(price__gte=form.cleaned_data["min_mileage"])
        if form.cleaned_data["max_mileage"]:
            cars = cars.filter(price__lte=form.cleaned_data["max_mileage"])
    paginator = Paginator(cars, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    if request.GET.get('brand'):
        data = {}
        qwe = AutoModels.objects.filter(brand=request.GET.get('brand'))
        for i in qwe:
            data.update({str(i): str(i.id)})
            print(data)
        return JsonResponse(data)
    page = paginator.get_page(page_num)
    context = {'form': form, 'page': page, 'cars': page.object_list}
    return render(request, 'main_app/home.html', context)


def detail(request, entry_id):
    recomendation = AutoCharacters.objects.all()[:5]
    entry = AutoCharacters.objects.get(pk=entry_id)
    return render(request, 'main_app/detail.html', {'entry': entry, 'recomendation': recomendation})


@cache_page(60 * 5)
@login_required()
def tec_servise(request):
    if request.method == 'POST':
        form = TechnicalServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TechnicalServiceForm()
    return render(request, 'main_app/technical_service.html', {'form': form})


@cache_page(60 * 5)
@login_required()
def test_drive(request, car_id):
    car = AutoCharacters.objects.get(pk=car_id)
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            per = form.save(commit=False)
            per.brand = car.brand  # изменение данных
            per.model = car.model  # изменение данных
            form.save()
            return redirect('home')
    else:
        form = TestDriveForm()

        return render(request, 'main_app/test_drive.html', {'form': form, 'car': car})


@cache_page(60 * 5)
def about_company(request):
    return render(request, 'main_app/about_company.html')


@cache_page(60 * 5)
def contacts(request):
    return render(request, 'main_app/contacts.html')


@cache_page(60 * 5)
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main_app/register.html', {'form': form})


def add_new_entry(request):
    if request.method == 'POST':
        form = AddEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddEntryForm()
        if request.GET.get('brand'):
            data = {}
            qwe = AutoModels.objects.filter(brand=request.GET.get('brand'))
            for i in qwe:
                data.update({str(i): str(i.id)})
                print(data)
            return JsonResponse(data)
    return render(request, 'main_app/add.html', {'form': form})

def all_clients(request):
    all_users = User.objects.all()
    return render(request, 'main_app/all_clients.html', {'all_users': all_users})

def test_drive_requests(request):
    all_entry = TestDriveModel.objects.all()
    a = {}
    for i in all_entry:
        a.update({str(AutoCharacters.objects.get(id=i.id)): AutoCharacters.objects.get(id=i.id).main_photo})
    return render(request, 'main_app/test_drive_requests.html', {'all_entry': all_entry, 'a': a})