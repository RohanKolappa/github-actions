import pandas as pd

def clean_data(input_file, output_file):
    # Read input file
    df = pd.read_csv(input_file)
    
    # Clean data (dropping missing values)
    df_cleaned = df.dropna()
    
    # Save cleaned data to output file
    df_cleaned.to_csv(output_file, index=False)
    print("Data cleaned")
    return "Data cleaned successfully!"

