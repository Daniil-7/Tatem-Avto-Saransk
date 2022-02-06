from django.db import models
import cloudinary
import cloudinary.models


CONDITIONS = (
  ('Новый', 'Новый'),
  ('Б/У', 'Б/У')
)


cloudinary.config(
  cloud_name = "name cloud key",
  api_key = "api key",
  api_secret = "password key"
)


class Category(models.Model):
  id = models.AutoField(unique=True, primary_key=True)
  title_category = models.CharField(max_length=300, verbose_name='Имя категории')
  def __str__(self):
    return self.title_category



class Phone(models.Model):
  phone_form = models.CharField(max_length=12, verbose_name='Номер телефона')
  def __str__(self):
    return self.phone_form


class Product(models.Model):
  product_category_id = models.AutoField(unique=True, primary_key=True)
  category = models.ForeignKey(Category, related_name='categorys', verbose_name='Выбирите категорию', on_delete=models.CASCADE)
  phone = models.ForeignKey(Phone, related_name='phones', verbose_name='Выбирити номер телефона', on_delete=models.CASCADE)
  title = models.CharField(max_length=300, verbose_name='Название товара')
  money = models.IntegerField(verbose_name='Цена в рублях')
  condition = models.CharField(choices=CONDITIONS, max_length=200, verbose_name='Состояние:', default='Новый')
  image_product1 = cloudinary.models.CloudinaryField(verbose_name="Фото товара(обязательно):")
  image_product2 = cloudinary.models.CloudinaryField( verbose_name='Второе фото товара(необязательно):', blank=True)
  image_product3 = cloudinary.models.CloudinaryField(verbose_name='Третье фото товара(необязательно):', blank=True)
  text = models.TextField(verbose_name='Описание товара')
  date_creat = models.DateTimeField(auto_now_add=True) 
  date_update = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title
