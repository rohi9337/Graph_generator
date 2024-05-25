from django.urls import path
from . import views


app_name = 'graph'
urlpatterns = [
    path('', views.graph_form, name='graph_form'),
    path('save/', views.save_graph, name='save_graph'),
]
