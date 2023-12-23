from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    tanks = 'Танки'
    healers = 'Хилеры'
    damagers = 'ДД'
    merchants = 'Торговцы'
    guildmasters = 'Гилдмастеры'
    questgivers = 'Квестгиверы'
    warsmiths = 'Кузнецы'
    tanners = 'Кожевенники'
    potionmasters = 'Зельевары'
    spellmasters = 'Мастера заклинаний'
    ANN_CATEGORIES = [
        (tanks, "Танки"),
        (healers, "Хилы"),
        (damagers, "ДД"),
        (merchants, "Торговцы"),
        (guildmasters, "Гилдмастеры"),
        (questgivers, "Квестгиверы"),
        (warsmiths, "Кузнецы"),
        (tanners, "Кожевники"),
        (potionmasters, "Зельевары"),
        (spellmasters, "Мастера заклинаний")
    ]
    author = models.ForeignKey(User,
                                  on_delete = models.CASCADE,
                                  verbose_name='Автор')
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Cодержание')
    category = models.CharField(max_length=255,
                                choices=ANN_CATEGORIES,
                                default='tanks',
                                verbose_name='Категория')
    time = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Reply(models.Model):
    author = models.ForeignKey(User,
                                  on_delete = models.CASCADE,
                                  verbose_name='Автор')
    text = models.TextField(verbose_name='Cодержание')
    post = models.ForeignKey('Post',
                             on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата создания')

    def __str__(self):
        return self.post.title, self.time