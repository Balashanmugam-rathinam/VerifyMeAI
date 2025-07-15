import streamlit as st
import cv2
import numpy as np
import random
import string
import os

# Load known face
KNOWN_FACE_PATH = "priya.jpg"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if not os.path.exists(KNOWN_FACE_PATH):
    st.error(f"Known face image not found at {KNOWN_FACE_PATH}")
    st.stop()

known_face = cv2.imread(KNOWN_FACE_PATH)
known_face_gray = cv2.cvtColor(known_face, cv2.COLOR_BGR2GRAY)

# Function to generate CAPTCHA
def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Initialize session state variables
if "captured_image" not in st.session_state:
    st.session_state["captured_image"] = None
if "captcha" not in st.session_state:
    st.session_state["captcha"] = None
if "verified" not in st.session_state:
    st.session_state["verified"] = False  # Track if user is verified

# If the user is verified, show the welcome screen
if st.session_state["verified"]:
    st.title("🎉 Welcome Screen 🎉")
    st.success("Face and CAPTCHA verified! You are now authenticated.")
    st.stop()  # Stop execution to prevent showing the rest of the UI

# Main screen
st.title("Facial Recognition CAPTCHA Verification")
st.write("Please allow webcam access to proceed.")

# Capture button
if st.button("Capture & Verify Face", key="capture_button"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        st.session_state["captured_image"] = frame
    else:
        st.error("Failed to capture image.")

# If image is captured, process it
if st.session_state["captured_image"] is not None:
    captured_image = st.session_state["captured_image"]
    st.image(captured_image, channels="BGR", caption="Captured Image")

    captured_gray = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the captured image
    captured_faces = face_cascade.detectMultiScale(captured_gray, scaleFactor=1.3, minNeighbors=5)

    if len(captured_faces) > 0:
        st.success("Face detected! Verifying...")
        
        # Compare known face with captured face (Simple Matching)
        faces1 = face_cascade.detectMultiScale(known_face_gray, scaleFactor=1.3, minNeighbors=5)
        if len(faces1) > 0:
            st.success("Face recognized! Please solve the CAPTCHA to continue.")
            
            # Generate CAPTCHA if not already set
            if st.session_state["captcha"] is None:
                st.session_state["captcha"] = generate_captcha()

            st.write(f"**CAPTCHA: {st.session_state['captcha']}**")
            user_input = st.text_input("Enter CAPTCHA:", key="captcha_input")

            if user_input and user_input == st.session_state["captcha"]:
                st.session_state["verified"] = True  # Mark user as verified
                st.experimental_rerun()  # ✅ FIXED: Redirect to the welcome screen
            elif user_input:
                st.error("Incorrect CAPTCHA. ❌ Try again.")

        else:
            st.error("Face not recognized. ❌ Access denied.")
    else:
        st.error("No face detected. Please try again.")
