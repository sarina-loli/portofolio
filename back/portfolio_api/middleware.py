from user_agents import parse
from .models import Visitor


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        # Don't track Django admin, static files, etc.
        if not request.path.startswith('/admin/'):

            user_agent_string = request.META.get('HTTP_USER_AGENT', '')
            user_agent = parse(user_agent_string)

            Visitor.objects.create(
                user=request.user if request.user.is_authenticated else None,
                ip_address=self.get_client_ip(request),
                device=self.get_device(user_agent),
                browser=user_agent.browser.family,
                operating_system=user_agent.os.family,
                page=request.path,
            )

        return response

    def get_client_ip(self, request):
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR')

        if forwarded:
            return forwarded.split(',')[0].strip()

        return request.META.get('REMOTE_ADDR')

    def get_device(self, user_agent):
        if user_agent.is_mobile:
            return 'Mobile'
        elif user_agent.is_tablet:
            return 'Tablet'
        elif user_agent.is_pc:
            return 'Desktop'
        else:
            return 'Other'