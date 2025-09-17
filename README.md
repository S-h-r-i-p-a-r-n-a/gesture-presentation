# Gesture-Controlled Presentation Slides 🎤📊

Control your PowerPoint presentation **hands-free** using just your **hand gestures**!  
With this project, you can swipe your hand left/right in front of the webcam to move between slides.

---

## 🚀 Features
- Swipe **Right → Next Slide**
- Swipe **Left → Previous Slide**
- Works in **PowerPoint Slideshow Mode** (or any app that uses `←` / `→` keys).
- 1-second **cooldown** to avoid accidental multiple skips.
- Simple setup, no extra hardware needed (just your webcam).

---

## 🛠 Tech Stack
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) → webcam input
- [MediaPipe](https://developers.google.com/mediapipe) → hand tracking
- [PyAutoGUI](https://pyautogui.readthedocs.io/) → simulating keyboard presses

---

## 📂 Project Structure
gesture-presentation/

│── gesture_ppt.py # Main Python script
│── requirements.txt # Dependencies

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gesture-presentation.git
   cd gesture-presentation
pip install -r requirements.txt

---


##▶️ Usage
Open your PowerPoint in Slideshow Mode (F5).
Run the script:
    python gesture_ppt.py

Stand in front of the webcam and use gestures:

Swipe Right Hand → Right → Next Slide

Swipe Left Hand → Left → Previous Slide

Quit anytime by pressing Q.

---

🧑‍💻 How It Works

Captures webcam feed using OpenCV.

Tracks hand landmarks with MediaPipe.

Detects index finger movement across screen.

Sends → or ← keystroke with PyAutoGUI.

📝 Future Improvements

Add gesture for exit presentation.

Support multiple users.

Improve accuracy with gesture classification.

👨‍🏫 Use Cases

College / Office presentations

Touchless interaction demos

Cool ML project showcase

---

📜 License
This project is open-source under the MIT License.

