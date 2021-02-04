from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["username"] = "太郎"
        return context


class PistoView(TemplateView):
    template_name = "pisto.html"
