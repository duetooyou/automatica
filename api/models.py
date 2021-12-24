from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=80,
                            verbose_name="Имя работник")
    phone_number = models.IntegerField(verbose_name="Номер телефона")

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Список работников"

    def __str__(self):
        return f"{self.name} with phone {self.phone_number}"


class Store(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name="Название точки")
    worker = models.ForeignKey(Worker,
                               on_delete=models.CASCADE,
                               verbose_name="Работник",
                               related_name="workers")

    class Meta:
        verbose_name = "Точка"
        verbose_name_plural = "Список точек"

    def __str__(self):
        return f"{self.name}"


class Visit(models.Model):
    date = models.DateField(auto_now=True,
                            verbose_name="Посещение")
    store = models.ForeignKey(Store,
                              on_delete=models.CASCADE,
                              verbose_name="Точка",
                              related_name="stores")
    coordinates = models.TextField(verbose_name="Координаты")

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Список посещений"

    def __str__(self):
        return f"{self.date}"
