from django.db import models

# Create your models here.
from django.db import models

# Hero Section
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    intro = models.TextField()
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name

# About Section
class About(models.Model):
    description = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"About Section"

# Experience Section
class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=150, default='')

    def __str__(self):
        return f"{self.role} at {self.company}"



# Qualification / Education
class Qualification(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150, blank=True)
    period = models.CharField(max_length=50)
    scored = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree

# Projects
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=250)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Contact
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.email

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FrameworkAPI(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Database(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class ToolsPlatforms(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class WebTechnologies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class CoreConcepts(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OtherSkills(models.Model):
    name = models.CharField(max_length=50)

class SocialMedia(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.platform