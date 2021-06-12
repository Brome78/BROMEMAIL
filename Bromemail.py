from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter.messagebox import *

bromemail_fen=Tk()

frame1=LabelFrame(bromemail_fen, text="Expéditeur")
frame1.pack()
frame2=LabelFrame(bromemail_fen, text="Destinataire")
frame2.pack()
frame3=LabelFrame(bromemail_fen, text="Mail")
frame3.pack()

expediteurEmailLabel=Label(frame1, text="Adresse de l'expéditeur : ")
expediteurEmail=Entry(frame1, textvariable=str, width=70)

expediteurPasswordLabel=Label(frame1, text="Mot de passe : ")
expediteurPassword=Entry(frame1, textvariable=str, width=70)

expediteurEmailLabel.grid(row=1, column=1)
expediteurEmail.grid(row=1, column=2)
expediteurPasswordLabel.grid(row=2, column=1)
expediteurPassword.grid(row=2, column=2)

destinataireEmailLabel=Label(frame2, text="Adresse du destinataire : ")
destinataireEmail=Entry(frame2, textvariable=str, width=70)

destinataireEmailLabel.grid(row=1, column=1)
destinataireEmail.grid(row=1, column=2)

destinataireSujetLabel=Label(frame3, text="Sujet : ")
destinataireSujet=Entry(frame3, textvariable=str, width=147)

destinataireMessageLabel=Label(frame3, text="Message : ")
destinataireMessage=Text(frame3, height=30, width=110)

destinataireSujetLabel.grid(row=1, column=1)
destinataireSujet.grid(row=1, column=2)
destinataireMessageLabel.grid(row=2, column=1)
destinataireMessage.grid(row=2, column=2)


def sendMail():
    expediteurEmailRecup=expediteurEmail.get()
    expediteurPasswordRecup=expediteurPassword.get()
    destinataireEmailRecup=destinataireEmail.get()
    destinataireSujetRecup=destinataireSujet.get()
    destinataireMessageRecup=destinataireMessage.get("1.0", "end")

    message=EmailMessage()
    message['From']=expediteurEmailRecup
    message['To']=destinataireEmailRecup
    message['Subject']=destinataireSujetRecup
    message.set_content(destinataireMessageRecup)

    bromemail=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    bromemail.ehlo()
    bromemail.login(expediteurEmailRecup, expediteurPasswordRecup)
    bromemail.send_message(message)
    bromemail.quit()
    showinfo('Confirmation', 'EMAIL SENT !')
    bromemail_fen.destroy()


sendButton=Button(bromemail_fen, command=sendMail, text="Envoyer")
sendButton.pack()

bromemail_fen.mainloop()