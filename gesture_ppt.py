import cv2
import mediapipe as mp
import pyautogui
import time

# -----------------------------
# MediaPipe Hands setup
# -----------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # track only 1 hand
mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Make camera window resizable and always on top
cv2.namedWindow("Gesture Controlled Slides", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Gesture Controlled Slides", cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow("Gesture Controlled Slides", 400, 300)  # small corner window

# -----------------------------
# Variables for gesture detection
# -----------------------------
prev_x = 0
gesture_time = 0  # cooldown (1 second)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    success, img = cap.read()
    if not success:
        break

    # Flip image horizontally (mirror view)
    img = cv2.flip(img, 1)

    # Convert BGR to RGB (MediaPipe needs RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on screen
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get x coordinate of index finger tip (landmark 8)
            x = hand_landmarks.landmark[8].x * img.shape[1]

            # Gesture detection with cooldown
            if time.time() - gesture_time > 1:  # 1 sec cooldown
                if prev_x != 0:
                    if x - prev_x > 100:  # moved right
                        pyautogui.press("right")
                        print("Next Slide →")
                        gesture_time = time.time()
                        cv2.putText(img, "Next Slide →", (50,50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                    elif prev_x - x > 100:  # moved left
                        pyautogui.press("left")
                        print("Previous Slide ←")
                        gesture_time = time.time()
                        cv2.putText(img, "Previous Slide ←", (50,50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            prev_x = x

    # Show camera feed
    cv2.imshow("Gesture Controlled Slides", img)

    # Exit on Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
