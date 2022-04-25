from rolepermissions.roles import AbstractUserRole
# from rolepermissions.roles import assign_role
# from .models import User


class Editer(AbstractUserRole):
    available_permissions = {
        'can_add_post': True,
        'Can view post': True,
        'Can delete post': True,
        'Can change post': True,

        'Can add tag': True,
        'Can view tag': True,
        'Can delete tag': True,
        'Can change tag': True,

        'Can add category': True,
        'Can view category': True,
        'Can delete category': True,
        'Can change category': True,
    }


# assign_role(User, 'editer')
