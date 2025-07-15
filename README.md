
# 🔐 VerifyMe.AI

> AI-powered CAPTCHA system using face and hand gesture recognition for secure human verification.

---

## 📌 Project Summary

**VerifyMe.AI** replaces traditional CAPTCHA methods with a smart, real-time human verification system. It uses webcam-based **face detection** and **hand gesture recognition** to ensure that only real users — not bots — pass through security checks.

This system is ideal for online exams, secure login systems, or kiosk-based public services. The user is asked to perform a random challenge (e.g., show 2 fingers and smile), and the system verifies both **face presence** and **gesture correctness**.

---

## 🎯 Key Features

- ✅ Detects and verifies human **face using Haar Cascades**
- ✋ Identifies **hand gestures** (1–5 fingers) using Mediapipe
- 🎥 Works in real-time using webcam
- 🔐 Enhanced security against bots and spoofing
- 💡 Can be extended to mobile, web, or kiosk systems

---

## 🧠 Real-World Applications

| Use Case | Examples |
|----------|----------|
| Online exam portals | Facial + gesture login for human candidates |
| Government portals | Secure public access (UIDAI, IRCTC, etc.) |
| Banking Kiosks | Face + hand check before e-KYC |
| Cybercafés | Prevent bots from auto-registering |

---

## 🛠️ Technologies Used

- **Python 3.8**
- **OpenCV** – for webcam and face detection
- **Mediapipe** – for hand landmark tracking
- **Haarcascade XML** – pre-trained face detection model
- **NumPy** – image/array operations

---

## 📁 Folder Structure

```
verifyme-ai/
├── app.py                        # Main script to run system
├── requirements.txt              # Dependencies list
├── LICENSE                       # MIT License
├── README.md                     # This file
│
├── haarcascades/
│   └── haarcascade_frontalface_default.xml
│
├── hand_module/
│   └── hand_gesture.py           # Hand gesture detection logic
│
├── assets/
│   └── bala.jpg                  # Test image or user sample
│
└── .venv/                        # Virtual environment (optional)
```

---

## 📥 Installation Guide

### ✅ Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/verifyme-ai.git
cd verifyme-ai
```

### ✅ Step 2: Create a Virtual Environment
```bash
python -m venv .venv
```

### ✅ Step 3: Activate the Environment

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```

### ✅ Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python app.py
```

1. The webcam will start.
2. The system will detect your **face** using Haar Cascade.
3. A random gesture challenge appears (e.g., "Show 3 fingers").
4. Mediapipe detects your hand and counts fingers.
5. If both checks pass → ✅ CAPTCHA Passed

---

## 🔍 How It Works (Flowchart)

```text
[ Webcam Feed ]
       ↓
[ Detect Face (Haar Cascade) ]
       ↓
[ Detect Hand (Mediapipe) ]
       ↓
[ Generate Random Gesture Challenge ]
       ↓
[ Match Face + Gesture ]
       ↓
[ Verification Success ]
```

---

## 🧪 Sample Challenge Logic (Python)
```python
import random
challenge = random.choice([1, 2, 3, 4, 5])
print(f"Show {challenge} fingers to continue")
```

---

## 💡 Example Code Snippet: Face Detection (OpenCV)

```python
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
```

---

## 🖐️ Example Code: Hand Landmark Detection (Mediapipe)

```python
with mp_hands.Hands() as hands:
    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        count_fingers(result.multi_hand_landmarks)
```

---

## 📷 Demo Preview 
![demo]<img width="1914" height="971" alt="image" src="https://github.com/user-attachments/assets/6b1eff39-6073-42e9-90ae-ad9816e78e14" />


---

## 🚀 Future Enhancements

- [ ] GUI using Tkinter or Streamlit
- [ ] Mobile version using MediaPipe on Android
- [ ] OTP fallback for invalid attempts
- [ ] Smile/blink detection (multi-modal verification)
- [ ] Voice command captcha support

---

## 👨‍💻 Author

**Balashanmugam**  
MSc Data Science | AI Enthusiast | Python Developer  
📧 balashanmugamrathinam@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/balashanmugamr/)

---

## 📝 License

This project is licensed under the [LICENSE](https://github.com/Balashanmugam-rathinam/VerifyMeAI/blob/main/LICENSE.txt).  
You are free to use, modify, and distribute this code for personal or commercial use.

---

> _“VerifyMe.AI: Making CAPTCHA smarter, not harder.”_
