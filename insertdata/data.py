import face_recognition
from os import path
while True:
    path_to_img=input('Nhập vào đường dẫn của hình ảnh :')
    if(path.exists(path_to_img)):
        try:
            img = face_recognition.load_image_file(path_to_img)
            break
        except:
            print("lỗi mã hóa khuôn mặt, vui lòng nhập lại đường dẫn ảnh :")
img_ecoding = face_recognition.face_encodings(img)[0]
img_name=path.basename(path_to_img).split('.')[0]
print(f',"{img_name}":{img_ecoding}')
