from django.urls import path
from . import views

urlpatterns =[
    path('List/', views.ListEmp.as_view(), name="list_url"),
    path('Create/', views.CreateEmp.as_view(), name="create_url"),
    path('Update/<int:pk>/', views.UpdateEmp.as_view(), name="update_url"),
    path('Delete/<int:pk>/', views.DeleteEmp.as_view(), name="delete_url"),
    path('pdf/<int:pk>/',views.particularData, name='pdf2_url'),
    path('pdf/',views.GeneratePDF, name='pdf_url'),
]



