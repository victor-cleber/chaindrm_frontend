from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customer'),
    path('distributor/', views.distributor, name='distributor'),
    path('blockchain/', views.blockchain, name='blockchain'),

    #path('tarefas/delete/<slug:id>', views.delete_tarefa),
    #path('',RedirectView.as_view(url='tarefas/'))
]
