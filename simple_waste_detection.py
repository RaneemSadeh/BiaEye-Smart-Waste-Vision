import cv2
from ultralytics import YOLO
import time

MODEL = YOLO("yolo11s.pt")
ZONE = [100, 100, 500, 400]
CONF = 0.4

cap = cv2.VideoCapture(0)
violation_count = 0

print("System Active. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    results = MODEL(frame, conf=CONF, verbose=False)
    
    cv2.rectangle(frame, (ZONE[0], ZONE[1]), (ZONE[2], ZONE[3]), (0, 255, 0), 2)
    
    for r in results:
        frame = r.plot() 
        
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            
            if ZONE[0] < cx < ZONE[2] and ZONE[1] < cy < ZONE[3]:
                violation_count += 1
                cv2.putText(frame, "", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.putText(frame, f"Violations: {violation_count}", (10, 450), #that is going to be for the ui
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Simple Waste Detect", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()