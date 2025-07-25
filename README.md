#Healthcare Analysis
# 🏥 Healthcare Appointment No-Show Prediction

This project uses machine learning and data visualization to analyze and predict whether a patient will show up for their medical appointment. It helps hospitals reduce no-shows by identifying key patterns like age, SMS reminders, waiting days, and appointment day.

---

## 📌 Problem Statement

Missed appointments can cost hospitals both time and money. Using historical data, we aim to build a predictive model and explore key trends using Power BI.

---

## 🔧 Tools & Technologies Used

| Tool           | Purpose                        |
|----------------|--------------------------------|
| Python (pandas, seaborn, sklearn) | Data cleaning, EDA, model building |
| Power BI       | Data visualization & dashboard |
| Jupyter / IDLE | Code execution |
| scikit-learn   | ML Model (Decision Tree)       |

---

## 🧪 Steps Performed

1. **Data Cleaning** (null handling, datetime conversion)
2. **Feature Engineering** (`WaitingDays`, weekday, encoded labels)
3. **Modeling** with `DecisionTreeClassifier`  
   - Accuracy: **77.14%**
4. **Evaluation** using confusion matrix & classification report
5. **Power BI Dashboard**: Interactive visuals and filters

---

## 📊 Dashboard Insights

- ❌ **No-show rate**: ~20% overall
- ✅ **SMS Reminders**: Increase patient attendance
- 📅 **Weekdays**: Monday had highest no-shows
- ⏱️ **Waiting Time**: Longer waits = more no-shows
- 👩‍⚕️ **Age Factor**: Young adults and elderly miss more often

---

## 📁 Project Files

- `Hospital Model.py` – Python script for cleaning and modeling
- `cleaned_appointments.csv` – Cleaned dataset
- `Project Report.pdf` – Final 2-page summary report
- `Power BI Visuals` – Dashboard screenshots

---

## 🧠 Learnings

- Real-world healthcare data preprocessing
- Model evaluation & metric interpretation
- Storytelling through interactive dashboards

---

## 🔗 Project Preview

> Dashboard & results included in the PDF and images folder


