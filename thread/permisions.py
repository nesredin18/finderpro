from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user
class Istype(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        request.user_type==1