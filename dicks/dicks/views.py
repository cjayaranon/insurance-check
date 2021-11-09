from django.views import generic


class Test503(generic.TemplateView):
    template_name = '500.html'