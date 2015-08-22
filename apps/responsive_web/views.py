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
            "host": "http://192.168.120.20:8080",
            "sign_up": "/index.php/user_registration",
            "sign_in": "/",
            "advertiser_sign_in": "/index.php/user_login/advertiser",
            "publisher_sign_in": "/index.php/user_login/publisher"
        }

        return context
