from django.shortcuts import render

from .models import Organization

def index(request):
    organization_list = Organization.objects.all()
    return render(request, 'organizations/index.html', {'organization_list':organization_list})

# def detail(request, organization_slug):
    # return render(request, 'organization/index.html', {'organiztion_slug': organization_slug})


