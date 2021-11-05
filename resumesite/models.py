from django.db import models

# Create your models here.


class SocialMedia(models.Model):
    title = models.CharField(max_length=50)
    mediaURL = models.CharField(
        max_length=500, verbose_name='Social media URL')
    iconClass = models.CharField(
        max_length=50, help_text='Eg: fa-linkedin', verbose_name='Font Awesom Icons')
    is_active = models.BooleanField(default=True, verbose_name='ACtive Status')

    def __str__(self):
        return self.title


class Academics(models.Model):

    ACADEMY_CHOICE = (
        ('High School', 'High School'),
        ('12th', '12th'),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ("Others", "Others")
    )
    level = models.CharField(choices=ACADEMY_CHOICE, max_length=50,
                             verbose_name=" Choose level of academic")
    course = models.CharField(max_length=100, verbose_name='Course Title')
    college = models.CharField(max_length=250, verbose_name='College Name')
    description = models.TextField(
        max_length=1000, verbose_name='Explain about the course')
    year_of_passing = models.IntegerField(verbose_name='Year of passing out')
    is_active = models.BooleanField(default=True, verbose_name='ACtive Status')

    class Meta:
        ordering = ["-year_of_passing"]

    def __str__(self):
        return self.course
