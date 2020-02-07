from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Topic(models.Model):
    '''单位工程名称'''
    text = models.CharField(default=timezone.now, max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = '单位工程'

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''施工日志'''
    topic = models .ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models .DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = '施工日志'
