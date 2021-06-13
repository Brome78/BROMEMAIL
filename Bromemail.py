from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter.filedialog import askopenfilename
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

message=MIMEMultipart()

def sendMail():
    expediteurEmailRecup=expediteurEmail.get()
    expediteurPasswordRecup=expediteurPassword.get()
    destinataireEmailRecup=destinataireEmail.get()
    destinataireSujetRecup=destinataireSujet.get()
    destinataireMessageRecup=destinataireMessage.get("1.0", "end")

    
    message['From']=expediteurEmailRecup
    message['To']=destinataireEmailRecup
    message['Subject']=destinataireSujetRecup
    msg=destinataireMessageRecup
    message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

    

    bromemail=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    bromemail.ehlo()
    bromemail.login(expediteurEmailRecup, expediteurPasswordRecup)
    texte=message.as_string().encode('utf-8')
    bromemail.sendmail(expediteurEmailRecup, destinataireEmailRecup, texte)
    bromemail.quit()
    showinfo('Confirmation', 'EMAIL SENT !')
    bromemail_fen.destroy()

def pieceJointe():
    pieceJointeFen=Tk()
    pieceJointeFen.title("Ajout de piece jointe")

    entree=askopenfilename(title="Ouvrir le fichier", filetypes=[('all files', '.*')])
    warningLabel=Label(pieceJointeFen, text="choisir le nom de la piece jointe (ne pas oublier l'extension) : ")
    cheminPiece=Label(pieceJointeFen, text=entree)
    cheminPiece.pack()
    warningLabel.pack()
    nomDeLaPiece=Entry(pieceJointeFen, textvariable=str, width=70)
    nomDeLaPiece.pack()

    def validationPieceJointe():
        chemin=entree
        piece=open(chemin, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" %  nomDeLaPiece.get())
        message.attach(part)
        showinfo('Conhirmation', 'Piece jointe ajouté')
        pieceJointeFen.destroy()
    
    valider=Button(pieceJointeFen, text="Valider", command=validationPieceJointe)
    valider.pack()
    
    pieceJointeFen.mainloop()
    
destinatairePieceJointeButton=Button(frame3, text="Ajouter une piece jointe", command=pieceJointe)
destinatairePieceJointeButton.grid(row=3, column=2)


#destinatairePieceJointeButton=Button(frame3, text="Ajouter une piece jointe", command=pieceJointe)

destinataireSujetLabel.grid(row=1, column=1)
destinataireSujet.grid(row=1, column=2)
destinataireMessageLabel.grid(row=2, column=1)
destinataireMessage.grid(row=2, column=2)
#destinatairePieceJointeButton.grid(row=3, column=2)

sendButton=Button(bromemail_fen, command=sendMail, text="Envoyer")
sendButton.pack()

bromemail_fen.mainloop()