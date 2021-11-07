from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib import messages

# Create your views here.
from .models import About, Academics, Professional, Skills, SocialMedia
from .forms import ContactForm


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
        tech_skill = Skills.objects.filter(is_key_skill=True, is_active=True)
        non_tech_skill = Skills.objects.filter(
            is_key_skill=False, is_active=True)
        abouts = About.objects.all()

        context["socialmedia"] = social_media_links
        context["education"] = academics_result
        context["profession"] = professional_result
        context["tech_skills"] = tech_skill
        context["non_tech_skills"] = non_tech_skill
        context["about_me"] = abouts
        return context


class ContactView(FormView):
    template_name = "contact/main.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)
