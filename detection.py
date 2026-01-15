# yeah you are most likely see how this file works so I added some comments so that you can get some of the things
# and you need to know about OpenCV and torch to understand logic here.



import ctypes                                 # absolutely dangerous package
import atexit                          


user32 = ctypes.windll.user32

def block_input():                        # block keyboard + mouse
    user32.BlockInput(True)

def unblock_input():                          # always unblock
    user32.BlockInput(False)

block_input()


from pathlib import Path
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import cv2
import time
import subprocess


atexit.register(unblock_input)


SIM_THRESHOLD = 0.78     # cosine similarity threshold
TIMEOUT = 15            # seconds before auto-fail
CAMERA_INDEX = 0


mtcnn = MTCNN(select_largest=True)
resnet = InceptionResnetV1(pretrained="vggface2").eval()


emb_path = Path("emb.pt")

if not emb_path.exists():
    exit(1)

embeddings = torch.load(emb_path.resolve())


def cosine_sim(in_tensor, stored_embeddings=embeddings):
    return [
        torch.nn.functional.cosine_similarity(
            emb.flatten(),
            in_tensor.flatten(),
            dim=0
        )
        for emb in stored_embeddings
    ]


def lock_pc():
    subprocess.run(
        "rundll32.exe user32.dll,LockWorkStation",
        shell=True
    )


WINDOW_NAME = "Face Verification"

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)


cv2.setWindowProperty(
    WINDOW_NAME,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)


cap = cv2.VideoCapture(CAMERA_INDEX)


for _ in range(10):
    status, _ = cap.read()
    if status:
        break


start_time = time.time()



######################## detection part from here
verified = False

while True:
    if time.time() - start_time > TIMEOUT:
        break

    status, frame = cap.read()
    if not status:
        break

    cv2.imshow("Face Verification", frame)

    
    # if cv2.waitKey(1) & 0xFF == 2:
    #     break


    cropped, prob = mtcnn(
        frame.reshape((1, frame.shape[0], frame.shape[1], 3)),
        return_prob=True
    )

    if cropped is None:
        continue

    try:
        emb = resnet(cropped[0].unsqueeze(0))
        similarity_list = cosine_sim(emb)

        max_sim = max(similarity_list)
        print(float(max_sim))

        if max_sim >= SIM_THRESHOLD:
            verified = True
            break

    except Exception:
        continue


cap.release()
cv2.destroyAllWindows()

if verified:
    exit(0)
else:
    lock_pc()
    exit(1)
