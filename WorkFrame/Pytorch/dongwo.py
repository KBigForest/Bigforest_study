import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt


# %%
X = torch.Tensor([[1,1],[1,0],[0,1],[0,0]])
Y = torch.Tensor([[0],[1],[1],[0]])

# %%
class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        
        self.layer1 = nn.Sequential(
            nn.Linear(2,4,bias=True),
            nn.Sigmoid()
        )
        
        self.layer2 = nn.Sequential(
            nn.Linear(4,4, bias=True),
            nn.Sigmoid()
        )
        
        self.layer3 = nn.Sequential(
            nn.Linear(4,1, bias=True),
            nn.Sigmoid()
        )
    #순전파    
    def forward(self,x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        return out
# %%
total_epoch = 15000
learning_rate = 0.5


# %%
model = Network()
#이진분류 시 사용되는 loss function
lossfunc = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
epoch_array = list()
loss_array = list()

# %%

for epoch in range(total_epoch):
    optimizer.zero_grad()
    hypothesis = model(X)
    loss = lossfunc(hypothesis,Y)
    epoch_array.append(epoch)
    loss_array.append(loss.item())
    
    loss.backward()
    optimizer.step()
    
    if epoch%100 == 0:
        print(f'epoch: {epoch}, loss: {loss.item()}')


# %%
model.eval()
with torch.no_grad():
    input1 = torch.Tensor([[0,0],[0,1],[1,0],[0,1]])
    input2 = torch.Tensor([[0,1],[1,0],[0,1],[0,1]])
    input3 = torch.Tensor([[1,1],[0,0],[0,0],[0,1]])
    inputlist = [input1,input2,input3]
    for input in inputlist:
        out = model(input)
        print(input, '\n', out)
        print('-'*50)