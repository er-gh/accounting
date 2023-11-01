from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .forms import *

from urllib.parse import urlparse


def get_models():
    models = [
        Building,
        Owner,
        Room,
        Organization,
        Subdivision,
        Responsible,
        WireCore,
        Equipment,
        Port,
        Cable
    ]
    return models


@login_required
def index(request):
    models = get_models()
    context = {}
    models_obj = {}
    for model in models:
        models_obj[f'{model._meta.verbose_name}'] = [model.__name__.lower(), len(model.objects.all())]
    context['models_obj'] = models_obj
    return render(request, 'accounting_of_ccl/index.html', context)


@login_required
def dictionary(request):
    context = {}
    return render(request, 'accounting_of_ccl/dictionary/dictionary.html', context)


@login_required
def dict_info(request, model_type):
    models = get_models()
    for model in models:
        if model_type == model.__name__.lower():
            context = {
                'title': model._meta.verbose_name,
                'model': model.objects.all(),
                'model_type': model_type,
                'ref': reverse('dictionary_info_new', args=['delete']) == urlparse(request.META.get('HTTP_REFERER')).path
            }
            return render(request, 'accounting_of_ccl/dictionary/info/info.html', context)
    raise Http404()


@login_required
def dict_edit(request, model_type, model_id):
    models = get_models()
    form = None
    model_name = None
    for model in models:
        if model_type == model.__name__.lower():
            model_name = model._meta.verbose_name
            model_inst = get_object_or_404(model, id=model_id)
            form = modelform_factory(model, fields="__all__")
            if request.method == 'POST':
                form = form(request.POST, instance=model_inst)
                if form.is_valid():
                    form.save()
                    return redirect('dictionary_info', model_type)
            else:
                form = form(instance=model_inst)
    context = {
        "model_type": model_type,
        "model_id": model_id,
        "model_name": model_name,
        "form": form
    }
    return render(request, 'accounting_of_ccl/dictionary/edit/edit.html', context)


@login_required
def dict_info_new(request, action_type):
    models = get_models()
    if action_type == 'new':
        action_type = 'Добавить'
    elif action_type == 'edit':
        action_type = 'Редактировать'
    elif action_type == 'delete':
        action_type = 'Удалить'
    else:
        raise Http404
    context = {
        'action_type': action_type
    }
    models_obj = {}
    for model in models:
        models_obj[f'{model._meta.verbose_name}'] = model.__name__.lower()
    context['models_obj'] = models_obj
    return render(request, 'accounting_of_ccl/dictionary/info/new.html', context)


@login_required
def dict_new(request, model_type):
    models = get_models()
    context = {}
    for model in models:
        if model.__name__.lower() == model_type:
            form = modelform_factory(model, fields="__all__")
            context['title'] = model._meta.verbose_name
            if request.method == 'POST':
                form = form(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('dictionary_info_new', 'new')
            context['form'] = form
    return render(request, 'accounting_of_ccl/dictionary/new/new.html', context)


@login_required
def dict_delete(request, model_type, model_id):
    models = get_models()
    model_name = None
    model_inst = None
    for model in models:
        if model.__name__.lower() == model_type:
            model_name = model._meta.verbose_name
            model_inst = get_object_or_404(model, id=model_id)
            if request.method == 'POST':
                model_inst.delete()
                return redirect('dictionary_info', model_type)
    context = {
        'model_type': model_type,
        'model_id': model_id,
        'model_name': model_name,
        'model_inst_fields': model_inst.get_fields()
    }
    return render(request, 'accounting_of_ccl/dictionary/delete/delete.html', context)
