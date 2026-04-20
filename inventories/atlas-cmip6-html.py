# coding: utf-8
import pandas as pd
df = pd.read_html("CMIP6.html")[0]
df = df.join(df["dataset"].str.split("_", expand=True))
df["activity_id"] = df[3].map(lambda e: "CMIP" if e == "historical" else "ScenarioMIP")
df[7] = "v"+df[7]
df["instance_id"] = df[[0,"activity_id",1,2,3,4,5,"variable",6,7]].agg('.'.join, axis=1)
df["instance_id"].to_csv("atlas-cmip6-html.txt", index=False)
