from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    status_choices = [
        (1, 'Ожидание'),
        (2, 'В процессе'),
        (3, 'Выполнено'),
    ]
    status = models.IntegerField(choices=status_choices, default=1)

    def __str__(self):
        return f"{self.name} - {self.status}"