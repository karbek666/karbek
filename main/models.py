from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class ProductImage(models.Model):
    image =  models.ImageField('фото')

class Product(models.Model):
    name = models.CharField('Имя', max_length=20, blank=True)
    short_description = models.TextField('краткое описание', max_length=100)
    Full_description = models.TextField('полное описание', max_length=250)
    price = models.FloatField('цена', blank=True)
    quantity_in_stock = models.IntegerField('количество на складе', blank=True)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)


class Comment(models.Model):
    link_to_the_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_link = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField('Tекст комментария')
    date_of_creation = models.DateTimeField('дата создания',auto_now_add=True)

class Rating(models.Model):
    link_to_the_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_link = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    grade = models.IntegerField(validators=[MaxLengthValidator(10)])

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
