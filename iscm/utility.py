def userAuthentication(loginid, password):
	role = ''
	message = 'authenticated'
	if loginid == '1' and password == 'commercial':
		role = 'commercial'
	elif loginid == '2' and password == 'hr':
		role = 'hr'
	elif loginid == '3' and password == 'operation':
		role = 'operation'
	else:
		message = 'unauthenticated'
		role = ''

	return {'message' : message,'loginid': loginid, 'role' : role}


def find_user_locationlist():
	from account.models import User, UserAccess
	from location.models import OperationLocation
	#findUser
	# import pdb;pdb.set_trace()
	location_for_individualuser = None
	try:
		# import pdb;pdb.set_trace()
		# user_object = User.objects.get(userid = userid)
		locationlist = [i[0] for i in OperationLocation.objects.all().values_list('oplocationid')]
		if locationlist:
			# location_for_individualuser = UserAccess.objects.filter(user = user_object).values_list('location')
			location_for_individualuser = locationlist
			# print("location_for_individualuser {}".format(location_for_individualuser))

			# print('here it comes in utility find user location')
		else:
			location_for_individualuser = None
	except:
		return location_for_individualuser

	return location_for_individualuser


def email(request):
	from django.core.mail import send_mail
	from django.conf import settings
	subject = 'Thank you for registering to our site'
	message = ' it  means a world to us '
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['25004740@mahindra.com',]
	send_mail( subject, message, email_from, recipient_list )
	# return redirect('redirect to a new page')

