import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Appointments.csv')

# Display first few rows and column info
print(df.head())
print(df.info())

# ================================
# Data Cleaning & Feature Engineering
# ================================

# Convert dates to proper datetime format
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Create new column: WaitingDays = gap between scheduling and appointment
df['WaitingDays'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days

# Filter out invalid ages (negative or unrealistic)
df = df[(df['Age'] >= 0) & (df['Age'] <= 100)]

# Convert 'No-show' column: Yes → 1, No → 0
df['No-show'] = df['No-show'].map({'Yes': 1, 'No': 0})

# Drop unnecessary columns if present (safe drop)
df = df.drop(columns=['PatientId', 'AppointmentID'], errors='ignore')

# Extract weekday from appointment date
df['Weekday'] = df['AppointmentDay'].dt.day_name()

# Preview the cleaned data
print(df.head())

sns.histplot(data=df, x='Age', hue='No-show', bins=30, kde=True)
plt.title('Age vs No-show')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.legend(title='No-show (1 = Missed)')
plt.show()

sns.boxplot(data=df, x='No-show', y='WaitingDays')
plt.title('Waiting Days vs No-show')
plt.xlabel('No-show (1 = Missed)')
plt.ylabel('Waiting Days')
plt.show()

sns.barplot(data=df, x='SMS_received', y='No-show')
plt.title('SMS Reminder vs No-show Rate')
plt.xlabel('SMS Received (0 = No, 1 = Yes)')
plt.ylabel('Average No-show Rate')
plt.show()


sns.countplot(data=df, x='Weekday', hue='No-show', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
plt.title('No-show by Weekday')
plt.xlabel('Appointment Day')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.legend(title='No-show (1 = Missed)')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Define the features (input) and the target (output)
features = ['Age', 'WaitingDays', 'Scholarship', 'Hipertension', 'Diabetes',
            'Alcoholism', 'Handcap', 'SMS_received']
X = df[features]
y = df['No-show']



# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
print(" Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


df.to_csv("cleaned_appointments.csv", index=False)

