import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

path=r'D:\Python\08.07.2022forhome\Analysisofexp4'
expnum='5'
k=np.linspace(1,5,5)
#Open files
gamma=0.4
#Five files because there were five experiments (one glucose concentration relates to one experiment)
for j in range(1,len(k)+1):
    #Loading images (Nx1024x1280)
    globals()[f"img{j}"]=np.load(path+'\pctr'+expnum+str(int(k[j-1]))+'.npy')
    #Improving their contrast
    globals()[f"img{j}"] =(globals()[f"img{j}"]/255)**gamma#*255
    #Loading signals (N)
    globals()[f"sig{j}"] = np.load(path + '\signal' + expnum + str(int(k[j-1])) + '.npy')#'\maxsig'
#Make concentration files
conc=np.array([5.4,4.8,6.5,8.7,8.2])
for i in range(1,len(k)+1):
    globals()[f"con{i}"]=np.ones_like(globals()[f"sig{i}"])*conc[i-1]
#PCA of images
pca=PCA(27)
#pca=PCA(.95)
for i in range(1,len(k)+1):
    globals()[f"imgflat{i}"]=globals()[f"img{i}"].reshape([len(globals()[f"img{i}"][:]),-1])
    globals()[f"conv{i}"]= pca.fit_transform(globals()[f"imgflat{i}"])

#Unification (combining among all of experiments)
sigsum=globals()[f"sig{1}"]
convsum= globals()[f"conv{1}"]
concsum=globals()[f"con{1}"]
for i in range(2,len(k)+1):
    sigsum=np.concatenate((sigsum,globals()[f"sig{i}"]))
    convsum=np.concatenate((convsum,globals()[f"conv{i}"]))
    concsum=np.concatenate((concsum,globals()[f"con{i}"]))

#Creating of x and y
#In case of correlation between image+signal and glucose values
y=concsum
x=np.zeros((convsum.shape[0],convsum.shape[1]+1))
x[:,0]=sigsum
x[:,1:]=convsum
#In case of correlation between image and signal for one glucose value
# x=conv4
# y=sig4
#8.2 mmol/dl

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from sklearn import svm
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#Init models
pipelines = []
pipelines.append(('ScaledLR', Pipeline([('Scaler', StandardScaler()),('LR',LinearRegression())])))
pipelines.append(('ScaledLASSO', Pipeline([('Scaler', StandardScaler()),('LASSO', Lasso())])))
pipelines.append(('ScaledEN', Pipeline([('Scaler', StandardScaler()),('EN', ElasticNet())])))
pipelines.append(('ScaledKNN', Pipeline([('Scaler', StandardScaler()),('KNN', KNeighborsRegressor())])))
pipelines.append(('ScaledCART', Pipeline([('Scaler', StandardScaler()),('CART', DecisionTreeRegressor())])))
pipelines.append(('ScaledGBM', Pipeline([('Scaler', StandardScaler()),('GBM', GradientBoostingRegressor())])))
X_train, X_test, Y_train, Y_test = train_test_split (x, y, test_size = 0.10, random_state=42)
results = []
names = []
#Search for best model
for name, model in pipelines:
    kfold = KFold(n_splits=5, random_state=21,shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='r2')#'neg_mean_squared_error')#
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

from sklearn.model_selection import GridSearchCV
#Best parameters for best model
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
alphas = np.linspace(0.1,0.6, 10)
#alphas=np.logspace(-2.0, 2.0, num=10)
#param_grid  = {'alpha':alphas}#Elastic,Lasso,Regr
#param_grid = [{'n_neighbors': [2,3,4,5,6,7,8,9,10,11,12,13,14,15], 'weights': ['uniform','distance'],'p':[1,2,5]}]#Kneighb
param_grid = {'learning_rate': [0.01,0.004,0.1,0.4],
                  'subsample'    : [0.9, 0.8, 0.99, 0.1],

                 }
#model = Lasso()
#model=ElasticNet()
#model=KNeighborsRegressor()
model=GradientBoostingRegressor()
kfold = KFold(n_splits=5, random_state=21,shuffle=True)
grid = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=kfold)
grid_result = grid.fit(rescaledX, Y_train)

means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

from sklearn.metrics import mean_squared_error

scaler = StandardScaler().fit(X_train)
rescaled_X_train = scaler.transform(X_train)
#model = Lasso(alpha=0.04888)
#model = Lasso(alpha=0.32727)
#model=KNeighborsRegressor(n_neighbors=15,weights="distance",p=1)
model=GradientBoostingRegressor(learning_rate=0.01,subsample=0.9)
model.fit(rescaled_X_train, Y_train)

# transform the validation dataset
rescaled_X_test = scaler.transform(X_test)
predictions = model.predict(rescaled_X_test)
print (mean_squared_error(Y_test, predictions)/np.mean(Y_test))

print(predictions)
print(Y_test)