from django.urls import path
from . import views


app_name = 'graph'
urlpatterns = [
    path('', views.graph_form, name='graph_form'),
    path('view/<int:pk>/', views.graph_view, name='graph_view'),
    path('save/<int:pk>/', views.save_graph, name='save_graph'),
]