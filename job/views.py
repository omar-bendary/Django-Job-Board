from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job
from .form import ApplicantForm


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


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()

    else:
        form = ApplicantForm()

    context = {
        'job': job,
        'form': form

    }
    return render(request, 'job/job_detail.html', context)
