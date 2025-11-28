#!/usr/bin/awk -f

BEGIN{
	FS=","
	OFS=" "

        # institution not present in atlas inventories
        inst["ACCESS-CM2"] = "CSIRO-ARCCSS"
        inst["ACCESS-ESM1-5"] = "CSIRO"
        inst["AWI-CM-1-1-MR"] = "AWI"
        inst["BCC-CSM2-MR"] = "BCC"
        inst["CAMS-CSM1-0"] = "CAMS"
        inst["CanESM5"] = "CCCma"
        inst["CESM2"] = "NCAR"
        inst["CESM2-WACCM"] = "NCAR"
        inst["CMCC-CM2-SR5"] = "CMCC"
        inst["CNRM-CM6-1"] = "CNRM-CERFACS"
        inst["CNRM-CM6-1-HR"] = "CNRM-CERFACS"
        inst["CNRM-ESM2-1"] = "CNRM-CERFACS"
        inst["EC-Earth3"] = "EC-Earth-Consortium"
        inst["EC-Earth3-Veg"] = "EC-Earth-Consortium"
        inst["FGOALS-g3"] = "CAS"
        inst["GFDL-CM4"] = "NOAA-GFDL"
        inst["GFDL-ESM4"] = "NOAA-GFDL"
        inst["HadGEM3-GC31-LL"] = "MOHC"
        inst["IITM-ESM"] = "CCCR-IITM"
        inst["INM-CM4-8"] = "INM"
        inst["INM-CM5-0"] = "INM"
        inst["IPSL-CM6A-LR"] = "IPSL"
        inst["KACE-1-0-G"] = "NIMS-KMA"
        inst["KIOST-ESM"] = "KIOST"
        inst["MIROC6"] = "MIROC"
        inst["MIROC-ES2L"] = "MIROC"
        inst["MPI-ESM-1-2-HAM"] = "HAMMOZ-Consortium"
        inst["MPI-ESM1-2-HR"] = "MPI-M"
        inst["MPI-ESM1-2-LR"] = "MPI-M"
        inst["MRI-ESM2-0"] = "MRI"
        inst["NESM3"] = "NUIST"
        inst["NorESM2-LM"] = "NCC"
        inst["NorESM2-MM"] = "NCC"
        inst["TaiESM1"] = "AS-RCEC"
        inst["UKESM1-0-LL"] = "MOHC"
}

NR>1{
	split($1, a, "_")
	scenario = a[3]
	if(scenario == "historical") {
		activity = "CMIP"
	} else {
		activity = "ScenarioMIP"
	}

	# manage version, might be false or contain several versions split by ,
	if(index($4, ",") > 0) {
		split($4, versions, ",")
	} else {
		versions[1] = $4
	}

	if(versions[1] != "FALSE" && versions[1] != "") {
		for(i in versions) {
			version = versions[i]
			sub("v", "", version)

			query = sprintf("variant_label=%s project=%s activity_id=%s institution_id=%s source_id=%s experiment_id=%s table_id=%s variable_id=%s grid_label=%s version=%s", a[4], a[1], activity, inst[a[2]], a[2], scenario, "day", "tas", "gn", version)
			instance_id = sprintf("%s.%s.%s.%s.%s.%s.%s.%s.%s.%s", a[1], activity, inst[a[2]], a[2], scenario, a[4], "day", "tas", "gn", versions[i])
			id = sprintf("%s.%s.%s.%s.%s.%s.%s.%s.%s", a[1], activity, inst[a[2]], a[2], scenario, a[4], "day", "tas", "gn")
			printf("\"%s\",\"%s\",\"%s\"\n", id, instance_id, query)
		}
	}
}
