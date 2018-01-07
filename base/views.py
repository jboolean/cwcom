from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import (
    ContentBlock,
    Portfolio,
    Project,
    System,
    Talk,
    Text,
    Event
)


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['events'] = Event.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['projects'] = Project.objects.all()
        context['systems'] = System.objects.all()
        context['talks'] = Talk.objects.all()
        context['texts'] = Text.objects.filter(category='tx')
        context['teaching_texts'] = Text.objects.filter(category='teaching')
        context['site_url'] = settings.SITE_URL

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context


class ProjectDetailView(generic.DetailView):
    template_name = 'project-detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['events'] = Event.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['projects'] = Project.objects.all()
        context['systems'] = System.objects.all()
        context['talks'] = Talk.objects.all()
        context['texts'] = Text.objects.filter(category='tx')
        context['teaching_texts'] = Text.objects.filter(category='teaching')
        context['site_url'] = settings.SITE_URL

        return context


class SystemDetailView(generic.DetailView):
    template_name = 'system-detail.html'
    model = System

    def get_context_data(self, **kwargs):
        context = super(SystemDetailView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['events'] = Event.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['projects'] = Project.objects.all()
        context['systems'] = System.objects.all()
        context['talks'] = Talk.objects.all()
        context['texts'] = Text.objects.filter(category='tx')
        context['teaching_texts'] = Text.objects.filter(category='teaching')
        context['site_url'] = settings.SITE_URL

        return context


class PastView(generic.TemplateView):
    template_name = 'past.html'

    def get_context_data(self, **kwargs):
        context = super(PastView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['events'] = Event.objects.filter(date__lte=today).order_by('-date')
        context['content_blocks'] = ContentBlock.objects.all()
        context['site_url'] = settings.SITE_URL
        context['projects'] = Project.objects.all()
        context['systems'] = System.objects.all()
        context['talks'] = Talk.objects.all()
        context['texts'] = Text.objects.filter(category='tx')
        context['teaching_texts'] = Text.objects.filter(category='teaching')

        return context


class PortfolioView(generic.TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['events'] = Event.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['projects'] = Project.objects.all()
        context['systems'] = System.objects.all()
        context['talks'] = Talk.objects.all()
        context['texts'] = Text.objects.filter(category='tx')
        context['teaching_texts'] = Text.objects.filter(category='teaching')
        context['site_url'] = settings.SITE_URL

        context['portfolio'] = Portfolio.objects.all()[0]


        return context
