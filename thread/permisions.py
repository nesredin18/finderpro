from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id==request.user.id
class Istype(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.user_type_id)
        return request.user.user_type_id==1