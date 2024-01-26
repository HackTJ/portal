import rules


@rules.predicate
def no_other_projects(user):
    return user.projects.count() == 0


@rules.predicate
def is_project_member(user, project):
    if not project:
        return False
    return user in project.members.all()


@rules.predicate
def is_unsubmitted(_, project):
    if not project:
        return False
    return not project.submitted
