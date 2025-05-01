# app/model/style_transfer.py
import torch
from torchvision import transforms
from PIL import Image
import torchvision.models as models
import copy

def image_loader(image_path, imsize):
    loader = transforms.Compose([
        transforms.Resize(imsize), 
        transforms.ToTensor()
    ])
    image = Image.open(image_path)
    image = loader(image).unsqueeze(0)
    return image.to(torch.float)

def run_style_transfer(content_img, style_img, model):
    # For simplicity: use torch.hub
    import torch.nn as nn
    import torch.optim as optim

    cnn = models.vgg19(pretrained=True).features.eval()
    cnn = cnn.to(torch.float)

    # You can plug in more sophisticated NST here
    # Placeholder: return content_img for now
    return content_img
