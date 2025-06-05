import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv('data/soil_crop_data.csv')

# Encode soil_type to numeric
data['soil_type'] = data['soil_type'].astype('category').cat.codes

X = data[['soil_type', 'ph', 'rainfall', 'temperature']]
y = data['crop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print("Model accuracy:", model.score(X_test, y_test))

joblib.dump(model, 'app/rf_model.joblib')
