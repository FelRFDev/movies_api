from rest_framework.permissions import BasePermission

class GlobalDefaultPermission(BasePermission):
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(request.method, view)
        if model_permission_codename == None:
            return False
        else:
            return request.user.has_perm(model_permission_codename)


    def __get_model_permission_codename(self, method, view):
        app_label = view.model.queryset._meta.app_label
        model_name = view.model.queryset._meta.model_name
        action = self.__get_action_sufix(method)

        try:
            return f'{app_label}.{model_name}_{action}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):

        METHOD_ACTIONS = {
            "GET":"view",
            "OPTION":"view",
            "HEAD":"view",
            "POST":"add",
            "PUT":"change",
            "PATCH":"change",
            "DELETE":"delete",
        }

        return METHOD_ACTIONS.get(method,'')