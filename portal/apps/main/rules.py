import rules


@rules.predicate
def admin_only(user):
    return False
