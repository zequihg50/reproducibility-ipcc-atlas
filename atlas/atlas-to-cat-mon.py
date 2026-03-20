import pandas as pd

df = pd.read_csv('CMIP6_mon.csv')
variables = ['prsn', 'sfcWind', 'tos', 'ph', 'siconc']

ids = []

for _, row in df.iterrows():
    sim = row['dataset']
    parts = sim.split("_")
    inst = parts[1]
    model = parts[2]
    exp = parts[3] 
    act = "CMIP" if exp == "historical" else "ScenarioMIP"
    run = parts[4]
    freq = parts[5]
    grid = parts[6]

    for var in variables:
        if pd.isna(row[var]) or isinstance(row[var], bool) or row[var][0]!="v":
            continue

        if "," in row[var]:
            versions = row[var].split(",")
        else:
            versions = [row[var]]

        for version in versions:
            esgf_id = f"CMIP6.{act}.{inst}.{model}.{exp}.{run}.{freq}.{var}.{grid}.{version}"
            ids.append(esgf_id)

out_df = pd.DataFrame({"esgf_id": ids})
out_path = "esgf_ids_full_mon.csv"
out_df.to_csv(out_path, index=False)

out_path
