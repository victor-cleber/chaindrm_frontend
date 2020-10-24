from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('', views.index),
    path('customer/', views.customer),
    path('distributor/', views.distributor),
    path('blockchain/', views.blockchain),

    #path('tarefas/delete/<slug:id>', views.delete_tarefa),
    #path('',RedirectView.as_view(url='tarefas/'))
]
