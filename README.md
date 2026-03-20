# ESGF data volatility

> Volatility refers to the degree of price fluctuation in a market, security, or substance over time. In finance, it indicates risk and is measured by the standard deviation or beta of returns, with high volatility meaning large price swings and high risk.

Does the ESGF provides enough reproducibility capabilities?

## Usage

```bash
# esgfva
./esgfva.awk gsat-esgf.csv 

# atlas
./atlas.awk CMIP6_day.csv
```

Obatining WDC ESGF dataset identifiers:

```bash
url='https://www.wdc-climate.de/ui/solr/select?q=hierarchy_steps_ss%3AIPCC-AR6_CMIP6%20AND%20publication_type_s%3ADataset&rows=500&indent=on&fl=entry_name_s&facet=off&facet.mincount=0&facet.limit=-1&start='
seq 0 500 65118 | sed 5q | while read n ; do wget -q -O - "${url}${n}" | jq -r '.response.docs | map(.entry_name_s | split(" ") | join("."))[]' ; done >> wdc-ids-20260319.txt
```
