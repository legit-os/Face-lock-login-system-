from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import cv2


mtcnn = MTCNN(select_largest=True,)
resnet = InceptionResnetV1(pretrained="vggface2").eval()

embeddings = torch.load(r"D:\face_lock\emb.pt")

cap = cv2.VideoCapture(0)


def cosine_sim(in_tensor, l = embeddings):
    sim_list = []
    for tensor in l:
        sim_list.append(torch.nn.functional.cosine_similarity(tensor.flatten(),in_tensor.flatten(),dim=0))
        
    return sim_list
    
while True:
    status, frame = cap.read()
    if not status:
        break
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break
    
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cropped, prob = mtcnn(frame.reshape((1,480,640,3)),return_prob=True)
            
        if cropped is not None:
                # print(cropped[0])
            try:
                emb = resnet(cropped[0].unsqueeze(dim=0))
                similarity_list = cosine_sim(in_tensor=emb)
                
                print(max(similarity_list))
                if max(similarity_list) > 0.99:
                    break
                
                    
            except Exception as e:
                continue
    
    

cap.release()
cv2.destroyAllWindows()

