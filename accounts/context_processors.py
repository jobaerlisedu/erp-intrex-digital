from .decorators import ERP_MODULE_NAMES


def user_modules(request):
    """
    Adds `user_modules` (a set of module names) to every template context.
    Used by erp_base.html to conditionally show/hide sidebar items.
    """
    if not request.user.is_authenticated:
        return {'user_modules': set()}

    # Superusers and staff see everything
    if request.user.is_superuser or request.user.is_staff:
        return {'user_modules': set(ERP_MODULE_NAMES)}

    # Regular users: derive access from their groups
    accessible = set()
    for group in request.user.groups.all():
        name = group.name
        if name.endswith('_access'):
            module = name[:-7]  # strip '_access'
            if module in ERP_MODULE_NAMES:
                accessible.add(module)

    return {'user_modules': accessible}
