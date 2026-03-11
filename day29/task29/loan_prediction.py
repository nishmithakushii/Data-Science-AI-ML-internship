import pandas as pd

# Load dataset
df = pd.read_csv("day29/task29/train.csv")

# Function to predict loan approval
def predict_loan(row):

    # Rule 1: Good credit history
    if row['Credit_History'] == 1:

        # Rule 2: Applicant income must be sufficient
        if row['ApplicantIncome'] > 2500:

            # Rule 3: Loan amount reasonable
            if row['LoanAmount'] < 200:
                return "Approved"
    
    return "Rejected"


# Apply prediction rules
df['Predicted_Loan_Status'] = df.apply(predict_loan, axis=1)

# Show predictions
print(df[['ApplicantIncome','LoanAmount','Credit_History','Predicted_Loan_Status']].head())

# Count approvals vs rejections
print("\nPrediction Summary:")
print(df['Predicted_Loan_Status'].value_counts())