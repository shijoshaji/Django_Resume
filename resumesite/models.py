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
    from_year = models.DateField(verbose_name='Year of Joining')
    to_year = models.DateField(
        verbose_name='Year of Resign', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='ACtive Status')

    class Meta:
        ordering = ["-from_year"]

    def __str__(self):
        return f"{self.company} | {self.role}"


class Skills(BaseModel):
    skill = models.CharField(max_length=75, verbose_name='Skill Name')
    scale = models.IntegerField(
        default=50, verbose_name='Rating of skill', help_text='Enter a range from 0 -100')
    is_key_skill = models.BooleanField(
        default=False, verbose_name='Is this Tech Skill', help_text='Check MArk if this is technical skill')

    class Meta:
        ordering = ["-scale"]

    def __str__(self):
        return self.skill
