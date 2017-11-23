from django.contrib.auth.decorators import login_required
from clients.models import ClientProfile
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def unsubscribe(request, client_profile_id):

    if request.method == 'POST':
        Client = ClientProfile.objects.get(id=client_profile_id)
        User = ClientProfile.objects.get(id=client_profile_id).user
        if User.email == request.POST.get('email'):
            Client.email_unsubscribed = True
            Client.save()
            confirm_message = "Unsubscribed Successfully..."
        else:
            confirm_message = "Email is not exist or incorrect..."
        return render_to_response('unsubscribe/confirm.html',
                                  {'confirm_message': confirm_message},
                                  RequestContext(request))
    else:
        return render_to_response('unsubscribe/unsubscribe.html',
                              {'client_profile_id': client_profile_id},
                              RequestContext(request))