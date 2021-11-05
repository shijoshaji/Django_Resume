from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='ACtive Status')

    class Meta:
        abstract = True


class SocialMedia(BaseModel):
    title = models.CharField(max_length=50)
    mediaURL = models.CharField(
        max_length=500, verbose_name='Social media URL')
    iconClass = models.CharField(
        max_length=50, help_text='Eg: fa-linkedin', verbose_name='Font Awesom Icons')

    def __str__(self):
        return self.title


class Academics(BaseModel):

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

    class Meta:
        ordering = ["-year_of_passing"]

    def __str__(self):
        return self.course


class Professional(BaseModel):

    role = models.CharField(max_length=100, verbose_name='Role Name')
    company = models.CharField(max_length=250, verbose_name='Company Name')
    description = models.TextField(
        max_length=1000, verbose_name='Explain about the role')
    from_year = models.IntegerField(verbose_name='Year of Joining')
    to_year = models.IntegerField(verbose_name='Year of Resign', null=True)
    is_active = models.BooleanField(default=True, verbose_name='ACtive Status')
    # TODO: try date feilds, and for no to_year make a logic to update as present

    class Meta:
        ordering = ["-to_year"]

    def __str__(self):
        return f"{self.company} | {self.role}"
