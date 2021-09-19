from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_contact_email(name,receiver):
    # Creating message subject and sender
    subject = 'Message recieved'
    sender = 'cynthiabella.obonyo@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/contact.txt',{"name": name})
    html_content = render_to_string('email/contact.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()