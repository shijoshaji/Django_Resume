from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Active Status')

    class Meta:
        abstract = True


class About(BaseModel):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50, verbose_name='Profile Name')
    intro = models.CharField(max_length=150, verbose_name='One Line Intro')
    desp = models.TextField(max_length=2000, verbose_name='About Me')
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1,
                              verbose_name=" Choose Sex")
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Mobile Number')
    location = models.CharField(
        max_length=100, verbose_name='Current Location')

    avatar = models.CharField(blank=True, null=True, max_length=255,
                              verbose_name='URL to your Profile Pic')
    cv = models.CharField(blank=True, null=True, max_length=255,
                          verbose_name='URL to your Resume')

    def __str__(self):
        return self.name


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
    skillurl = models.CharField(
        max_length=300, verbose_name='Skill Logo URL', null=True, blank=True)
    scale = models.IntegerField(
        default=50, verbose_name='Rating of skill', help_text='Enter a range from 0 -100')
    is_key_skill = models.BooleanField(
        default=False, verbose_name='Is this Tech Skill', help_text='Tick if this is technical skill')

    class Meta:
        ordering = ["-scale"]

    def __str__(self):
        return self.skill
