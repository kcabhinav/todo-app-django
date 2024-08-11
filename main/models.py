from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    def complete(self) -> None:
        self.completed = True
