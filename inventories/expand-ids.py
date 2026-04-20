import pandas as pd

# CMIP6
df = pd.read_csv("esgf-ids.txt", header=None, names=["instance_id"])
df_expand = df["instance_id"].str.split(".", expand=True).rename({
        0: "project",
        1: "activity_id",
        2: "institution_id",
        3: "source_id",
        4: "experiment_id",
        5: "variant_label",
        6: "table_id",
        7: "variable_id",
        8: "grid_label",
        9: "version",},
    axis=1)


with open("esgf-ids-expanded-cmip6.txt", "w") as f:
    for i, row in df_expand.iterrows():
        for k in row.index:
            if k != "version":
                f.write(f"{k}={row[k]} ")
        f.write("\n\n")

df = pd.read_csv("atlas-cmip6-html.txt", header=None, names=["instance_id"])
df_expand = df["instance_id"].str.split(".", expand=True).rename({
        0: "project",
        1: "activity_id",
        2: "institution_id",
        3: "source_id",
        4: "experiment_id",
        5: "variant_label",
        6: "table_id",
        7: "variable_id",
        8: "grid_label",
        9: "version",},
    axis=1)

with open("esgf-ids-expanded-cmip6.txt", "a") as f:
    for i, row in df_expand.iterrows():
        for k in row.index:
            if k != "version":
                f.write(f"{k}={row[k]} ")
        f.write("\n\n")

df = pd.read_csv("atlas-cmip6-tsu.txt", header=None, names=["instance_id"])
df_expand = df["instance_id"].str.split(".", expand=True).rename({
        0: "project",
        1: "activity_id",
        2: "institution_id",
        3: "source_id",
        4: "experiment_id",
        5: "variant_label",
        6: "table_id",
        7: "variable_id",
        8: "grid_label",
        9: "version",},
    axis=1)

with open("esgf-ids-expanded-cmip6.txt", "a") as f:
    for i, row in df_expand.iterrows():
        for k in row.index:
            if k != "version":
                f.write(f"{k}={row[k]} ")
        f.write("\n\n")

# CMIP5
df = pd.read_csv("atlas-cmip5.txt", header=None, names=["instance_id"])
df_expand = df["instance_id"].str.split(".", expand=True).rename({
        0: 'project',
        1: 'product',
        2: 'institute',
        3: 'model',
        4: 'experiment',
        5: 'time_frequency',
        6: 'realm',
        7: 'cmor_table',
        8: 'ensemble',
        9: 'version'},
    axis=1)

with open("esgf-ids-expanded-cmip5.txt", "w") as f:
    for i, row in df_expand.iterrows():
        for k in row.index:
            if k != "version":
                f.write(f"{k}={row[k]} ")
        f.write("\n\n")
