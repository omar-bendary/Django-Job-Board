from django.db import models

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
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title
