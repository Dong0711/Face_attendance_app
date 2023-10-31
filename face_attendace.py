

import cv2
import face_recognition as fr
from database_layer import DataBase
import os
import numpy as np
import json



class face_recognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_ID = []
        self.data=DataBase()
        self.load_data()
        self.registered_names=set()
        pass

    def load_data(self):
        # query = "select mssv,linkanh from thong_tin_sv"
        # know_faces=self.data.execute_query(query)
        # for row in know_faces:
        #     image = fr.load_image_file(
        #         os.path.join("D:\FaceAttendace\images", row[1])
        #     )
        #     self.known_face_encodings.append(fr.face_encodings(image)[0])
        #     self.known_face_ID.append(str(row[0]))
        with open('data.json', 'r') as f:
            data=json.load(f)
        for key, value in data.items():
            self.known_face_encodings.append(np.array(value))
            self.known_face_ID.append(key) 

    def get_processed_frame(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(
            rgb_small_frame, face_locations
        )

        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):
            matches = fr.compare_faces(
                self.known_face_encodings, face_encoding
            )
            face_distances = fr.face_distance(
                self.known_face_encodings, face_encoding
            )
            best_match_index = np.argmin(face_distances)
            name = "Unknown"
            if matches and face_distances[best_match_index]<0.4:
                # first_match_index = matches.index(True)
                
                name = self.known_face_ID[best_match_index]
            color = (0, 0, 0)
            if name != "Unknown":
                color = (255, 0, 0)
                self.registered_names.add(name)
                name=name+ 'successful'
            else:
                color = (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            # Draw a label with a name below the face
            cv2.rectangle(
                frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED
            )
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1
            )
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (311, 311))
        return frame
    def return_name(self):
        return self.registered_nam
