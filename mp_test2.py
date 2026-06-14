import mediapipe as mp

try:
    import mediapipe.python.solutions.hands as hands
    print("SUCCESS")
    print(hands)
except Exception as e:
    print("ERROR:", e)