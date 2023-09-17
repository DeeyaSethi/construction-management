# pip install ultralytics
import torch
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO  

# model = YOLO()

# path = 'C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/SafetyOfWorkers/yolov8n.pt'
# torch.save(model.state_dict(), path) 
# model.load_state_dict(torch.load(path))  # Loading the trained weights into model

# model.eval()

input_image = 'C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/SafetyOfWorkers/sample.jpg'

model = YOLO('C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/runs/detect/train/weights/best.pt')
results = model.predict('C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/SafetyOfWorkers/sample.jpg', save=True)
