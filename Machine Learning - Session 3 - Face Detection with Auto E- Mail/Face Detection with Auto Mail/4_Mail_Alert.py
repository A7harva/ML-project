import cv2
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'xxxxxxxxx@email.com'
email_password = 'xxxxxxxxxx'
email_send = 'xxxxxxxxx@gmail.com'

subject = 'Alert!!!'

msg = MIMEMultipart()
msg['From'] = "From Python <"+email_user+">"
msg['To'] = email_send
msg['Subject'] = subject



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "0_haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['none', 'id 1', 'id 2'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
#cam.set(3, 480) # set video widht
#cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
mailStat = False

def sendmail(id):
    global names
   
    body = ('Hello The safe is accessed by the user ' +str(names[id])+'\n Please find the attachment')
    print(names[id])
    msg.attach(MIMEText(body,'plain'))
    filename='dataset/Userpic.png'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    try:  
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.mail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        print ('Email sent!'),email_send

        mailStat =False
    except:  
        #print ('Something went wrong...')
        print ('Email sent!'),email_send


while True:
    

    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        conf=round(100 - confidence)
        
        # Check if confidence is less them 100 ==> "0" is perfect match
        if mailStat==False:
            if ( conf > 30):
                cv2.imwrite("dataset/Userpic.png" ,img)
                sendmail(id)
                id = names[id]
                confidence = "  {0}%".format(conf)
                
                mailStat=True
                
            else:
                
                id = "unknown"
               
                confidence = "  {0}%".format(conf)
                
                     
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(conf), (x+5,y+h-5), font, 1, (255,255,0), 1)

    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(1) & 0xff # Press 'q' for exiting video
    if k == ord('q'):
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
