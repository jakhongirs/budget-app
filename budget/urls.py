from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('add_budget/', views.BudgetCreateView.as_view(), name="budget_form"),
    path('add_expense/', views.ExpenseCreateView.as_view(), name="expense_form"),
    path('update_expense/<int:pk>', views.ExpenseUpdateView.as_view(), name="update_expense"),
    path('delete_expense/<int:pk>', views.ExpenseDeleteView.as_view(), name="delete_expense"),
]
