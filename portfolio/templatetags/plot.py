from django import template
import seaborn as sns
import matplotlib.pyplot as plt
register = template.Library()



@register.simple_tag
def plot(value):
    data = list(value.keys())
    keys = list(value.values())
    palette_color = sns.color_palette('bright')
    
    plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
    
    plt.show()