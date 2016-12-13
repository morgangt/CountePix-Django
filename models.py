from datetime import datetime
from datetime import timedelta
from django.db import models, transaction
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum


__all__ = ['Counter']



class Counter(models.Model):
    """ Модель счетчика по датам """
    content_type = models.ForeignKey(ContentType, verbose_name='Приложение')
    object_id = models.PositiveIntegerField('ID объекта приложения')
    content_object = generic.GenericForeignKey()

    date = models.DateField(default=datetime.now, verbose_name='Дата')
    hits = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        unique_together = [('content_type', 'object_id', 'date')]

    def __str__(self):
        return '{0}: {1}'.format(self.date.strftime('%d-%m-%Y'), self.hits)

    @classmethod
    def find_for(cls, obj):
        """ Поиск записей счетчика по данному объекту  """
        if obj.pk:
            ct = ContentType.objects.get_for_model(obj)
            return cls.objects.filter(content_type=ct, object_id=obj.pk)
        else:
            raise ReferenceError('Object have not primary key for counter')

    @classmethod
    def hit(cls, obj, amount=1):
        """ Увеличение значения счетчика """
        ct = ContentType.objects.get_for_model(obj)
        with transaction.atomic():
            record, created = cls.objects.get_or_create(content_type=ct, object_id=obj.pk, date=datetime.now())
            record.hits += amount
            record.clean()
            record.save()

    @classmethod
    def get_hits_for(cls, obj):
        return cls.find_for(obj).aggregate(Sum('hits'))['hits__sum']

    @classmethod
    def get_hits_over_last_few_days(cls, obj, days=1):
        days = int(days)
        today_date = datetime.today()
        days = timedelta(days=days)
        finally_date = today_date-days
        return cls.find_for(obj).filter(date__range=(finally_date, today_date)).aggregate(Sum('hits'))['hits__sum']

