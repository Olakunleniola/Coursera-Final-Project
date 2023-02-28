#! /usr/bin/env python3
import os
import reports
from datetime import datetime
import emails

def generate_pdf_text():
    gen_data = []
    pdf_text = ''
    for texts in os.listdir('supplier-data/descriptions/'):
        with open('supplier-data/descriptions/'+texts, 'r') as f:
            dd = [x for x in f.read().splitlines()[0:2]]
        f.close()
        labels = ['name','weight']
        gen_data.extend(['{}: {}<br/><br/>'.format(labitm,keepitm) for labitm,keepitm in zip(labels,dd)])
            
    for i in range(len(gen_data)):
        if i%2!=0:
            pdf_text += gen_data[i] + '<br/>'
        else:
            pdf_text+=gen_data[i]
    return pdf_text

def main():
    title = 'Processed Update on '+ datetime.now().strftime('%B %d, %Y')
    pdf_text = generate_pdf_text()
    reports.generate_report('processed.pdf',title,pdf_text)
    sender = 'akandeola48@gmail.com'
    recipient = 'arrowofGod@gmail.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    filepath = 'C:\\Users\\OLAKUNLE AKANDE\\Downloads\\COURSERA FILES\\Coursera part 6 (Automating Real-World Tasks with Python)\\Final_Project_Folder\\processed.pdf'
    message = emails.generate(sender,recipient,subject,body,filepath)
    emails.send(message,sender)
if __name__ == '__main__':
    main()

