import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error! Cannot open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error! Cannot read frame.")
        break

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f"Faces Detected: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    cv2.imshow('Face Tracking and Counting', frame)

    if cv2.waitKey(1) == ord ('q'):
        break 

cap.release()
cv2.destroyAllWindows()