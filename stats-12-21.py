import pandas as pd

# Read the CSV file
df = pd.read_csv('data/master-20-21.csv')

# Group by institution and get their unique CIP codes
institution_programs = df.groupby('Institution name')['CIP Code'].unique()
print(institution_programs.count())
# Initialize lists for each category
geography_only = []
gis_only = []
both_programs = []

for institution, cip_codes in institution_programs.items():
    # Convert CIP codes to strings and remove any whitespace
    cip_codes = [str(code).strip() for code in cip_codes]
    
    has_geography = any('45.0701' in code for code in cip_codes)
    has_gis = any('45.0702' in code for code in cip_codes)
    
    if has_geography:
        if has_gis:
            both_programs.append(institution)
        else:
            geography_only.append(institution)
    elif has_gis:
        gis_only.append(institution)

print(f"\nNumber of institutions offering only Geography (45.0701): {len(geography_only)}")

print(f"\nNumber of institutions offering only GIS (45.0702): {len(gis_only)}")
print("\nInstitutions offering only GIS (45.0702):")
for inst in gis_only:
    print(f"- {inst}")

print(f"\nNumber of institutions offering both Geography and GIS: {len(both_programs)}")
print("\nInstitutions offering both Geography and GIS:")
for inst in both_programs:
    print(f"- {inst}")
