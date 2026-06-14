import cv2
from modules.hand_tracker import HandTracker

tracker = HandTracker()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hands = tracker.process(frame)

    print(f"Hands detected: {len(hands)}", end="\r")

    cv2.imshow("Hand Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()