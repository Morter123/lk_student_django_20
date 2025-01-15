from django.urls import path
from . import views

urlpatterns = [ 
    path('dashboard/<int:id>/', views.student_dashboard, name='dashboard'),
    path('analysis/', views.analysis_view, name='analysis'),
]