from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    """Public read access; only staff/admin users may create, update or delete.

    This keeps the portfolio content publicly viewable via the API while
    ensuring only the site owner (an authenticated staff user) can modify it.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
