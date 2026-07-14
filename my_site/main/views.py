from django.shortcuts import render, redirect
from .models import Member
from django.db.models import Q


def home(request):
     # If the user clicks "Submit Member" button
    if request.method == 'POST':
        # Grab data from the input fields via their HTML 'name' attributes
        first = request.POST.get('fname')
        last = request.POST.get('lname')
        phone = request.POST.get('phone_num')
        date = request.POST.get('joined_dt')

        # Check which button was clicked
        action = request.POST.get('action')

        if action == 'delete':
            # Find the member by name and delete them
            try:
                member_to_delete = Member.objects.get(firstname=first, lastname=last)
                member_to_delete.delete()
            except Member.DoesNotExist:
                # If name doesn't exist, ignore or handle gracefully
                pass
            return redirect('home')
        
        if action == 'update':
            # Find the member by name and update them
            try:
                member_to_update = Member.objects.get(firstname=first, lastname=last)

                if phone:
                    member_to_update.phone = int(phone)

                if date:
                    member_to_update.joined_date = date

                member_to_update.save()

            except Member.DoesNotExist:
                # If name doesn't exist, ignore or handle gracefully
                pass
            return redirect('home')
        
        elif action == 'add':
            new_member = Member(
                firstname=first,
                lastname=last,
                phone=int(phone) if phone else None,
                joined_date =date or None,
            )
            new_member.save()
            return redirect('home')

    # Default logic for loading the page normally
    all_members = Member.objects.all().order_by('firstname').values()  # <-- Make sure .values() is here!
    
    context = {
        'mymembers': all_members,
    }
    return render(request, 'home.html', context)

def details(request, slug):
    # Fetch only the one member matching the specific slug
    mymember = Member.objects.get(slug=slug)
    
    context = {
        'mymember': mymember,
    }
    return render(request, 'details.html', context)

def index(request):
    return render (request, 'index.html')

def testing(request):
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
    return render (request, 'template.html',context)