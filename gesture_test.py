import cv2
from modules.hand_tracker import HandTracker
from modules.gesture import GestureDetector

tracker = HandTracker()
detector = GestureDetector()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hands = tracker.process(frame)
    states = detector.update(hands)

    for state in states:
        print(
            f"Phase={state.phase.name} "
            f"Charge={state.charge:.2f}",
            end=" | "
        )

    print(" " * 20, end="\r")

    cv2.imshow("Gesture Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()