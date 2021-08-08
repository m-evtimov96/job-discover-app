from django.core.exceptions import PermissionDenied


class IsOwnerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().user != request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class BelongsToCompany(object):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().company.user.id != request.user.id:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
