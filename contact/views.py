from django.shortcuts import render

# Create your views here.


def contact(request):

    # context {
    #     'from': form
    # }

    return render(request, 'contact.html')
