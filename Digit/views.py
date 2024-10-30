from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import torch
import torch.nn as nn
import torchvision
import torch.nn.functional as F
from PIL import Image 
# Create your views here.
import urllib.request
from io import BytesIO
from Digit.Digit_test import *

@api_view(["POST"])
def digit_reg(req):
    img=req.body
    img=json.loads(img)
    response = urllib.request.urlopen(img['imageUrl']['url'])
    print()
    img=BytesIO(response.file.read())
    # print(img['imageUrl']['url'])
    transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Grayscale(),
    torchvision.transforms.Resize(28)
    ])
    predition=predict(img)
    return Response({ "prediction": predition[0], "probability": predition[1]})