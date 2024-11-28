import pandas as pd
import os

def students_in_certain_university(data_folder):
    # List to store all dataframes
    all_data = []
    
    # Read all CSV files from the data folder in chronological order
    csv_files = sorted([f for f in os.listdir(data_folder) if f.endswith('.csv')], 
                      key=lambda x: x.split('-')[1])  # Sort by the year portion
    
    # Read files in order
    for filename in csv_files:
        if filename.endswith('.csv'):
            # Extract year from filename (e.g., 'master-12-13.csv' -> '12-13')
            year = filename.split('-')[1] + '-' + filename.split('-')[2].replace('.csv', '')
            
            file_path = os.path.join(data_folder, filename)
            df = pd.read_csv(file_path)
            # Convert 'Total' column to numeric, replacing non-numeric values with 0
            df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
            # Add year column to the dataframe
            df['year'] = year
            all_data.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Filter for Johns Hopkins University
    jhu_df = combined_df[combined_df['Institution name'] == 'Florida State University']
    
    # First, show total graduates per year
    yearly_totals = jhu_df.groupby('year')['Total'].sum()
    
    # Calculate average number of graduates per year
    avg_graduates = yearly_totals.mean()
    
    print("Yearly Student Totals at Johns Hopkins:")
    print(yearly_totals)
    print("\nAverage Number of Students per Year:")
    print(avg_graduates)
    
    print("\nBreakdown by CIP Code for each year:")
    # Group by year and CIP code to show detailed breakdown
    detailed_breakdown = jhu_df.groupby(['year', 'CIP Code'])['Total'].sum().reset_index()
    
    # Display breakdown for each year
    for year in sorted(detailed_breakdown['year'].unique()):
        print(f"\nYear {year}:")
        year_data = detailed_breakdown[detailed_breakdown['year'] == year]
        for _, row in year_data.iterrows():
            print(f"CIP {row['CIP Code']}: {int(row['Total'])}")

    return yearly_totals, avg_graduates, detailed_breakdown

# Example usage
if __name__ == "__main__":
    data_folder = "data"  # Path to your data folder
    students_in_certain_university(data_folder)
