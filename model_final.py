import pandas as pd
import math
import pickle
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('TV.csv')

brand_labelencoder = LabelEncoder()
speaker_labelencoder = LabelEncoder()
size_labelencoder = LabelEncoder()
hd_labelencoder = LabelEncoder()
rating_scaler = StandardScaler()

dataset.iloc[:,0]=brand_labelencoder.fit_transform(dataset.iloc[:,0])
dataset.iloc[:,1]=rating_scaler.fit_transform(dataset.iloc[:,1].values.reshape(-1, 1))
dataset.iloc[:,2]=speaker_labelencoder.fit_transform(dataset.iloc[:,2])
dataset.iloc[:,3]=size_labelencoder.fit_transform(dataset.iloc[:,3])
dataset.iloc[:,4]=hd_labelencoder.fit_transform(dataset.iloc[:,4])

x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

col_transformer = ColumnTransformer(transformers=[('ohe', OneHotEncoder(), [0,2,3,4,5,6])],remainder='passthrough')
x= col_transformer.fit_transform(x)
x=x.todense()
scaler_y = StandardScaler()
y=scaler_y.fit_transform(y.values.reshape(-1, 1))

def output(brand,hd,hdmi,rating,size,speaker,usb):
    topredict=[[brand,hd,hdmi,rating,size,speaker,usb]]
    temp=pd.DataFrame(topredict)
    temp.columns=['Brand','Ratings','Speaker','Size','HD','HDMI','USB']
    temp.iloc[:,0]=brand_labelencoder.transform(temp.iloc[:,0])
    temp.iloc[:,1]=rating_scaler.transform(temp.iloc[:,1].values.reshape(-1, 1))
    temp.iloc[:,2]=speaker_labelencoder.transform(temp.iloc[:,2])
    temp.iloc[:,3]=size_labelencoder.transform(temp.iloc[:,3])
    temp.iloc[:,4]=hd_labelencoder.transform(temp.iloc[:,4])
    temp=col_transformer.transform(temp)
    temp=temp.todense()
    model = pickle.load(open("saved_model",'rb'))
    y_pred = model.predict(temp)
    y_pred = scaler_y.inverse_transform(y_pred)
    return round(y_pred[0])

if __name__ == '__main__':
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    regressor = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    regressor.fit(x_train, y_train.ravel())
    y_pred = regressor.predict(x_test)
    y_pred_acc=scaler_y.inverse_transform(y_pred)
    y_test_acc=scaler_y.inverse_transform(y_test)
    from sklearn.metrics import mean_squared_error
    print('RMSE is {}'.format(math.sqrt(mean_squared_error(y_test_acc, y_pred_acc))))

    pickle.dump(regressor, open("saved_model",'wb'))