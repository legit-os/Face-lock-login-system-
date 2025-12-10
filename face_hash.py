from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torch import Tensor
device = "cpu"
import cv2
import numpy as np

mtcnn = MTCNN(select_largest=True,)
resnet = InceptionResnetV1(pretrained="vggface2").eval()

cap = cv2.VideoCapture(0)

embeddings = []

while True:
    status, frame = cap.read()
    if not status:
        break
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cropped, prob = mtcnn(frame.reshape((1,480,640,3)),return_prob=True)
        
        if cropped is not None:
            # print(cropped[0])
            try:
                emb = resnet(cropped[0].unsqueeze(dim=0))
                embeddings.append(emb)
                
            except Exception as e:
                # print(e)
                continue
        
        print(len(embeddings))
        
        if embeddings.__len__() == 10:
            break
        
    

cap.release()
cv2.destroyAllWindows()

torch.save(embeddings,"emb.pt")