from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import About, Academics, Professional, Skills, SocialMedia


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
        tech_skill = Skills.objects.filter(is_key_skill=True,is_active=True)
        non_tech_skill = Skills.objects.filter(is_key_skill=False,is_active=True)
        abouts = About.objects.all()

        context["socialmedia"] = social_media_links
        context["education"] = academics_result
        context["profession"] = professional_result
        context["tech_skills"] = tech_skill
        context["non_tech_skills"] = non_tech_skill
        context["about_me"] = abouts
        return context
