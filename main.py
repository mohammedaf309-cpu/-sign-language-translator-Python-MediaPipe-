import cv2
import mediapipe as mp

print("مرحبا - مشروع ترجمة لغة الاشارة اشتغل!")

# دي البداية - بعد كده هنضيف تتبع الايد
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

print("MediaPipe جاهز!")
