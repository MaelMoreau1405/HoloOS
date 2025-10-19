import cv2
import mediapipe as mp
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import threading, psutil, socket

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def is_hand_open(landmarks):
    tips = [8, 12, 16, 20]
    open_count = sum(1 for tip in tips if landmarks[tip].y < landmarks[tip - 2].y)
    return open_count >= 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system')
def system_info():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
    except:
        ip = "N/A"
    return jsonify({"cpu": cpu, "ram": ram, "ip": ip})

def video_loop():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    smooth_x, smooth_y = None, None
    alpha = 0.3  # léger lissage, réactif mais doux

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        h, w, _ = frame.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                state = "open" if is_hand_open(hand_landmarks.landmark) else "closed"
                wrist = hand_landmarks.landmark[0]
                x, y = int(wrist.x * w), int(wrist.y * h)
                if smooth_x is None:
                    smooth_x, smooth_y = x, y
                else:
                    smooth_x = int((1 - alpha) * smooth_x + alpha * x)
                    smooth_y = int((1 - alpha) * smooth_y + alpha * y)

                socketio.emit('hand_state', {'state': state, 'x': smooth_x, 'y': smooth_y})
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("HoloCam", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release(); cv2.destroyAllWindows()

if __name__ == '__main__':
    t = threading.Thread(target=video_loop, daemon=True)
    t.start()
    socketio.run(app, host='0.0.0.0', port=5000)