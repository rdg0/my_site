from django.db import models


class Category(models.Model):
    """Категории"""

    title = models.CharField(
        'Название категории',
        max_length=100
    )
    slug = models.SlugField()

    class Meta:
        ordering = ['title']
        verbose_name = 'Катергория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Посты"""

    title = models.CharField('Заголовок поста', max_length=200)
    title_eng = models.CharField('Title post on eng', max_length=200)
    text = models.TextField(
        'Текст поста',
        help_text='Введите текст поста'
    )
    text_eng = models.TextField(
        'Text post on eng',
        help_text='Enter the text'
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Выберите группу'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
    
    def get_preview(self):
        return self.text[:150]


class Comment(models.Model):
    """Комментарии"""
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField('Почта')
    text = models.TextField('Комментарий')
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True
    )

    def __str__(self):
        return self.name
