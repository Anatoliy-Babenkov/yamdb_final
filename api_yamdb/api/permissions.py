from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Пользователь суперюзер или администратор.
    """
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_admin or request.user.is_superuser))


class IsAdminOrReadOnly(permissions.BasePermission):
    """Пользователь суперюзер или администратор,
    но для чтения доступно всем.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.is_admin or request.user.is_superuser)))


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пользователь автор, админ, модератор,
    но для чтения доступно всем.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator
                or request.user.is_superuser)

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
