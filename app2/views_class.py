from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView


class TestTemplateView(TemplateView):
    template_name = '2/test_templateview.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(self, **kwargs)
        context['info'] = '该变量可以传递到模板'
        return context
