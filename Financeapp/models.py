from django.db import models

class AddTransaction(models.Model):
    class TypeChoices(models.TextChoices):
        INCOME = 'Income', 'Income'
        EXPENSE = 'Expense', 'Expense'

    Title = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Type = models.CharField(max_length=50, choices=TypeChoices.choices)
    Category = models.CharField(max_length=50)
    Date = models.DateField()

    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return f"{self.Title} - {self.Type} - {self.Amount}"
