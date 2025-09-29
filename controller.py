import cv2
import mediapipe as mp

class MediaPipeController:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.cap = cv2.VideoCapture(0)
        self.jump_detected = False
        self.prev_hip_y = None  

    def update(self):
        self.jump_detected = False

        ret, frame = self.cap.read()
        if not ret:
            return self.jump_detected

        frame = cv2.flip(frame, 1)  
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(rgb)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark

            hip_y = landmarks[24].y 

            if self.prev_hip_y is not None:
                if self.prev_hip_y - hip_y > 0.05: 
                    self.jump_detected = True

            self.prev_hip_y = hip_y  

        cv2.imshow("Mediapipe Jump Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()

        return self.jump_detected
