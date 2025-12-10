# FACE LOCK using MTCNN and InceptionResnetV1 (vggface)

### This program keeps 10 photos as embeddings and calculates similarity for each image captured in a video.

## How to Use

1. Clone this repo

2. Run face_hash.py and click "c" on keyboard to capture your photos from different angles (10 times).

3. Add a bin or bat file in PATH which runs the command "uv run path/to/detection.py" to run this 
program on every startup.

---
### Detection is different thing and Face Lock is different, face lock is done with infrared cameras

1. 3d representation of the face is captured in that process.

2. Since landmarks are perfectly detected, and simple photo or video can't be used to trick the algorithm.

3. Liveliness of the person is also a part in that case.

### My project aims to use the accuracy of the pretrained face detection models to implement them in this type of projects confirming there ability to make perfect embeddings for human face that general cnn models can't do.




