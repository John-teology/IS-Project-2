from django import template


nameProb = {
    '1C Enterprise' : 'CEnterprise',
    'ASP.NET' : 'ASPNET',
    'C#':'CSharp',
    'C++':'Cplus',
    'F#':'FSharp',
    'HTML+RAZOR':'HTML_Razor',
    'Jupyter Notebook':'JupyterNotebook',
    'Objective-C':'ObjectiveC',
    'Objective-C++':'ObjectiveCplus',
    'OpenEdge ABL':'OpenEdgeABL',
    'Perl 6':'Perl6',
    'Protocol Buffer':'ProtocolBuffer',
}



register = template.Library()


@register.simple_tag
def update_variable(value):
    try:
        key_list = list(nameProb.keys())
        val_list = list(nameProb.values())
        position = val_list.index(value)
        return key_list[position]
    except ValueError:
        return value
