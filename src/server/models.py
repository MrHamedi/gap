from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        ordering = ('name',)
        verbose_name = "نوع"
        verbose_name_plural = "انواع"

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=300, verbose_name="عنوان")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              verbose_name="مالک")
    description = models.TextField(verbose_name="توضیحات")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="نوع")
    member = models.ManyToManyField(get_user_model())

    class Meta:
        ordering = ('name',)
        verbose_name = "سرور"
        verbose_name_plural = "سرور ها"

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=300, verbose_name="عنوان")
    topic = models.CharField(max_length=300, verbose_name="موضوع")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              related_name="channel_owner", verbose_name="مالک")
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="سرور",
                               related_name="channel_server")

    class Meta:
        ordering = ("name",)
        verbose_name = "کانال"
        verbose_name_plural = "کانال ها"

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
