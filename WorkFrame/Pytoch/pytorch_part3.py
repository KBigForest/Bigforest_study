import torch
X = torch.Tensor(2,3)#임의의 2x3행렬 생성
X = torch.tensor([[1,2,3],[4,5,6]])

x= torch.tensor(data = [2.0, 3.0], requires_grad=True)
y = x**2
z = 2*y +3 
target = torch.tensor([2.0, 230])
loss = torch.sum(torch.abs(z-target))
loss.backward()
print(x.grad, y.grad, z.grad) #z= 2*x^2+3 식에서의 x에 대한 기울기를 구하는 코드

# %%
import torch 
import torch.nn as nn #인공신경망
import torch.optim as optim #경사하강법 알고리즘
import torch.nn.init as init #텐서 초기값
num_data = 1000
num_epoch =10000
x = init.uniform_(torch.Tensor(num_data, 1), -10, 10)#[1000, 1]행렬에 대해 -10에서 10으로 무작위 생성
noise = init.normal_(torch.FloatTensor(num_data, 1), std= 1)#노이즈 추가 이유 보통 센서나 관측에 들어오는 데이터는 노이즈가 추가된 상태로 들어오기 때문에 추가, 표준 정규분포를 따르는 [1000,1]모냥의 noise행렬임. mean = 0은 default갑
y = 2*x + 3
y_noise = 2*(x+noise)+3#관측치에 noise가 더해진 값으로 y_noise생성
model = nn.Linear(1, 1)#파이토치 선형회귀 
loss_function = nn.L1Loss()#L1손실은 xi-yi 절대값의 평균

optimizer = optim.SGD(model.parameters(), lr=0.05)#최적화함수 경사하강법을 적용하여 오차를 줄이고 최적의 가중치 편차를 근사하게 함. lr은 learning rate

label = y_noise
for i in range(num_epoch):
    optimizer.zero_grad()#지난번 계산했던 기울기를 초기화
    output = model(x)# 결과값을 선형회귀값에 집어넣고
    
    loss = loss_function(output, label) #손실함수의 계산 label은 y_noise 잔차 생성
    loss.backward() #잔차에 따른 가중치w, 편차b값의 계산
    optimizer.step() #인수로 들어간 model.parameters()에서 리턴되는 변수들의 기울기에 학습률 0.05을 곱하여 optimizer값을 빼주고 업데이트함.
    
    if i % 10 == 0:
        print(loss.data)
    param_list = list(model.parameters())
    print(param_list[0].item(), param_list[1].item())

    
# %%
import torch
import torch.nn as nn #인공신경망
import torch.optim as optim #경사하강법 알고리즘
import torch.nn.init as init #텐서 초기값
num_data = 1000 #데이터의 개수
num_epoch = 10000
#초기값 생성 x,값과 y_noise 생성

x = init.uniform_(torch.Tensor(num_data, 1), -10, 10)#[1000, 1]행렬에 대해 -10에서 10으로 무작
noise = init.normal_(torch.Tensor(num_data,1),mean= 0, std = 1)
y = 2*x + 3
y_noise = 2*(x+noise)+3

model = nn.Linear(1,1)#단순선형회귀 생성
loss_function = nn.L1Loss()#L1loss생성

optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

for i in range(num_epoch):
    optimizer.zero_grad()
    output = model(x)
    loss = loss_function(output, y_noise)
    loss.backward()
    optimizer.step() 
    
    print(f'손실값: {loss.data}')#손실값은 작을 수록 좋음
    param_list = list(model.parameters())
    print(f'가중치:{param_list[0]}, 상수항: {param_list[1]}')



# %%
import torch
import torch.nn as nn #인공신경망
import torch.optim as optim #경사하강법 알고리즘
import torch.nn.init as init #텐서 초기값
num_data = 1000 #데이터의 개수
num_epoch = 10000 
x= init.uniform_(torch.Tensor(num_data,1 ),-15, 15)
noise = init.normal_(torch.Tensor(num_data,1),mean= 0, std=1)
y= x**2 + 3
y_noise = y+noise

model = nn.Sequential(nn.Linear(1,6),nn.ReLU(),nn.Linear(6,10),nn.ReLU(),nn.Linear(10,6),nn.ReLU(),nn.Linear(6,1),nn.ReLU())

loss_function = nn.L1Loss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

loss_array = []

for i in range(num_epoch):
    optimizer.zero_grad()
    output = model(x)
    loss = loss_function(output, y_noise)
    loss.backward()
    optimizer.step()
    loss_array.append(loss)
    print(loss)

# %%
import matplotlib.pyplot as plt
plt.plot(loss_array)

