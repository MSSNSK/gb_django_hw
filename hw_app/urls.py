from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeViews.as_view(), name='index'),
    path('about/', views.AboutViews.as_view(), name='about'),
    path('customer/<int:pk>/', views.CustomerView.as_view(), name='customer_page'),
    path('orders/year/<int:year>/<int:pk>/', views.AllYearProducts.as_view(), name='yearly_orders'),
    path('orders/monthly/<int:year>/<int:month>/<int:pk>/', views.AllMonthProducts.as_view(), name='monthly_orders'),
    path('orders/week/<int:year>/<int:week>/<int:pk>/', views.AllWeekProducts.as_view(), name='weekly_orders'),
]
