import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self,num_features):
        self.num_features = num_features
        self.W = np.random.randn(num_features,1)
        self.b = np.random.randn()
        return W,b
    def generate_example(self,W,b,num=1000):
        self.x = np.random.randn(num,2)
        self.y = b + np.dot(x,w) + np.random.randn()
        return x,y
    def forward_pass(self,x):
        y = self.b + np.dot(X,self.W)
        return y
    def compute_loss(self,y_hat,y_true):
        loss = np.sum(np.square(y_hat-y_true))
        return loss/(2*y.shape[0])
    def backward_pass(self,x,y_true,y_hat):
        m = y_hat.shape[0]
        db = np.sum(y_hat-y_true)/m
        dW = np.sum(np.dot(np.transpose(y_hat-y_true)))
        return db,dW
    def update_params(self,dW,db,lr):
        self.W = self.W -lr*np.reshape(dW , (self.num_features,1))
        self.b = self.b - lr * db
    def train(self,x_train,y_train,iterations,lr):
        losses=[]
        for i in range(iterations):
            y_hat = self.forward_pass(x_train)
            dW,db = self.backward_pass(x_train,y_train,y_hat)
            self.update_params(dW,db,lr)
            loss = self.compute_loss(y_hat,y_train)
            losses.append(loss)
            if i % 100==0:
                print('Iter : {}, current Loss : {.4f}'.format(i,loss))
        return losses
model = Model(2)
x_train,y_train = model.generate_example()
losses = model.train(x_train,y_train,1000,3e-3)
plt.plot(range(1000),losses)
