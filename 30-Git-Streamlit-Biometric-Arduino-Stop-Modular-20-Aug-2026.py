import cv2
import numpy as np
import requests
import serial
import streamlit as st
import time

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

IP_URL = "http://192.168.1.6:8080/shot.jpg"
SERIAL_PORT = "COM4"
BAUD_RATE = 9600

@st.cache_resource
def get_serial_connection(port, baud):
    try:
        ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)
        return ser
    except Exception as e:
        st.sidebar.error(f"Could not connect to Serial Port {port}: {e}")
        return None

arduino = get_serial_connection(SERIAL_PORT, BAUD_RATE)

def send_to_arduino(char):
    if arduino and arduino.is_open:
        try:
            arduino.write(char.encode())
        except Exception:
            pass

def get_ip_webcam_frame(url):
    try:
        response = requests.get(url, timeout=1.5)
        if response.status_code == 200:
            img_bytes = np.asarray(bytearray(response.content), dtype=np.uint8)
            return cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
    except requests.exceptions.RequestException:
        pass
    return None

def login_page():
    st.title("🔒 Biometric Control Console")
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
    
    use_webcam = st.checkbox("Use Built-in Webcam (Uncheck to use IP Webcam)", value=True)
    
    col1, col2 = st.columns(2)
    detect_eyes = col1.checkbox("Enable Eye Detection", value=False)
    detect_smile = col2.checkbox("Enable Smile Detection", value=False)
    
    # --- SOLUTION: Use a master execution checkbox to control the while loop ---
    run_camera = st.checkbox("Toggle Camera Stream (Check to Run, Uncheck to Stop)", value=False)
    
    status_placeholder = st.empty()
    frame_placeholder = st.empty()

    # The while loop is driven directly by the web interface toggle instead of code variables
    if run_camera:
        cap = None
        if use_webcam:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                status_placeholder.warning("⚠️ Local webcam missing! Auto-routing to IP Webcam...")
                use_webcam = False
                if cap: cap.release()
        
        while run_camera:
            frame = None

            if use_webcam and cap and cap.isOpened():
                status_placeholder.info("📹 Scanning via: Local Webcam...")
                ret, frame = cap.read()
                if not ret:
                    status_placeholder.error("Failed to capture frame from local webcam.")
                    break
            else:
                status_placeholder.info(f"📱 Scanning via: IP Webcam ({IP_URL})...")
                frame = get_ip_webcam_frame(IP_URL)
                if frame is None:
                    status_placeholder.error("Failed to fetch image stream from IP Webcam address.")
                    break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))

            face_count = len(faces)
            smile_count = 0
            eye_count = 0

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                if detect_eyes:
                    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(15, 15))
                    eye_count = len(eyes)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

                if detect_smile:
                    smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22, minSize=(25, 25))
                    smile_count = len(smiles)
                    for (sx, sy, sw, sh) in smiles:
                        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

            # Send states to Arduino
            if face_count == 0:
                send_to_arduino('R')
            elif smile_count == 1:
                send_to_arduino('G')
            elif eye_count == 1:
                send_to_arduino('B')
            elif face_count == 1:
                send_to_arduino('Y')

            # Render frame on screen
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)
            
            # Simulated automatic unlock logic if a face is locked in
            if face_count > 0:
                # If you want to bypass navigation and jump to dashboard, toggle authentication
                #st.session_state.authenticated = True
                send_to_arduino('G')
                #break

        if cap:
            cap.release()
            
        if st.session_state.authenticated:
            frame_placeholder.empty()
            status_placeholder.empty()
            st.toast("Identity Verified!", icon="✅")
            time.sleep(0.5)
            st.rerun()
    else:
        status_placeholder.info("Camera is currently idle. Toggle the box above to activate.")
        frame_placeholder.empty()

# =====================================================================
# NAVIGATION ENGINE ROUTER
# =====================================================================
auth_view = st.Page(login_page, title="Authentication Gate", icon="🔒")
dashboard_view = st.Page("26-Streamlit-Biometric-Main-App-20-Aug-2026.py", title="Dashboard Console", icon="📊")

if not st.session_state.authenticated:
    navigation_router = st.navigation([auth_view], position="hidden")
else:
    navigation_router = st.navigation([dashboard_view], position="sidebar")

navigation_router.run()
