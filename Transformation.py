import numpy as np
#sample_data
X_train= np.array([10,20,30,40,50,60,70,80,90])
X_test= np.array([7,15,23,34,45,66,17,83,49])
def mean(x):
    print('Type of X :',type(x))
    Mean_x= np.sum(x)/len(x)
      #Here, I am just trying to check your code vs Numpy 
    print('Check your Mean  :',Mean_x-np.mean(x),' The Answer should be 0 ')
    return  Mean_x
def std(x):
    print('Mean of X :',mean(x))
    std_x =(np.sum((x-mean(x))**2)/len(x))**0.5
  #check your code vs Numpy 
    print('Check your Standard Deviation  :',std_x-np.std(x),' The Answer should be 0 ')
    return std_x 
def StandardScalertransform(x):
    return (x-mean(x))/std(x)
StandardScalertransform(X_train)
Scaled=StandardScalertransform(X_train)
print(Scaled)
('Check your Result here :',np.std(Scaled) ,' The Answer Should  be equal to 1.0')
def minMaxScaler(x):
    return (x-min(x))/(max(x)-min(x))
mm=minMaxScaler(X_train)
print(mm)
print('to Check if you are right :-\n' ' The Minimum ',np.min(mm),'The Value should be 0\n', 'The Maximum ' ,np.max(mm), ' The Value should be 1 ')
