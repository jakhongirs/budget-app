from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('budget.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
