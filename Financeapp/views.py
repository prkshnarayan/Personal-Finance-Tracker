from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from .forms import AddTransactionForm
from .models import AddTransaction


def home(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            t1 = form.save()

            income = AddTransaction.objects.filter(Type='Income').aggregate(total=Sum('Amount'))['total'] or 0
            expense = AddTransaction.objects.filter(Type='Expense').aggregate(total=Sum('Amount'))['total'] or 0
            balance = income - expense

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'income': income,
                    'expense': expense,
                    'balance': balance,
                    'new_transaction': {
                        'Title': t1.Title,
                        'Amount': t1.Amount,
                        'Type': t1.Type,
                        'Category': t1.Category,
                        'Date': t1.Date.strftime('%Y-%m-%d')
                    }
                })
    else:
        form = AddTransactionForm()

    # Calculate totals for initial page load
    income = AddTransaction.objects.filter(Type='Income').aggregate(total=Sum('Amount'))['total'] or 0
    expense = AddTransaction.objects.filter(Type='Expense').aggregate(total=Sum('Amount'))['total'] or 0
    balance = income - expense

    transactions = AddTransaction.objects.all().order_by('Date')

    context = {
        'form': form,
        'income': income,
        'expense': expense,
        'balance': balance,
        'transactions': transactions
    }
    return render(request, 'display.html', context)
