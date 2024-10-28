from rest_framework import permissions


class IsUserObject(permissions.BasePermission):
    """Разрешение на изменение записи модели CustomUser.
    При запросах на чтение, изменение или удаление учётной записи
    проверьте, совпадает ли id пользователя, делающего сейчас запрос
    (request.user.id) с id владельца учётной записи
    (id объекта из модели CustomUser) obj.id.
    """

    def has_object_permission(self, request, view, obj):
        return (
            obj.id == request.user.id
        )


class IsAdmin(permissions.BasePermission):
    """Разрешение администратора.
    Сам запрос разрешён.
    Изменение объекта разрешено если приватный атрибут
    request.user.is_admin вернёт True.
    """
    # приватный атрибут is_admin прописан в моделе CustomUser
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class IsModerator(permissions.BasePermission):
    """Разрешение модератора.
    Сам запрос разрешён.
    Изменение объекта разрешено если приватный атрибут
    request.user.is_moderator вернёт True.
    """
    # приватный атрибут is_moderator прописан в моделе CustomUser
    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator


class IsUser(permissions.BasePermission):
    """Разрешение пользователя.
    Сам запрос разрешён.
    Изменение объекта разрешено если приватный атрибут
    request.user.is_user вернёт True.
    """
    # приватный атрибут is_user прописан в моделе CustomUser
    def has_object_permission(self, request, view, obj):
        return request.user.is_user


class ReadOnly(permissions.BasePermission):
    """Зазрешение за чтение у всех, в том числе и анонимов."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            )
