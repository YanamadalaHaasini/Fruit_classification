
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Fruit Classification System",
    page_icon="🍎",
    layout="centered"
)

st.title("🍎 Fruit Classification System")
st.write("Predict a fruit using its physical characteristics.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("fruit.csv")

df = load_data()

features = ["weight", "width", "height", "color_score"]
X = df[features]
y = df["fruit_name"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

@st.cache_resource
def train_model(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

model = train_model(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

st.subheader("Enter Fruit Characteristics")

weight = st.number_input("Weight", min_value=0.0, value=1.0, step=0.1)
width = st.number_input("Width", min_value=0.0, value=2.0, step=0.1)
height = st.number_input("Height", min_value=0.0, value=1.0, step=0.1)
color_score = st.number_input(
    "Color Score", min_value=0.0, value=2.0, step=0.1
)

if st.button("Predict Fruit", type="primary"):
    input_data = pd.DataFrame(
        [[weight, width, height, color_score]],
        columns=features
    )

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Fruit: {prediction} 🍓")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        st.write("Prediction probabilities:")
        st.bar_chart(
            pd.DataFrame({
                "Fruit": model.classes_,
                "Probability": probabilities
            }).set_index("Fruit")
        )

with st.expander("Model Information"):
    st.write("Algorithm: Random Forest Classifier")
    st.write(f"Test-set accuracy: {accuracy:.2%}")
    st.write("Features: Weight, Width, Height, Color Score")
    st.write("Classes:", ", ".join(sorted(y.unique())))

st.caption(
    "Educational demo. Predictions depend on the quality and size "
    "of the training dataset."
)
