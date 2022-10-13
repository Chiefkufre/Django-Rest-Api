from urllib import request
from rest_framework import permissions

from .permissions import IsStaffPermission, StaffPermission

class IsStaffPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffPermission]
    

class StaffPermissionMixin():
    permission_classes = [StaffPermission]

# possibe used case ----> constructing a dashboard view ----
class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
