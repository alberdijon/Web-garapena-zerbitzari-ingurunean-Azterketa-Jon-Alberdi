from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='page-default'),

    path('pazienteak/', views.paziente_list, name='paziente-default'),
    path('pazienteak/new/', views.paziente_new, name='paziente-new'),
    path('pazienteak/edit/', views.paziente_edit, name='paziente-edit'),
    path('pazienteak/edit/<int:paziente_id>/', views.paziente_edit_form, name='paziente_edit_form'),
    path('paziente/delete/', views.paziente_delete, name="paziente-delete"),


    path('medikuak/', views.medikua_list, name='medikua-default'),
    path('medikuak/new/', views.medikua_new, name='medikua-new'),
    path('medikuak/edit/', views.medikua_edit, name='medikua-edit'),
    path('medikuak/edit/<int:medikua_id>/', views.medikua_edit_form, name='medikua_edit_form'),
    path('medikua/delete/', views.medikua_delete, name="medikua-delete"),

    path('zitak-list/', views.zita_list, name='zitak-default'),
    path('zitak/new/', views.zita_new, name='zitak-new')
]
