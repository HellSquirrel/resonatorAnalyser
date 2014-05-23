from django import template

register = template.Library()


@register.tag
def start_template(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return TemplateStartNode(format_string[1:-1])


class TemplateStartNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return '<script type="text/template" id="%s">' % self.format_string


def end_template():
    return '</script>'

register.simple_tag(end_template)

