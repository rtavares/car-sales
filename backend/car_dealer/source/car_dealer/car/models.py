from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Car(BaseModel):
    # Field for various pictures - TBD
    # Field for initial picture - TDB
    owner = models.ForeignKey(
        User, on_delete=models.DO_NOTHING
    )  # Should default to the current logged user
    brand = models.CharField(max_length=50)  # Should be a table lookup field
    model = models.CharField(max_length=50)  # Should be a table lookup field
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    seats = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    publishing_date = models.DateField(blank=True, null=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} - {self.model} - Display: {self.display}"
