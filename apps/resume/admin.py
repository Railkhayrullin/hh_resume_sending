from django.contrib import admin

from .models import Resume, Vacancy, ResumeSendingSettings


class ResumeSendingSettingsInline(admin.TabularInline):
    model = ResumeSendingSettings
    extra = 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('resume_name', 'filtered_link')
    list_display_links = ('resume_name',)
    search_fields = ('resume_name',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'company')
    list_display_links = ('vacancy_name',)
    search_fields = ('vacancy_name', 'company')
