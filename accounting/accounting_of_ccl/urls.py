from django.urls import path, include

from . import views

dict_new_patterns = [
    path('<str:model_type>/', views.dict_new, name='dictionary_new')
]
dict_info_patterns = [
    path('action/<str:action_type>/', views.dict_info_new, name='dictionary_info_new'),
    path('<str:model_type>/', views.dict_info, name='dictionary_info')
]
dict_edit_patterns = [
    path('<str:model_type>/<int:model_id>/', views.dict_edit, name='dictionary_edit')
]
dict_delete_patterns = [
    path('<str:model_type>/<int:model_id>/', views.dict_delete, name='dictionary_delete')
]
dict_patterns = [
    path('', views.dictionary, name='dictionary'),
    path('info/', include(dict_info_patterns)),
    path('new/', include(dict_new_patterns)),
    path('edit/', include(dict_edit_patterns)),
    path('delete/', include(dict_delete_patterns))
]
urlpatterns = [
    path('', views.index, name='index'),
    path('dict/', include(dict_patterns))
]

