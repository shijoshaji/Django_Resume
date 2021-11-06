from django.shortcuts import render

# Create your views here.
from .models import SocialMedia, Academics, Professional
from django.views.generic import TemplateView


def landing_page(request):
    template = "landingpage.html"
    return render(request, template)


class IndexView(TemplateView):
    template_name = "landingpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        social_media_links = SocialMedia.objects.filter(is_active=True)
        academics_result = Academics.objects.filter(is_active=True)
        professional_result = Professional.objects.filter(is_active=True)

        context["socialmedia"] = social_media_links
        context["education"] = academics_result
        context["profession"] = professional_result
        return context
