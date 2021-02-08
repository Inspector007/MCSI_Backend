from django.shortcuts import render
from account.models import User
from account.forms import UserLoginForm

# Create your views here.

def userlogin_view(request):
    try:
        if request.method == 'POST':
            # A comment was posted
            # userlogin_form = UserLoginForm(data=request.POST)
            data=request.POST

            if 1==1:
                # Create Comment object but don't save to database
                # new_comment = userlogin_form.save(commit=False)
                # Assign the current post to the comment
                # new_comment.post = post
                # Save the comment to the database
                # new_comment.save()
                return render(request,'account/base.html')
            else:
                userlogin_form = UserLoginForm()
            # return render(request,'account/userlogin.html',{'userlogin_form': userlogin_form})

            return render(request, 'account/userlogin.html', {'error': "Your username and password didn't match. Please try again"})
        else:
           return render(request, 'account/userlogin.html')
    except:
        return render(request, 'userlogin.html', {'error': "Your username and password didn't match. Please try again"})

