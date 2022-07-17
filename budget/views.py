from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from budget.models import Budget, Expense


def home_view(request):
    budgets = sum(list(Budget.objects.values_list('amount', flat=True)))
    expenses = [list(expense) for expense in Expense.objects.all().values_list()]
    all_expense_amount = sum([expense[2] for expense in list(Expense.objects.all().values_list())])

    print(expenses)

    context = {
        'budgets': budgets,
        'expenses': expenses,
        'all_expense_amount': all_expense_amount
    }

    return render(request, 'budget/index.html', context)


class BudgetCreateView(CreateView):
    model = Budget
    fields = "__all__"
    success_url = "/"


class ExpenseCreateView(CreateView):
    model = Expense
    fields = "__all__"
    success_url = "/"


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = "__all__"
    success_url = "/"


class ExpenseDeleteView(DeleteView):
    model = Expense
    fields = "__all__"
    success_url = "/"

