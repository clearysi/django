# Stdlib imports
from itertools import chain

# Core Django imports
from django.shortcuts import render, render_to_response, RequestContext, \
    redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, decorators
from django.template.loader import get_template
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

# Third-party app imports
from django_tables2 import RequestConfig

# Imports from app
from UploadFile_Funcitons import handle_uploaded_file
from folder_cleanup import delete_tmp_csv
from .models import SampleInformation, UploadFile, MailRequest
from .filterset import SampleInformationFilter
from .tables import SampleTable
from .queryset_to_csv import dump, id_generator
from .forms import SampleInputInformationForm, SampleQueryInformationForm,FileUploadForm, ContactForm, FirstCheckForm,SecondCheckForm


# Create your views here.
def display(request):
    return render(request, 'table/display.html',
                  {'obj': SampleInformation.objects.all()})


def login_user(request):
    state = "Please log in below"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # state="You're successfully logged in!"
                return HttpResponseRedirect('/home/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'table/auth.html',
                  {'state': state, 'username': username})

@decorators.login_required
def home(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
    return render(request, 'table/home.html')

@decorators.login_required
def input(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        #        state = "Please enter sample information below:"

        if request.method == 'POST':
            form = SampleInputInformationForm(request.POST)
            if form.is_valid():
                if request.user.has_perm('table.add_SampleInformation'):
                    sample = form.cleaned_data['d_number']
                    if SampleInformation.objects.filter(
                            d_number=sample).exists():
                        return render(request,
                                      'table/sample_exists_error.html')
                    else:
                        # new_sample = form.cleaned_data['d_number']
                        form.save()
                        messages.success(request,
                                         'Success: Your data has been '
                                         'submitted!')
                        return redirect('/input/')
                else:
                    return render(request, 'table/permission.html')
            else:
                print form.errors
                return render(request,'table/sample_exists_error.html',
                                          {'form': form.errors})
        else:
            form = SampleInputInformationForm()

            return render(request,'table/input.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'table/logout.html')

@decorators.login_required
def list(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        samples_exist = []
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                if request.user.has_perm('table.add_SampleInformation'):
                    data = handle_uploaded_file(request.FILES['upload'])
                    sample_keys = data.keys()
                    for sample in sample_keys:
                        # sample=form.cleaned_data['sample']
                        if SampleInformation.objects.filter(
                                d_number=sample).exists():
                            samples_exist += [sample]
                        # return render(request,
                        # 'table/sample_exists_error.html', {'form': form})
                        else:
                            s = SampleInformation(d_number=sample,
                                                  date=data[sample][0],
                                                  worksheet_number=
                                                  data[sample][1],
                                                  link=data[sample][2])
                            s.save()
                    if samples_exist == []:
                        samples_exist = None
                    messages.success(request,
                                     'Success: Your file has been uploaded!')
                    return render(request,'table/list.html',
                                              {'samples': samples_exist})
                else:
                    return render(request, 'table/permission.html')

                return render(request,'table/list.html', {'form': form})
            else:
                return render(request,'table/list.html', {'form': form})
        else:
            form = FileUploadForm()
            return render(request,'table/list.html', {'form': form})

@decorators.login_required
def index_sample(request):
    delete_tmp_csv()
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
    q = SampleInformation.objects.all()
#        if request.method == 'POST':
#            form = SampleQueryInformationForm(data=request.POST)
#            if form.is_valid():
#                d_number_list = form.cleaned_data['d_number']
#                start_date = form.cleaned_data['start_date']
#                end_date = form.cleaned_data['end_date']
#                worksheet_list = form.cleaned_data['worksheet_number']
#                link_list = form.cleaned_data['link']
#                my_obj_list = []
    if request.POST:
        form = SampleQueryInformationForm(data=request.POST)
        if form.is_valid():
            d_number_list=request.POST.getlist('d_number')
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            worksheet_list=request.POST.getlist('worksheet_number')
            link_list=request.POST.getlist('link')
            my_obj_list = []
            if (d_number_list):
                    #   d_number=d_number_list.strip().split(",")
                    #   d_number_list=[str(item) for item in d_number_list]
                    #                    for x1 in d_number:

                    #d_number=d_number_list.strip().split(",")
                for x1 in d_number_list:
                   # x2=x1.replace("u","")
                    q2 = q.filter(d_number=x1)
                    my_obj_list += [q2]
            if (start_date) and (end_date):
                q2 = q.filter(date__range=[start_date, end_date])
                my_obj_list += [q2]
            else:
                q2 = q.filter(date=start_date)
                my_obj_list += [q2]

            if (worksheet_list):
                   # worksheet = worksheet_list.strip().split(",")
                for x1 in worksheet_list:
                 #   x2 = x1.replace("u", "")
                    q2 = q.filter(worksheet_number=x1)
                    my_obj_list += [q2]
            if (link_list):
                #link = link_list.strip().split(",")
                for x1 in link_list:
                  #  x2 = x1.replace("u", "")
                    q2 = q.filter(link=x1)
                    my_obj_list += [q2]
        qs = SampleInformation.objects.none()
        for obj in my_obj_list:
            qs = qs | obj
            # q=list(chain(none_qs,my_obj_list))
        q = qs
    else:
        form = SampleQueryInformationForm()
    d_number_values = q.order_by('d_number').values('d_number').distinct()

    link_values = q.order_by('link').values('link').distinct()

    worksheet_number_values = q.order_by('worksheet_number').values('worksheet_number').distinct()

    table = SampleTable(q)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    filename = id_generator() + ".csv"
    dump(q, filename)
        #        f = "/home/scleary/Lab_database/files/" + filename
    context={
            'all_samples': q
        }
    return render(request,'table/results.html',
                                  {"obj": table, "queryfile": dump,
                                   "filename":filename,
                                   "queryset": q,
                                   "worksheet_number_values": worksheet_number_values,
                                   "d_number_values":d_number_values,
                                   "link_values": link_values,
                                   "form": form})


@decorators.login_required
def modify_sample(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
       #        state = "Please enter sample information below:"
        if request.method == 'POST':
            form = SampleQueryInformationForm(request.POST)
            if form.is_valid():
                sample = form.cleaned_data['d_number']
                date = form.cleaned_data['date']
                worksheet = form.cleaned_data['worksheet_number']
                link = form.cleaned_data['link']
                if SampleInformation.objects.filter(d_number=sample).exists():
                    if request.user.has_perm('table.add_SampleInformation'):
                        SampleInformation.objects.filter(
                            d_number=sample).update(date=date,
                                                    worksheet_number=worksheet,
                                                    link=link)
                        messages.success(request,
                                         'Sample has been '
                                         'successfully modified')
                        return redirect('/results/')
                    else:
                        return render(request, 'table/permission.html')
                else:
                    return render(request,'table/sample_exists_error.html',
                                              {'form': form.errors,
                                               "d_number": sample})
            else:
                return render(request,'table/sample_exists_error.html',
                                          {'form': form.errors})
        else:
            form = SampleQueryInformationForm()

            return render(request,'table/modify.html', {'form': form})

@decorators.login_required
def contact(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        context = RequestContext(request)
        #        state = "Please enter sample information below:"
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                if request.user.has_perm('table.add_MailRequest'):
                    subject = request.POST.get('subject', '')
                    sender = request.POST.get('sender', '')
                    message = request.POST.get('message', '')
                    req = MailRequest(sender=sender, subject=subject,
                                      message=message)
                    req.save()
                    messages.success(request, 'Your request has been sent')
                    return redirect('/home/')
            else:
                return render(request,'table/sample_exists_error.html',
                                          {'form': form.errors})
        else:
            form = ContactForm()

            return render(request,'table/contact.html', {'form': form})

@decorators.login_required
def request_list(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        if request.user.is_superuser:
            return render(request, 'table/request_list.html',
                          {'obj': MailRequest.objects.all()})

@decorators.login_required
def first_check(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        context = RequestContext(request)
        #        state = "Please enter sample information below:"
        if request.method == 'POST':
            form = FirstCheckForm(request.POST)
            if form.is_valid():
                sample = form.cleaned_data['d_number']
                date = form.cleaned_data['date']
                worksheet = form.cleaned_data['worksheet_number']
                link = form.cleaned_data['link']
                classification=form.cleaned_data['classification']
                first = form.cleaned_data['first_check']
                if SampleInformation.objects.filter(d_number=sample).exists():
                    if request.user.has_perm('table.add_SampleInformation'):
                        SampleInformation.objects.filter(d_number=sample,
                                                         date=date,
                                                         worksheet_number=
                                                         worksheet,
                                                         link=link).update(classification=classification,
                            first_check=first)
                        messages.success(request, form.errors)
                        return redirect('/results/')
                    else:
                        return render(request, 'table/permission.html')
                else:
                    return render(request,'table/sample_exists_error.html',
                                              {'form': form.errors,
                                               "d_number": sample})
            else:
                return render(request,'table/sample_exists_error.html',
                                          {'form': form.errors})
        else:
            sample = SampleInformation.objects.filter(
                first_check="not_checked")
            form = FirstCheckForm()

            return render(request,'table/first_check.html',
                                      {'form': form, 'obj': sample})

@decorators.login_required
def second_check(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
        context = RequestContext(request)
        #        state = "Please enter sample information below:"
        if request.method == 'POST':
            form = SecondCheckForm(request.POST)
            if form.is_valid():
                sample = form.cleaned_data['d_number']
                date = form.cleaned_data['date']
                worksheet = form.cleaned_data['worksheet_number']
                link = "file://" + form.cleaned_data['link']
                classification=form.cleaned_data['classification']
                first = form.cleaned_data['first_check']
                second = form.cleaned_data['second_check']
                if SampleInformation.objects.filter(d_number=sample).exists():
                    if request.user.has_perm('table.add_SampleInformation'):
                        if str(request.user) == first:
                            messages.error(request,
                                           "Sorry both checks cannot be "
                                           "performed by the same person")
                            return redirect('/second_check/')
                        else:
                            SampleInformation.objects.filter(d_number=sample).update(second_check=second)
                            messages.success(request,'Sample Information has been changed')
                            return redirect('/second_check/')
                    else:
                        return render(request, 'table/permission.html')
                else:
                    return render(request,'table/sample_exists_error.html',
                                              {'form': form.errors,
                                               "d_number": sample})
            else:
                return render(request,'table/sample_exists_error.html',
                                          {'form': form.errors})
        else:
            sample = SampleInformation.objects.exclude(
                first_check="not_checked")
            sample = sample.filter(second_check="not_checked")
            form = SecondCheckForm()
            form.fields['classification'].choices = [('VAR', 'variant'),
                                                  ('POL', 'polymorphism'),
                                                  ('ART', 'artefact')]
            form.fields['classification'].initial = ['VAR']
            return render(request,'table/second_check.html',
                                      {'form': form, 'obj': sample})

#@decorators.login_required
#def product_list(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/')
#    else:
#        f = SampleInformationFilter(request.GET,
#                                    queryset=SampleInformation.objects.all())
#        return render(request,'table/product_list.html', {'filter': f})
