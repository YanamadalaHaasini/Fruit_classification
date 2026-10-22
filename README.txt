# 🍎 Fruit Classification System Using Fruit Characteristics

## 📌 Project Overview
The Fruit Classification System is a Machine Learning project that predicts the type of fruit based on its physical characteristics. It uses a Random Forest Classifier to classify fruits into three categories: Apple, Banana, and Orange.

The system uses features such as weight, width, height, and color score to predict the fruit category.

## 🎯 Objectives
- To develop a machine learning model for fruit classification.
- To classify fruits based on their physical characteristics.
- To understand the implementation of the Random Forest Classification algorithm.
- To evaluate the model using classification metrics.

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Machine Learning

## 📊 Dataset Description
The dataset is stored in `fruit.csv` and contains the following features:

| Feature | Description |
|---|---|
| weight | Weight of the fruit |
| width | Width of the fruit |
| height | Height of the fruit |
| color_score | Color score of the fruit |
| fruit_name | Target fruit category |

**Fruit Categories:**
- Apple
- Banana
- Orange

*Note: The project uses a small demonstration dataset. Model performance on real-world fruit data may differ.*

## 🤖 Machine Learning Algorithm
**Random Forest Classifier**

Random Forest is a supervised machine learning algorithm that combines multiple decision trees to make predictions. It is used in this project to classify fruits based on the provided characteristics.

## 📈 Model Evaluation
The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

The initial test run reported **100% accuracy** on 20 test samples. This result applies only to the current dataset and does not guarantee the same performance on unseen real-world data.

## 💻 Project Structure

```text
fruit-classification-system/
│
├── app.py
├── fruit_classification.py
├── fruit.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/fruit-classification-system.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd fruit-classification-system
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## 🚀 Features
- Fruit classification using physical characteristics.
- Random Forest machine learning model.
- Interactive input fields for fruit characteristics.
- Prediction output through a Streamlit web application.
- Model performance information.

## 🔮 Future Enhancements
- Train the model using a larger, reliable fruit dataset.
- Improve model generalization and evaluation.
- Add fruit image classification using computer vision.
- Expand the application to support additional fruit categories.

## 👩‍💻 Author
**Lalitha Devi**

## 📄 License
This project is developed for educational and learning purposes.
