
from django.shortcuts import render

from reporting.forms import GetReportingForm, RegistrationForm

from googleads import adwords
from reporting import get_campaigns
from ReportingAdmin.utils import render_to_pdf
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/login/")

def login(request):
    return HttpResponseRedirect("/login/")

def getRegistration(request):
    return render(request, 'registration/registration.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def get_context_data(request):

    context ={}
    try:
        simpleList = []
        simpleList = get_campaigns.getCampaigns()
        context ={'all_cajas' : simpleList}
    except Exception as e:
        print (e)
            
    return render(request, 'reporting/index.html', context)

def campaignsToPDF(request, *args, **kwargs):
    
    class SimpleClass(object):
        pass
    
    campanias  = []
    campanias = get_campaigns.getCampaigns()
    context = {
        'campanias': campanias,
    } 

    template = get_template ('pdf/campaigns.html')
    html = template.render(context)
    pdf = render_to_pdf('pdf/campaigns.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "InformeX_cierre%s.pdf" #%(cierre_id)
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        response['content-Disposition'] = content
        return response
    else:
        return HttpResponse("Not Found")  

def getReporting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetReportingForm(request.POST)
        print(form)
        
        errors = []
        error = False
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            observaciones = form.cleaned_data['observaciones']
            
            # Initialize the AdWords client.
            adwords_client = adwords.AdWordsClient.LoadFromStorage()
            
            
            return render(request, 'reporting/index.html', {'errors': errors})
        else:
            errors.append("No existe un dia de trabajo creado.")
            return render(request, 'reporting/index.html', {'errors': errors})
            