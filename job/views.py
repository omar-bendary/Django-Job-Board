from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from .form import ApplicantForm, JobForm
from .filter import JobFilter
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    jobs_filter = JobFilter(request.GET, queryset=jobs)
    jobs = jobs_filter.qs

    paginator = Paginator(jobs, 5)  # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'jobs_num': jobs,
        'jobs_filter': jobs_filter


    }
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    form = ApplicantForm()

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()

    context = {
        'job': job,
        'form': form

    }
    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    context = {

        'form': form

    }
    return render(request, 'job/add_job.html', context)
