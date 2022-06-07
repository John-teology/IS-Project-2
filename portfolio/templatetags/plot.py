import matplotlib.pyplot as plt
from io import BytesIO
import base64
import urllib, base64
from django import template
register = template.Library()



@register.simple_tag
def plot(value):
   
    label = list(value.keys())
    data = list(value.values())
    # Creating plot
    fig = plt.figure(figsize =(10, 7))
    plt.pie(data,labels=label, startangle=90, autopct='%1.1f%%')
    plt.title("Language Distributions")
    buf = BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri