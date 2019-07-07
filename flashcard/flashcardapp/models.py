from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Category(models.Model):

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
    
    name = models.CharField(
        verbose_name = 'カテゴリ名',
        max_length = 255
    )
    @property
    def card_count(self):
        cards = self.cards.all()
        return len(cards)

class Card(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'カード'
        verbose_name_plural = 'カード'
    

    name = models.CharField(
        verbose_name = '名前',
        max_length = 255
    )
    category = models.ForeignKey(
        to = Category,
        on_delete = models.CASCADE,
        related_name = 'cards'
    )
    image = models.ImageField(
        verbose_name = '画像ファイル',
        upload_to = 'card_images/',
    )
    audio = models.FileField(
        verbose_name = '音声ファイル',
        upload_to = 'card_audio/'
    )
    mistaken = models.BooleanField(
        verbose_name = '間違えた',
        default = False
    )
    
class CardMistaken(models.Model):
    def __str__(self):
        return self.card.name
    class Meta:
        verbose_name = '間違った問題'
        verbose_name_plural = '間違った問題'
    
    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE
    )
    card = models.ForeignKey(
        to = Card,
        on_delete = models.CASCADE
    )
    