from rest_framework import permissions

from .permissions import IsStaffPermission, StaffPermission

class IsStaffPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffPermission]
    

class StaffPermissionMixin():
    permission_classes = [StaffPermission]
