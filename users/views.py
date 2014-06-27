import csv

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from calculator.models import StringSet, String
from calculator import guitarstring

# Login
def authenticate_user(request, context):
    context = set_is_logged_in(request, context)
    context = set_session_username(request, context)
    return context


def set_is_logged_in(request, context):
    is_logged_in = request.user.is_authenticated()
    context['is_logged_in'] = is_logged_in
    return context


def set_session_username(request, context):
    if request.user.is_authenticated():
        context['username'] = request.user.get_username()
    return context


def login(request):
    context = authenticate_user(request, {})
    context.update(csrf(request))
    return render(request, 'login.html', context)

def auth_view(request):
    username = request.POST.get('username', '')
    print(username)
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render(request, 'invalid_login.html')
    # return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    context = authenticate_user(request, {})
    context.update(csrf(request))

    return render_to_response('logout.html', {}, context_instance=RequestContext(request))


# ###################################
def register_user(request):
    context = authenticate_user(request, {})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    context.update(csrf(request))

    context['form'] = UserCreationForm()
    return render_to_response('register.html', context, context_instance=RequestContext(request))


def register_success(request):
    context = authenticate_user(request, {})
    return render_to_response('register_success.html', context)


def profile(request):
    context = authenticate_user(request, {})
    context.update(csrf(request))
    if not context['is_logged_in']:
        return render_to_response('login.html', context)

    string_sets = StringSet.objects.filter(user=request.user)
    context['string_sets'] = string_sets
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def search(request):
    context = {}
    if request.user.is_authenticated():
        context['is_logged_in'] = True
        context['username'] = request.user.get_username()
    else:
        context['is_logged_in'] = False
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 50:
            errors.append('Please enter at most 50 characters.')
        else:
            context['search_name_results'] = StringSet.objects.filter(name__icontains=q)
            context['search_desc_results'] = StringSet.objects.filter(desc__icontains=q)
        context['errors'] = errors
    print(request)
    return render_to_response('search_results.html', context, context_instance=RequestContext(request))


def downloadStringSet(request):
    # get the response object, this can be used as a stream.
    response = HttpResponse(mimetype='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename="export.csv"'

    # the csv writer
    writer = csv.writer(response)

    context = {}
    if request.method == 'GET':
        print(request.GET)
        string_set_name = str(request.GET['string_set_name'])
        user = str(request.GET['user'])
        print(user)
        response['Content-Disposition'] = 'attachment;filename="' + string_set_name + ' export.csv"'
        context['string_set_name'] = string_set_name

        string_set = StringSet.objects.filter(name=string_set_name)

        for set in string_set:
            print(set)
            desc = set.desc
            is_mscale = set.is_mscale
            number_of_strings = set.number_of_strings

        strings = String.objects.all()
        user_set = []
        for string in strings:
            if str(string.string_set.name) == str(string_set_name):
                user_set.append(string)

    writer.writerow(["Name", string_set_name])
    writer.writerow(["Description", desc])
    writer.writerow(["Multiscale", is_mscale])
    writer.writerow(["Total Number of Strings", number_of_strings])
    writer.writerow(["Scale Length", string.scale_length])

    writer.writerow(["Number", "Note", "Octave", "Gauge", "String Type", "Tension"])
    for string in user_set:
        if is_mscale:
            gs = guitarstring.GuitarString(string.scale_length, string.string_type, string.gauge, string.note,
                                           string.octave, number_of_strings, string.string_number)
            writer.writerow([string.string_number, string.note, string.octave, string.gauge,
                             string.string_type, gs.calculate_tension()])
        else:
            gs = guitarstring.GuitarString(string.scale_length, string.string_type,
                                           string.gauge, string.note, string.octave)
            writer.writerow([string.string_number, string.note, string.octave, string.gauge, string.string_type,
                             gs.calculate_tension()])

    return response