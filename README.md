# Smoking-Detection-Using-YOLO-V5

## Steps :
**1. Cloning repository for YoloV5**
```
!git clone https://github.com/ultralytics/yolov5
```
**2. Installing dependencies**
```
pip install -r requirements.txt
```
**3. Create annotations for a custom dataset Using the LabelImg tool**

![This is an image](./images/git.png)

**4. Creating YAML file for training**

We specify:
- Our training and validation dataset directory location.
- The number of classes we want to detect.
- The name of our class

**5. Training**
I used Google Colab GPU
```
!python train.py --img 640 --batch 12 --epochs 60 --data smoke.yaml --cfg models/yolov5s.yaml --name wm
```
**6. Inference**
```
!python detect.py --img 640 --source ../smallTest/ --weights runs/train/wm/weights/best.pt --conf-thres 0.4
```
## Result :
Here is the result of the inference on some images :

![This is an image](./images/2.png)
![This is an image](./images/3.png)
![This is an image](./images/5.png)
