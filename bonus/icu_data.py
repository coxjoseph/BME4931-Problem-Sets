import pandas as pd
import os

combined_data = pd.DataFrame(columns=["Patient_ID", "Time", "Parameter", "Value"])
data_directory = "./data"

# Loop through patient data files in the directory
for filename in os.listdir(data_directory):
    if filename.endswith(".txt"):
        patient_id = os.path.splitext(filename)[0]  # Extract the Patient_ID from the filename
        file_path = os.path.join(data_directory, filename)
        patient_data = pd.read_csv(file_path)

        # Add the Patient_ID to the patient data
        patient_data["Patient_ID"] = patient_id

        # Concatenate patient data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, patient_data], ignore_index=True)

# Export the combined data to a CSV file
combined_data.to_csv("patient_data.csv", index=False)

