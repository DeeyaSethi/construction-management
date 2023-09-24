# pip install ultralytics
import torch
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO  
import os
import cv2
# model = YOLO()

# path = 'C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/SafetyOfWorkers/yolov8n.pt'
# torch.save(model.state_dict(), path) 
# model.load_state_dict(torch.load(path))  # Loading the trained weights into model

# model.eval()
def predicted_output(input_image):
    input_image = 'C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/updated-constructionmanagement-backend/construction-management/static/SafetyOfWOrkersFinal/SafetyOfWorkers/sample.jpg'
    # input_image = cv2.imread('C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/updated-constructionmanagement-backend/construction-management/static/SafetyOfWOrkersFinal/SafetyOfWorkers/sample.jpg')
    model = YOLO('C:/Users/SUKHMANI KAUR/Desktop/Projects/SIH/updated-constructionmanagement-backend/construction-management/static/SafetyOfWOrkersFinal/runs/detect/train/weights/best.pt')
    results = model.predict(input_image, save=True)
    final = results
    return results
