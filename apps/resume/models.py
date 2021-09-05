from datetime import datetime, timedelta
from django.db import models


def default_stop_date(days=7):
    current_date = datetime.now()
    return current_date + timedelta(days=days)


class Resume(models.Model):
    resume_settings = models.ForeignKey('ResumeSendingSettings', verbose_name='настройки рассылки резюме',
                                        related_name='resume_settings', on_delete=models.CASCADE)
    resume_name = models.CharField('название резюме', max_length=255, blank=False)
    cover_letter = models.CharField('сопроводительное письмо', max_length=10000, blank=True, null=True)
    filtered_link = models.CharField('ссылка на hh.ru с примененными фильтрами поиска вакансий',
                                     max_length=255, blank=False)

    def __str__(self):
        return self.resume_name

    class Meta:
        verbose_name = 'резюме'


class Vacancy(models.Model):
    vacancy_name = models.CharField('название вакансии', max_length=255)
    company = models.CharField('название компании', max_length=255)
    link = models.CharField('ссылка на страницу вакансии', max_length=255)

    def __str__(self):
        return self.vacancy_name

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'


class ResumeSendingSettings(models.Model):
    HOUR_INTERVAL_CHOICES = (
        (8, 'каждые 8 часов'),
        (12, 'каждые 12 часов'),
        (24, 'каждые 24 часа'),
    )

    hour_interval = models.CharField('интервал рассылки', max_length=2, choices=HOUR_INTERVAL_CHOICES, default=24)
    stop_date_sending = models.DateField('дата остановки рассылки резюме', default=default_stop_date,
                                         help_text='не больше 30 дней')

    def __str__(self):
        return self.hour_interval

    class Meta:
        verbose_name = 'настройки рассылки'
        verbose_name_plural = 'настройки рассылки'
