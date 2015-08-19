from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        # get the session info
        # session_data = self.request.session

        # context['current_user'] = session_data.get('username')
        context['server_links'] = {
            "sign_up": "http://yookosadserver.local.192.168.2.25.xip.io:8890/index.php/user_registration",
            "sign_in": "http://yookosadserver.local.192.168.2.25.xip.io:8890/"
        }

        return context
