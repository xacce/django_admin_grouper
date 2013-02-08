from django.template import Library


register = Library()

@register.assignment_tag
def admin_regroup_by(model_list, code_list, by):
    list = {}
    for index, record in enumerate(model_list):
        if hasattr(record, by):
            shop = unicode(getattr(record, by))
            if not shop in list:
                list[shop] = []

            list[shop].append(code_list[index])

    return list
