from django.db import models
from Management.models import Members

# Create your models here.
payments_types = (
    ('Offerings','Offerings'),('Pledges','Pledges'),('Tithes','Tithes')
)

class Transaction(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='member_payments')
    payment_type = models.CharField(max_length=50, choices=payments_types)
    amount_paid = models.DecimalField(decimal_places=2,max_digits=10)
    transaction_number = models.IntegerField()
    transaction_date = models.DateField(auto_now_add=True)


