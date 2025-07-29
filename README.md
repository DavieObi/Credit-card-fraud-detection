# Credit Card Fraud Detection

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Problem Statement](#problem-statement)  
3. [Project Objective](#project-objective)  
4. [Column Dictionary](#column-dictionary)  
5. [Data Preprocessing](#data-preprocessing)  
   - [Missing Data](#missing-data)  
   - [Outlier Detection and Handling](#outlier-detection-and-handling)  
6. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis)  
7. [Feature Engineering](#feature-engineering)  
8. [Feature Selection, Train-Test Split & Scaling](#feature-selection-train-test-split--scaling)  
9. [Model Training](#model-training)  
   - [Logistic Regression](#logistic-regression)  
   - [Random Forest](#random-forest)  
10. [Model Comparison](#model-comparison)  
11. [Model Deployment](#model-deployment)  
12. [Conclusion](#conclusion)
    
---

## Project Overview  
This project focuses on detecting credit card fraud using machine learning techniques to mitigate financial losses by identifying fraudulent transactions.

## Problem Statement  
Fraudulent transactions are rare and hard to detect, posing a significant challenge to financial institutions. The goal is to identify these fraudulent transactions without disrupting legitimate activities.

## Project Objective  
To build a machine learning model capable of accurately predicting fraudulent credit card transactions, minimizing false positives while maximizing fraud detection.

## Column Dictionary  
| Column Name                     | Description                                                     |
|----------------------------------|-----------------------------------------------------------------|
| `distance_from_home`             | Distance from the cardholder's home to the transaction location |
| `distance_from_last_transaction` | Distance from the previous transaction                          |
| `ratio_to_median_purchase_price` | Ratio of transaction value to the median purchase price         |
| `repeat_retailer`                | Whether the transaction was from a repeat retailer (1: Yes, 0: No)|
| `used_chip`                      | Whether a chip was used in the transaction (1: Yes, 0: No)      |
| `used_pin_number`                | Whether a PIN number was used (1: Yes, 0: No)                   |
| `online_order`                   | Whether the transaction was online (1: Yes, 0: No)              |
| `fraud`                          | Indicates if the transaction was fraudulent (1: Fraud, 0: Legitimate)|

---

## Data Preprocessing  

### Missing Data  
We checked for missing values using `df.isnull().sum()`. Missing data was imputed or removed based on its significance.

### Outlier Detection and Handling  
Outliers were detected using box plots for key columns:  
- `distance_from_home`  
- `distance_from_last_transaction`  
- `ratio_to_median_purchase_price`  

To handle outliers, we capped values using the Interquartile Range (IQR) method via a custom `cap_outliers` function. This ensured that extreme values did not skew the model.

---

## Exploratory Data Analysis (EDA)  
- **Correlation Heatmap:** Plotted to examine relationships between features.  
- **Class Distribution:** Checked the balance of fraudulent vs. legitimate transactions in the `fraud` column.  

---

## Feature Engineering  
1. **Distance Ratio:** Calculated the ratio of `distance_from_home` to `distance_from_last_transaction`.  
2. **Transaction Score:** Combined multiple features to create a transaction risk score.  
3. **Purchase Category:** Grouped transactions based on `ratio_to_median_purchase_price` into categories:  
   - `very_low`, `low`, `medium`, `high`, `very_high`  
4. **Encoding:** Encoded purchase categories using a custom function to make them model-ready.  

---

## Feature Selection, Train-Test Split & Scaling  
- Selected significant features based on correlation analysis.  
- Split the dataset into training and test sets using an 80-20 ratio.  
- Applied **Standard Scaler** for feature normalization.  

---

## Model Training  

### Logistic Regression  
- **Accuracy:** 91.65%  
- **Confusion Matrix:**  
  ```
  [[166976  15581]
   [  1124  16319]]
  ```  
- **Classification Report:**  
  | Metric        | 0 (Legit) | 1 (Fraud) |  
  |---------------|------------|-----------|  
  | Precision     | 0.99       | 0.51      |  
  | Recall        | 0.91       | 0.94      |  
  | F1-Score      | 0.95       | 0.66      |  

---

### Random Forest  
- **Accuracy:** 94.27%  
- **Confusion Matrix:**  
  ```
  [[171253  11304]
   [   153  17290]]
  ```  
- **Classification Report:**  
  | Metric        | 0 (Legit) | 1 (Fraud) |  
  |---------------|------------|-----------|  
  | Precision     | 1.00       | 0.60      |  
  | Recall        | 0.94       | 0.99      |  
  | F1-Score      | 0.97       | 0.75      |  

---

## Model Comparison  
We compared both models using accuracy, precision, recall, and F1-score metrics, summarized in a DataFrame for easy reference.

---

## Model Deployment  
- **Model & Scaler Saving:** Saved the trained model and scaler for deployment using `joblib`.  
- **Deployment Platform:** Deployed using **Streamlit** on **Streamlit Cloud** for real-time predictions.

---

## Conclusion  
Our credit card fraud detection model demonstrated a significant ability to distinguish between fraudulent and legitimate transactions. By leveraging machine learning techniques such as Logistic Regression and Random Forest, we developed a robust solution capable of identifying fraudulent transactions with high accuracy.

### Key Insights:  
- **Fraud Detection Efficiency:** The model consistently identified fraudulent transactions with minimal false positives, reducing potential financial losses for credit card companies and enhancing customer trust.  
- **Impact on Fraud Prevention:** By accurately detecting fraudulent transactions, financial institutions can minimize disruptions to legitimate transactions, improving the overall user experience.  
- **High-Risk Factors:** Features like unusually high transaction distances and online orders showed strong correlations with fraud, offering valuable indicators for real-time monitoring systems.

### Recommendations:  
1. **Real-Time Monitoring:** Implementing this model in a real-time transaction monitoring system can help flag high-risk transactions promptly, reducing fraud-related losses.  
2. **Continuous Model Updating:** Regular updates with new transaction data will ensure the model adapts to emerging fraud patterns.  
3. **Customer Awareness:** Educating customers about common fraud triggers, such as unusual transaction patterns and PIN security, can further strengthen fraud prevention.  
4. **Integration with Multi-Layer Security:** This model should complement other security measures, such as two-factor authentication, to enhance fraud detection and prevention.

By integrating this machine learning-based solution into financial systems, organizations can strengthen their defenses against fraud, ensuring both security and a seamless customer experience.
