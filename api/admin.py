from django.contrib import admin
from .models import Worker, Store, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    actions = None
