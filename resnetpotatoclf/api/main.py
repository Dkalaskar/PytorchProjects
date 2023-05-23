from fastapi import FastAPI, File, UploadFile
import torch as nn
import torch
import os
import torchvision.models as models
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import torchvision.transforms as transforms
from torchvision.models import resnet18
import uvicorn
import torch.functional as F


#Load Model
model = resnet18(num_classes = 3)
model.load_state_dict(torch.load('D:/PytorchProjects/resnetpotatoclf/traning/resnetpotato.pth'))
model.eval()




app = FastAPI()
@app.get("/ping")
async def ping():
    return "hello world"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file)
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=10),
        
        transforms.Normalize([0.4983, 0.5114, 0.4322], [0.2193, 0.2037, 0.2456])
    ])
    image = transform(image).unsqueeze(0)
    
    #perform predication
    with torch.no_grad():
        output = model(image)
        probilities = torch.nn.functional.softmax(output, dim=1)[0]
        
        #Get the class as per your image 
        #provied list of the claase
        labels = ['Early_blight','Late_blight','Healthy']
        
        predicted_class_index = torch.argmax(probilities).item()
        
        predicted_class = labels[predicted_class_index]
        
        confndence = probilities[predicted_class_index].item()
        
        return {"predicted class":predicted_class, "confidence":confndence}
    
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)






