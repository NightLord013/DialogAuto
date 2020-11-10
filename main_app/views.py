from django.shortcuts import render, redirect
from .models import AutoCharacters, AutoBrand, AutoModels
from .forms import CarFilterForm, TechnicalServiceForm, TestDriveForm, UserRegisterForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    cars = AutoCharacters.objects.all()
    form = CarFilterForm(request.GET)
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
    page = paginator.get_page(page_num)
    context = {'form': form, 'page': page, 'cars': page.object_list}
    return render(request, 'main_app/home.html', context)

def detail(request, entry_id):
    recomendation = AutoCharacters.objects.all()[:5]
    entry = AutoCharacters.objects.get(pk=entry_id)
    return render(request, 'main_app/detail.html', {'entry': entry, 'recomendation': recomendation})

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

@login_required()
def test_drive(request, car_id):
    car = AutoCharacters.objects.get(pk=car_id)
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            per = form.save(commit=False)
            per.brand = car.brand # изменение данных
            per.model = car.model # изменение данных
            form.save()
            return redirect('home')
    else:
        form = TestDriveForm()

        return render(request, 'main_app/test_drive.html', {'form': form, 'car': car})

def about_company(request):
    return render(request, 'main_app/about_company.html')

def contacts(request):
    return render(request, 'main_app/contacts.html')

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

