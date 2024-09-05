from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView, View
from .redis_client import redis_client


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'random_number_app/home.html'


class NumberView(View):
    def get(self, request, *args, **kwargs):
        number = redis_client.get('random_number')

        if number is None:
            redis_client.set('random_number', 1)

        return JsonResponse({'number': number})
