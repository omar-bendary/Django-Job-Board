from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Customize iamge name when uploaded


def image_upload(instance, filename):
    image_name, extention = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extention)


class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=50)
    # loaction
    job_type = models.CharField(choices=JOB_TYPE, max_length=50)
    description = models.TextField(max_length=1000)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    published_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(max_length=500)
    applied_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
