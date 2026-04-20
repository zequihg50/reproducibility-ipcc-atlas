import pandas as pd

df = pd.read_csv("cmip6_datasets_ch13_input_20220125.csv", names=["instance_id", "_"], header=None)["instance_id"].str.replace(r'\.(\d+)$', r'.v\1', regex=True)
df.to_csv("atlas-cmip6-tsu.txt", header=None, index=False)
