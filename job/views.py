from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job


# Create your views here.


def job_list(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs, 2)  # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj

    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    job = Job.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'job/job_detail.html', context)
