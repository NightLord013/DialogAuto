from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=11, blank=True, verbose_name='Номер телефона')
    full_name = models.CharField(max_length=80, blank=True, verbose_name='ФИО')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class AutoBrand(models.Model):
    brand_name = models.CharField(max_length=30, verbose_name="Марка")

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class AutoModels(models.Model):
    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE, verbose_name='Марка')
    model_name = models.CharField(max_length=30, verbose_name="Модель")

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class AutoCharacters(models.Model):
    CHOOSE_TRANSMISSION = (
        ('автомат', 'автомат'),
        ('механика', 'механика'),
    )

    CHOOSE_DRIVE_WHEEL = (
        ('полный', 'полный'),
        ('передний', 'передний'),
        ('задний', 'задний'),
    )

    CHOOSE_BODY_TYPE = (
        ('седан', 'седан'),
        ('хетчбек', 'хетчбек'),
        ('кроссовер', 'кроссовер'),
    )

    CHOOSE_STEERING_WHEEL = (
        ('левый', 'левый'),
        ('правый', 'правый'),
    )

    CHOOSE_TYPE_OF_ENGINE = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
    )
    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE, verbose_name='Марка', related_name='mbrand')
    model = models.ForeignKey(AutoModels, on_delete=models.CASCADE, verbose_name="Модель", related_name='mmodel')
    engine = models.CharField(max_length=15, null=True, blank=True, verbose_name="Двигатель(литров)")
    power = models.IntegerField(null=True, blank=True, verbose_name="Мощность")
    transmission = models.CharField(max_length=15, choices=CHOOSE_TRANSMISSION, default='механическая',
                                    verbose_name="Трансмиссия")
    drive_wheel = models.CharField(max_length=10, choices=CHOOSE_DRIVE_WHEEL, default='передний', verbose_name="Привод")
    body_type = models.CharField(max_length=15, choices=CHOOSE_BODY_TYPE, default='седан', verbose_name="Тип кузова")
    color = models.CharField(max_length=20, verbose_name="Цвет")
    year = models.CharField(max_length=4, verbose_name="Год")
    mileage = models.IntegerField(verbose_name="Пробег")
    steering_wheel = models.CharField(max_length=8, choices=CHOOSE_STEERING_WHEEL, default='левый', verbose_name="Руль")
    engine_type = models.CharField(max_length=20, choices=CHOOSE_TYPE_OF_ENGINE, default='бензин',
                                   verbose_name='Тип двигателя')
    price = models.IntegerField(verbose_name='Цена')
    discount = models.IntegerField(verbose_name='Скидочная цена')
    main_photo = models.ImageField(verbose_name="Главное фото")
    photo_2 = models.ImageField(null=True, blank=True, verbose_name="Дополнительное фото 1")
    photo_3 = models.ImageField(null=True, blank=True, verbose_name="Дополнительное фото 2")
    photo_4 = models.ImageField(null=True, blank=True, verbose_name="Дополнительное фото 3")
    description = models.TextField(verbose_name='Описание', default='Нет описания')
    is_favorite = models.BooleanField(default=False, blank=True, verbose_name='В "Избранных"')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class TechnicalService(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    data = models.DateField(verbose_name='Предпочиемые дата записи')
    time = models.TimeField(verbose_name='Предпочитаемое время записи')
    phone_number = models.CharField(max_length=17, verbose_name="Номер телефона")
    extra_info = models.TextField(null=True, blank=True, verbose_name='Допонительная информация')

    class Meta:
        verbose_name = "Запись на ТО"
        verbose_name_plural = 'Записи на ТО'


class TestDriveModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")
    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Марка')
    model = models.ForeignKey(AutoModels, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Модель')
    photo = models.TextField(null=True, blank=True, verbose_name='Фото')
    data = models.DateField(verbose_name='Предпочиемые дата записи')
    time = models.TimeField(verbose_name='Предпочитаемое время записи')
    phone_number = models.CharField(max_length=17, verbose_name="Номер телефона")
    extra_info = models.TextField(null=True, blank=True, verbose_name='Допонительная информация')

    class Meta:
        ordering = ('data', 'time')
        verbose_name = "Запись на тест-драйв"
        verbose_name_plural = 'Записи на тест-драйв'
