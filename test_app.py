import os
from app import clean_data

def test_clean_data():
    # Prepare test input and output file paths
    input_file = 'test_input.csv'
    output_file = 'test_output.csv'
    
    # Create a sample input CSV file
    with open(input_file, 'w') as f:
        f.write('id,name,age\n1,Alice,25\n2,Bob,\n3,Charlie,30')
    
    # Run the cleaning function
    result = clean_data(input_file, output_file)
    
    # Check if output file is created
    assert os.path.exists(output_file)
    
    # Check if the data is cleaned correctly
    with open(output_file, 'r') as f:
        data = f.read()
        assert '2,Bob,' not in data
   
    print(output_file) 
    # Clean up
    os.remove(input_file)
    os.remove(output_file)

