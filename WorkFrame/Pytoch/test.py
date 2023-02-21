import torch

scalar1 = torch.tensor([1.])
print(scalar1)

scalar2 = torch.tensor([3.])
scalar1+scalar2

torch.add(scalar1,scalar2)
torch.sub(scalar1,scalar2)
torch.mul(scalar1,scalar2)
torch.div(scalar1,scalar2)

vector1 = torch.Tensor([1,2,3])
vector1
vector2 = torch.Tensor([4,5,6])
vector2

torch.dot(vector1,vector2)


matrix1 = torch.tensor([[1,2],[3,4]])
matrix2 = torch.tensor([[5,6],[7,8]])
torch.mul(matrix1,matrix2)
torch.matmul(matrix1,matrix2)

tensor1 = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
tensor2 = torch.tensor([[[9,10],[11,12]],[[13,14],[15,16]]])


### Autograd
import torch
if torch.cuda.is_available():
    DEVICE = torch.device('cuda')
else:
    DEVICE = torch.device('cpu')

BATCH_SIZE = 64
INPUT_SIZE = 1000
HIDDEN_SIZE = 100
OUTPUT_SIZE = 10


x = torch.randn(BATCH_SIZE, INPUT_SIZE, device = DEVICE, dtype = torch.float, requires_grad=False)

y = torch.randn(BATCH_SIZE, OUTPUT_SIZE, device = DEVICE, dtype = torch.float, requires_grad=False)

w1 = torch.randn(INPUT_SIZE, HIDDEN_SIZE, device = DEVICE, dtype = torch.float, requires_grad=True)

w2 = torch.randn(HIDDEN_SIZE,OUTPUT_SIZE, device = DEVICE, dtype = torch.float, requires_grad=True)

learning_rate = 1e-6
for t in range(1,501):
    y_pred = x.mm(w1).clamp(min = 0).mm(w2)#딥러닝 예측값
    loss  = (y_pred - y).pow(2).sum() #손실함수
    if t % 100 == 0:
        print('Iteration: ', t, '\t', 'Loss: ', loss.item())
    loss.backward()
    with torch.no_grad():
        w1 -= learning_rate*w1.grad
        w2 -= learning_rate*w2.grad
        w1.grad.zero_()
        w2.grad.zero_()