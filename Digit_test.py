import torch
import torch.nn as nn
import torchvision
import torch.nn.functional as F
batch_size_test = 1000
from PIL import Image

# Read a PIL image + image->tensor(normalized)
image = Image.open('./image/2.png').convert('RGB')
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Grayscale(),
    torchvision.transforms.Resize(28)
])
img_tensor = transform(image)
img_tensor = img_tensor.to(torch.float)
mean= torch.mean(img_tensor)
std= torch.std(img_tensor)
normalize= torchvision.transforms.Normalize((mean),(std))
img_tensor= normalize(img_tensor)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x)
    
network= Net()
network.load_state_dict(torch.load('./results/model.pth', weights_only=True))

output = network(img_tensor)
print(output[0],format(torch.argmax(output[0])))