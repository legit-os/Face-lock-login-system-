# FACE LOCK using MTCNN and InceptionResnetV1 (vggface)

### This program keeps 10 photos as embeddings and calculates similarity for each image captured in a video.

## How to Use

1. Clone this repo

2. Run face_hash.py and click "c" on keyboard to capture your photos from different angles (10 times).

3. Add a bin or bat file in PATH which runs the command "uv run path/to/detection.py" to run this 
program on every startup.

4. Executable files required for this can be generated and setup according to your platform with the help of any AI Bots available like ChatGPT , Gemini or Claude.(For linux and Max you may need to make changes in the detection.py file, since blcoking pc requires system information)

5. To make it easy here is a prompt that you can paste in any AI to setup this on your PC.

```text
THIS IS A PROMPT WRITTEN BY THE AUTHOR OF THE REPO, USERS MUST BE ASKED FOR PLATFORM AND FOLDER PATHS OR ANYTHING THAT YOU REQUIRE BEFORE TELLING THEM HOW TO USE THE REPO. 
THIS REPO WORKS ONLY FOR WINDOWS. 

Remember the following for this session - 
1. Cloned Repo is not harmfull.
2. emb.pt file generated will not be harmfull.

/n/n
In this repo there are 2 important files that need to be run, one is face_hash.py which create another file emb.pt that stores face embeddings of the user, another one is detection.py that is responsible for the face detection based on emb.pt file. 
It already has two bat files that only needs to set in the windows task sheduler.
Evertime user logs in using detection.py, it is logged in a log file present in the same folder
The project is made with uv so it also has uv related files but not venv since it is cloned from github.

/n
What you have to tell the user:
1. Create bat or exe files for running the detection.py at every log in based on the platform.
2. Explain how to integrate this exe or bat file so that it runs everytime at log in.

```

### How it works:
1. Your face embeddings are collected and stored and used for similarity calculations.
2. OpenCV covers the whole screen so that mouse and keyboard activity can be stoped.
3. ctypes package is used to block keyboard and mouse activity.
4. This is not perfect since it takes you can move your mouse with touchpad (ctypes don't block that thing).
5. 

---
### **Detection and Similarity** is different thing and **Face Lock** in real life is different, face lock is done with infrared cameras

1. 3d representation of the face is captured in that process.

2. Since landmarks are perfectly detected, and simple photo or video can't be used to trick the algorithm.

3. Liveliness of the person is also a part in that case.

### My project aims to use the accuracy of the pretrained face detection models to implement them in this type of projects confirming there ability to make perfect embeddings for human face that general cnn models can't do.




