from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Assumes the object (obj) has an 'owner' attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Deny access for other methods unless the request.user is the owner.
        return obj.owner == request.user
