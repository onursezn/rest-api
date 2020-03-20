from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit own profile"""

    def has_onject_permission(self, request, view, obj):
        """check user if is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
