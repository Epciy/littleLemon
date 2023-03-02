from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self):
        return self.title
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    


class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    def __str__(self):
        return self.table_number

class TableBooking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation for {self.user} at Table {self.table.table_number}"



