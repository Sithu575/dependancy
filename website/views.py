from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm,AddDepartmentForm,AddOrganizationForm,AddContactsForm,AddLeadsForm
from .models import Record
from .models import Organization,Lead
from django.contrib.auth.decorators import permission_required
from functools import wraps
from django.http import HttpResponseForbidden
from django.db.models import Case, When
from django.shortcuts import get_object_or_404


def permission_required(required_permission):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if the user has the required permission
            if request.user.has_perm(required_permission):
                # If permission is granted, execute the original view function
                return view_func(request, *args, **kwargs)
            else:
                # If permission is not granted, return a forbidden response
                return HttpResponseForbidden("Permission Denied")

        return wrapper

    return decorator


def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records}) #this records is same as the above variable


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})

def add_department(request):
	form = AddDepartmentForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_department = form.save()
				messages.success(request, "Department Added...")
				return redirect('home')
		return render(request, 'add_department.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



#RECORDS

@permission_required("website.add_record")
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


@permission_required("website.update_record")
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


@permission_required("website.delete_record")	
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
	
#FOR VIEWING EACH RECORD IT CONTAIN DELETE AND UPDATE BUTTON
@permission_required("website.view_record")
def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records and grab single record using id by passing argument as pk
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def add_organization(request):
	form = AddOrganizationForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_organization = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_organization.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def organization_details(request, pk):
	if request.user.is_authenticated:
		# Look Up Records and grab single record using id by passing argument as pk
		organization_details = Organization.objects.get(id=pk)
		return render(request, 'record.html', {'organization_detail':organization_details})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def add_leads(request):
	form = AddLeadsForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_leads = form.save()
				messages.success(request, "Lead Added...")
				return redirect('lead')
		return render(request, 'add_leads.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def lead(request):
	leads = Lead.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'lead.html', {'leads':leads}) #this records is same as the above variable

#BY CLICKING ID ON THE LEAD TABLE WE CAN SEE THE LEADS OF CURRESPONDING ID 
def view_leads(request, pk):
	if request.user.is_authenticated:
		# Look Up Records and grab single record using id by passing argument as pk
		view_leads = Lead.objects.get(id=pk)
		
		return render(request, 'view_leads.html', {'view_leads':view_leads})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

"""@permission_required("website.can_lead_approval")	
def lead_approval(request,pk):
    if request.user.is_authenticated:
      if request.method == "POST":
        Lead.objects.filter(pk=pk).update(approved=True)
        
        return redirect('None')
    else:
        return redirect('home')"""

@permission_required("website.can_lead_approval")	
def lead_approval(request,pk):
    if request.user.is_authenticated:
      
        approval =  Lead.objects.get(id=pk)# Retrieve the instance from the database
        print(pk)
        approval.approved=True
        approval.save()
        return redirect('lead')
    else:
        return redirect('home')
	
	
def add_contacts(request):
	form = AddContactsForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_contacts = form.save()
				messages.success(request, "Contact Added...")
				return redirect('home')
		return render(request, 'add_contacts.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
#dropdown dependency
	
def load_organization(request):
    type_id = request.GET.get("type")
    organizations = Organization.objects.filter(type_id=type_id)
    return render(request, "dropdown.html", {"organizations": organizations})

def search_lead(request):
    search_text = request.POST.get('search')
    results=Lead.objects.filter(name_icontains=search_text)
    context={'results':results}
    return render(request,'search_results.html',context)