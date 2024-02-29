# Use get_object_or_404 to handle non-existent users
# from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

# from django.contrib.auth.models import User This way there's no warning. But it explodes.
from my_app.models import User  # This way I get a warning in the IDE.
from .forms import UserForm

# Create your views here.


def user_new(request):
    if request.method == 'GET':  # First time user enter to the page.
        form = UserForm()  # Here is empty because there's no info to capture.

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    return render(request, 'user_new.html', {'form': form})


def user_edit(request, user_id):
    # user = get_object_or_404(User, id=user_id)
    user = User.objects.get(id=user_id)
    if request.method == 'GET':
        form = UserForm(instance=user)
        return render(request, 'user_edit.html', {'user': user, 'form': form})
        # return render(request, 'user_edit.html', {'user': user})  # Pass the user object to the context
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  # Pass the user object to the form
        if form.is_valid():
            form.save()
            return redirect('user_list')


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    if request.method == 'GET':
        return render(request, 'user_delete.html', {'user': user})


def user_list(request):
    user = User.objects.all()
    return render(request, 'user_list.html', {'users': user})
