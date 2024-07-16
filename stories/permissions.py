# stories/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to create, update, or delete.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Allow GET, HEAD, OPTIONS requests
            return True
        
        # Check if user is admin
        return request.user and request.user.is_staff
