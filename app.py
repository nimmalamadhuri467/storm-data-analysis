# app.py
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
st.title("🌀 Hurricane Prediction System")
st.write("Predict whether a storm system is a **Hurricane** based on environmental factors.")

try:
    data = pd.read_csv("storms.csv")
    st.success("Dataset loaded successfully!")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

data['pressure'] = data['pressure'].replace(-999, pd.NA)
data['pressure'] = data['pressure'].fillna(data['pressure'].median())

hurricane_labels = ["HU", "HURRICANE", "Hurricane"]
data['target'] = data['category'].apply(lambda x: 1 if str(x).upper() in hurricane_labels else 0)

X = data[['year','month','day','hour','lat','long','wind','pressure']]
y = data['target']

X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(X.median())
hurricane_labels = ["HU", "HURRICANE", "Hurricane"]
data['target'] = data['category'].apply(lambda x: 1 if str(x).upper() in hurricane_labels else 0)
print(data['target'].value_counts())



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.sidebar.header("⚙️ Model Information")
st.sidebar.write(f"**Model Accuracy:** {accuracy:.2f}")

# -------------------- User Inputs --------------------
st.subheader("🌍 Enter Storm Parameters")
lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1)
long = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1)
wind = st.number_input("Wind Speed (knots)", min_value=0.0, max_value=200.0, step=1.0)
pressure = st.number_input("Pressure (mb)", min_value=800.0, max_value=1100.0, step=1.0)

if st.button("Predict Hurricane"):
    user_data = pd.DataFrame([[2025, 9, 12, 12, lat, long, wind, pressure]],
                             columns=['year','month','day','hour','lat','long','wind','pressure'])
    user_data_scaled = scaler.transform(user_data)
    prediction = model.predict(user_data_scaled)
    
    if prediction[0] == 1:
        st.error("⚠️ Hurricane predicted in this area!")
    else:
        st.success("✅ No hurricane predicted!")
