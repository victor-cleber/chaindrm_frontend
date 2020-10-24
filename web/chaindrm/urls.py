from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('customer/', views.customer),
    path('distributor/', views.distributor),
    path('chaincode/', views.chaincode),

    #path('tarefas/delete/<slug:id>', views.delete_tarefa),
    #path('',RedirectView.as_view(url='tarefas/'))
]
