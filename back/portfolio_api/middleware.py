from user_agents import parse

from .models import Visitor, VisitorPageView


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        # Don't track Django admin
        if not request.path.startswith('/admin/'):

            visitor_cookie = request.COOKIES.get('visitor_id')

            visitor = None

            # Find existing visitor
            if visitor_cookie:
                visitor = Visitor.objects.filter(
                    visitor_id=visitor_cookie
                ).first()

            # Create new visitor if this is a new browser
            if visitor is None:

                user_agent_string = request.META.get(
                    'HTTP_USER_AGENT',
                    ''
                )

                user_agent = parse(user_agent_string)

                visitor = Visitor.objects.create(
                    user=(
                        request.user
                        if request.user.is_authenticated
                        else None
                    ),
                    ip_address=self.get_client_ip(request),
                    device=self.get_device(user_agent),
                    browser=user_agent.browser.family,
                    operating_system=user_agent.os.family,
                )

                # Mark as new visitor
                new_visitor = True

            else:
                new_visitor = False

            # Save the page visited by this visitor
            VisitorPageView.objects.create(
                visitor=visitor,
                page=request.path,
            )

            # Give new visitor a cookie
            if new_visitor:
                response.set_cookie(
                    'visitor_id',
                    str(visitor.visitor_id),
                    max_age=60 * 60 * 24 * 365,
                    httponly=True,
                    samesite='Lax'
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