import c__

cap = cv2.VideoCaptu__(0)  # Open the webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.ims____("Video Frame", frame)  #Display it  
    if cv2.waitKey(1) == 27:  #Exit if ‘Esc’ pressed
        break
cap.release()  # Release resources
cv2.destroyAllWind___()