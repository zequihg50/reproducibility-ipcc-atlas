#!/usr/bin/awk -f

BEGIN{
	FS=","
	OFS=" "
}

NR>1{
	split($1, a, "_")
	for(i=2; i<=6; i++) {
		if($i != "") {
			sub(".*/", "", $i)
			sub("\.ncml", "", $i)
			split($i, fs, "_")
			version = fs[9]
			sub("v", "", version)
			# CMIP6_ScenarioMIP_MOHC_UKESM1-0-LL_ssp126_day_tas_gn_v20190708
			query = sprintf("variant_label=%s project=%s activity_id=%s institution_id=%s source_id=%s experiment_id=%s table_id=%s variable_id=%s grid_label=%s version=%s", a[2], fs[1], fs[2], fs[3], fs[4], fs[5], fs[6], fs[7], fs[8], version)
			instance_id = sprintf("%s.%s.%s.%s.%s.%s.%s.%s.%s.%s", fs[1], fs[2], fs[3], fs[4], fs[5], a[2], fs[6], fs[7], fs[8], fs[9])
			id = sprintf("%s.%s.%s.%s.%s.%s.%s.%s.%s", fs[1], fs[2], fs[3], fs[4], fs[5], a[2], fs[6], fs[7], fs[8])
			printf("\"%s\",\"%s\",\"%s\"\n", id, instance_id, query)
		}
	}
}
