from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Job(models.Model):

    JOB_TYPE = [
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Team Leader', 'Team Leader')
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

    def __str__(self):
        return self.title
