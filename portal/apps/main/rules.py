import rules


@rules.predicate
def is_admin(user):
    return user.is_admin
