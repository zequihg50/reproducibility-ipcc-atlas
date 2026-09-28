# On long-term archival and data stewardship of digital products included in climate assessment reports: The case of the Interactive Atlas

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zequihg50/reproducibility-ipcc-atlas/HEAD?urlpath=%2Fdoc%2Ftree%2Fmain.ipynb)

## Loading datasets

```python
import pandas as pd
import xarray as xr

df = pd.read_csv("data_inventory.csv.zip")
subset = df[df["opendap"].str.contains("v20190710/tas_day_MPI-ESM1-2-HR_historical_r1i1p1f1_gn_")]["opendap"].sort_values()
ds = xr.open_mfdataset(list(subset), data_vars=["tas"], compat="no_conflicts")
```

## Notes

Obatining WDC ESGF dataset identifiers:

```bash
# CMIP6
url='https://www.wdc-climate.de/ui/solr/select?q=hierarchy_steps_ss%3AIPCC-AR6_CMIP6%20AND%20publication_type_s%3ADataset&rows=500&indent=on&fl=entry_name_s&facet=off&facet.mincount=0&facet.limit=-1&start='
seq 0 500 65118 | while read n ; do wget -q -O - "${url}${n}" | jq -r '.response.docs | map(.entry_name_s | split(" ") | join("."))[]' ; done >> wdc-ids-20260319.txt

# CMIP5
url='https://www.wdc-climate.de/ui/solr/select?q=hierarchy_steps_ss%3AIPCC-AR5_CMIP5%20AND%20publication_type_s%3ADataset&rows=500&indent=on&fl=entry_name_s&facet=off&facet.mincount=0&facet.limit=-1&start='
seq 0 500 819355 | while read n ; do wget -q -O - "${url}${n}" | jq -r '.response.docs | map(.entry_name_s | split(" ") | join("."))[]' ; done >> wdc-ids-cmip5-20260319.txt

# CORDEX
url='https://www.wdc-climate.de/ui/solr/select?q=publication_type_s%3ADataset%20AND%20hierarchy_steps_ss%3ACORDEX_DDS-CMIP5_native-grid&rows=500&&indent=on&fl=entry_name_s&facet=off&start='
seq 0 500 36933 | while read n ; do wget -q -O - "${url}${n}" | jq -r '.response.docs | map(.entry_name_s | split(" ") | join("."))[]' ; done | awk -F. 'BEGIN{OFS="."}{a=$NF; $NF=$(NF-1); $(NF-1)=a; print}' >> wdc-ids-cordex-20260319.txt
```
