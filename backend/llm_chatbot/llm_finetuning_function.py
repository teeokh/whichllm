import pandas as pd

examples = {
    "Input": [

    ],
    "Output": [

    ]
}

# Convert the dictionary to a DataFrame
examples_df = pd.DataFrame(examples)

# Save the DataFrame to a CSV file
output_file_path = '/Users/terrellokhiria/CodingProjects/MyProjects/whichllm/backend/Training/WhichLLM_Use_Case_Examples{}.csv'
examples_df.to_csv(output_file_path, index=False)