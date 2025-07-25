import pandas as pd
import dagster as dg

sample_data_file = "src/dagster_quickstart/defs/data/sample_data.csv"
processed_data_file = "src/dagster_quickstart/defs/data/processed_data.csv"
processed_excel_data_file = "src/dagster_quickstart/defs/data/processed_data.xlsx"


@dg.asset
def processed_data() -> str:
    # Read data from the CSV
    df = pd.read_csv(sample_data_file)

    # Add an age_group column based on the value of age
    df["age_group"] = pd.cut(
        df["age"], bins=[0, 30, 40, 100], labels=["Young", "Middle", "Senior"]
    )

    # Save processed data
    df.to_csv(processed_data_file, index=False)
    return "Data loaded successfully"


@dg.asset(deps=[processed_data])
def processed_excel_data() -> str:
    # Read data from the CSV
    df = pd.read_csv(processed_data_file)

    # Save processed data as excel
    df.to_excel(processed_excel_data_file, index=False)
    return "Data converted to excel successfully"
