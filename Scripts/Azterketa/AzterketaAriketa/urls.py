from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='page-default'),

    path('pazienteak/', views.paziente_list, name='paziente-default'),
    path('pazienteak/new/', views.paziente_new, name='paziente-new'),

    path('pazienteak/edit/', views.paziente_edit, name='paziente-edit'),
    path('pazienteak/edit/<int:paziente_id>/', views.paziente_edit_form, name='paziente_edit_form'),

]
