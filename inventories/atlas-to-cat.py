import pandas as pd

df = pd.read_csv('CMIP6_day.csv')

# mappings
grid = {
"ACCESS-CM2":"gn","ACCESS-ESM1-5":"gn","AWI-CM-1-1-MR":"gn","BCC-CSM2-MR":"gn",
"CAMS-CSM1-0":"gn","CanESM5":"gn","CESM2":"gn","CESM2-WACCM":"gn","CMCC-CM2-SR5":"gn",
"CNRM-CM6-1":"gr","CNRM-CM6-1-HR":"gr","CNRM-ESM2-1":"gr","EC-Earth3":"gr",
"EC-Earth3-Veg":"gr","FGOALS-g3":"gn","GFDL-CM4":"gr1","GFDL-ESM4":"gr1",
"HadGEM3-GC31-LL":"gn","IITM-ESM":"gn","INM-CM4-8":"gr1","INM-CM5-0":"gr1",
"IPSL-CM6A-LR":"gr","KACE-1-0-G":"gr","KIOST-ESM":"gr1","MIROC-ES2L":"gn",
"MIROC6":"gn","MPI-ESM-1-2-HAM":"gn","MPI-ESM1-2-HR":"gn","MPI-ESM1-2-LR":"gn",
"MRI-ESM2-0":"gn","NESM3":"gn","NorESM2-LM":"gn","NorESM2-MM":"gn",
"TaiESM1":"gn","UKESM1-0-LL":"gn"
}

inst = {
"ACCESS-CM2":"CSIRO-ARCCSS","ACCESS-ESM1-5":"CSIRO","AWI-CM-1-1-MR":"AWI",
"BCC-CSM2-MR":"BCC","CAMS-CSM1-0":"CAMS","CanESM5":"CCCma","CESM2":"NCAR",
"CESM2-WACCM":"NCAR","CMCC-CM2-SR5":"CMCC","CNRM-CM6-1":"CNRM-CERFACS",
"CNRM-CM6-1-HR":"CNRM-CERFACS","CNRM-ESM2-1":"CNRM-CERFACS",
"EC-Earth3":"EC-Earth-Consortium","EC-Earth3-Veg":"EC-Earth-Consortium",
"FGOALS-g3":"CAS","GFDL-CM4":"NOAA-GFDL","GFDL-ESM4":"NOAA-GFDL",
"HadGEM3-GC31-LL":"MOHC","IITM-ESM":"CCCR-IITM","INM-CM4-8":"INM",
"INM-CM5-0":"INM","IPSL-CM6A-LR":"IPSL","KACE-1-0-G":"NIMS-KMA",
"KIOST-ESM":"KIOST","MIROC6":"MIROC","MIROC-ES2L":"MIROC",
"MPI-ESM-1-2-HAM":"HAMMOZ-Consortium","MPI-ESM1-2-HR":"MPI-M",
"MPI-ESM1-2-LR":"MPI-M","MRI-ESM2-0":"MRI","NESM3":"NUIST",
"NorESM2-LM":"NCC","NorESM2-MM":"NCC","TaiESM1":"AS-RCEC",
"UKESM1-0-LL":"MOHC"
}

variables = ['pr','psl','tas','tasmax','tasmin','sftlf']

ids = []

for _, row in df.iterrows():
    sim = row['Simulation']
    parts = sim.replace('.', '_').split('_')
    model = parts[1]
    exp = parts[2]
    act = "CMIP" if exp == "historical" else "ScenarioMIP"
    run = parts[3]

    if model not in grid:
        print(f"Missing model in grid {model}.")
        continue
    if model not in inst:
        print(f"Missing model in inst {model}.")
        continue

    for var in variables:
        if pd.isna(row[var]) or isinstance(row[var], bool) or row[var][0]!="v":
            continue

        if "," in row[var]:
            versions = row[var].split(",")
        else:
            versions = [row[var]]

        for version in versions:
            esgf_id = f"CMIP6.{act}.{inst[model]}.{model}.{exp}.{run}.day.{var}.{grid[model]}.{version}"
            ids.append(esgf_id)

out_df = pd.DataFrame({"esgf_id": ids})
out_path = "esgf_ids_full.csv"
out_df.to_csv(out_path, index=False, header=False)

out_path
