from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Theme
from .forms import BbForm


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['themes'] = Theme.objects.all()
        return context


def index(request):
    all_goods = Bb.objects.all()
    themes = Theme.objects.all()
    return render(request, 'bboard/index.html', {'bbs': all_goods, 'themes': themes})


def by_theme(request, theme_id):
    """"returns all rubrics by certain theme"""
    all_goods = Bb.objects.filter(theme=theme_id)
    themes = Theme.objects.all()
    current_theme = Theme.objects.get(pk=theme_id)

    context = {'bbs': all_goods, 'current_theme': current_theme, 'themes': themes}
    return render(request, 'bboard/by_rubric.html', context)