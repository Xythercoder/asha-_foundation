from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ProgressReportForm
from .models import Progress_report

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('users:dashboard')
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('users:dashboard')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'app/signup.html', {'form': form})


@login_required
def dashboard_view(request):
	return render(request, 'app/dashboard.html')


def home_view(request):
	return render(request, 'app/home.html')


def about_view(request):
    return render(request, 'app/about.html')

def contact_view(request):
    return render(request, 'app/contact.html') 
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request, 'app/home.html') 


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HouseholdData
from .forms import HouseholdDataForm

@login_required
def household_list(request):
    data = HouseholdData.objects.filter(user=request.user)
    return render(request, 'household/list.html', {'data': data})


@login_required
def household_create(request):
    if request.method == 'POST':
        form = HouseholdDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Submitted successfully!")  
            return redirect('users:household_list')   
    else:
        form = HouseholdDataForm()
    return render(request, 'household/form.html', {'form': form})


@login_required
def household_list(request):
    household_data = HouseholdData.objects.filter(user=request.user)
    return render(request, 'household/list.html', {'household_data': household_data})



@login_required
def household_update(request, pk):
    household_data = get_object_or_404(HouseholdData, pk=pk, user=request.user)
    if request.method == "POST":
        form = HouseholdDataForm(request.POST, instance=household_data)
        if form.is_valid():
            form.save()
            return redirect('users:household_list')
    else:
        form = HouseholdDataForm(instance=household_data)
    
    return render(request, 'household/form.html', {'form': form})
@login_required
def household_delete(request, pk):
    record = get_object_or_404(HouseholdData, pk=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('users:household_list')  
    return render(request, 'household/delete.html', {'record': record})


@login_required
def progress_report_create(request):
    if request.method == 'POST':
        form = ProgressReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('users:progress_report_list')
    else:
        form = ProgressReportForm()
    return render(request, 'progress/create.html', {'form': form})

def progress_report_list(request):
    progress_reports = Progress_report.objects.all().order_by('-created_at')
    return render(request, 'progress/list.html', {'progress_reports': progress_reports})