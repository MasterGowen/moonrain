from django.shortcuts import render
from django.shortcuts import redirect
from django.core.context_processors import csrf
from .forms import RegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list_all', new_user='yes')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'accounts/register.html', args)
