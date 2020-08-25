from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def chat_list(request):
	try:
		messages = request.user.venue.message_set.all().distinct('customer')
		user_type = 'venue'
	except:
		messages = request.user.customer.message_set.all().distinct('venue')
		user_type = 'customer'
	return render(request, 'chat-list.html', {'messages': messages, 'user_type': user_type})