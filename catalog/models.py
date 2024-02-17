from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='навзвание')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE)
    price_for_1 = models.IntegerField(verbose_name='цена за штуку')
    date_of_birth = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_last_change = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    # created_at = models.TextField(null=True, blank=True, verbose_name='местро производства')

    def __str__(self):
        return f'{self.name}, {self.price_for_1}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price_for_1',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='categorys/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    slug = models.CharField(verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='preview', upload_to='blog/',  **NULLABLE)
    date_of_birth = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('view_count',)