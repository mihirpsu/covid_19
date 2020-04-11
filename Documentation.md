# Documentation:

## Files and Folders:
1. fused_dataset.csv 
	- This dataset contains US county level information about
		- Population
		- Population Density
		- Diabetic Prevalence Percentage 
		- Hypertension Prevalence Percentage
		- Old Population Percentage
		- Crude Rate for Cancer
		- Crude Rate for Chronic Respiratory Diseases 
		- Longitude and Latitude of Centroid of the County
2. gz_2010_us_050_00_500k.json
	- US Census Cartographic Boundary files for each county in JSON format
3. sample_file.csv
	- input file generated using fused_dataset.csv and COVID-19 Cases Statistics for a particular date (exactly same as comapre_file.csv format) (Refer to data_collection folder)
4. compare_file.csv
	- actual COVID-19 cases statistics after 5 days from input file date
5. Sample_Code_Run_Notebook.ipynb
	- Interactive sample Jupyter Notebook
6. grp_sen_spc.py
	- Module used to generate
		- Variable Importance Graph
		- Sensitivity and Specificity of the 3-Stage Model
7. cty_map.py
	- Module to generate County Level US Map
8. xgboost_hyperopt.py
	- Module used to tune hyper-parameters for XGBoost Regression and Classification using Hyperopt package
9. Documentation.md
	- Documentation Details File
10. data_collection folder
	- Sample cod to pull the data

## The flow of Sample Code
1. Importing necessary modules and files 
2. Preparing dataset for XGBoost Classification Model
3. XGBoost Classification Model Development
	1. Tuning Hyper-parameters using Hyperopt package
	2. 5-fold cross validation
	3. Finalizing the model
4. Classification Model Evaluation
5. Preparing dataset for XGBoost Regression Model
6. XGBoost Regression Model Development
	1. Tuning Hyper-parameters using Hyperopt package
	2. 5-fold cross validation
	3. Finalizing the model
7. Regression Model Evaluation
8. 3-Stage Model Calculations and segmentation
9. Variable Importance Graph, Sensitivity and Specificity Analysis
10. US County Level Map Generation

# Citation:
If you use this dataset, please cite the following:  
Early Stage Prediction of US County Vulnerability to the COVID-19 Pandemic
Mihir Mehta, Juxihong Julaiti, Paul Griffin, Soundar Kumara
medRxiv 2020.04.06.20055285; doi: https://doi.org/10.1101/2020.04.06.20055285

## References:
1. U.S. Census Bureau PD. Annual Resident Population Estimates, Estimated Components of Resident Population Change, and Rates of the Components of Resident Population Change for States and Counties: April 1, 2010 to July 1, 2018. https://www2.census.gov/programs-surveys/popest/datasets/2010-2018/counties/asrh/cc-est2018alldata.csv. Published 2019. Accessed March 19, 2020.
2. Website AFF. 2010 County Level Population Density. 2010. https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk. Accessed March 19, 2020.
3. Centers for Disease Control and Prevention UD of H and HS. Centers for Disease Control and Prevention. National Diabetes Statistics Report, 2020. Atlanta, GA. Cdc.Gov. doi:10.1111/j.1465-3362.2012.00432.x
4. United States Department of Health and Human Services C for DC and P and NCI. 2005–2016 Database: National Program of Cancer Registries and Surveillance, Epidemiology, and End Results SEER*Stat Database: NPCR and SEER Incidence – U.S. Cancer Statistics Public Use Research Database with Puerto Rico, November 2018 submission (2005–20. https://www.cdc.gov/cancer/uscs/public-use/. Published 2019. Accessed March 19, 2020.
5. United States Hypertension Estimates by County 2001-2009 | GHDx. http://ghdx.healthdata.org/record/ihme-data/united-states-hypertension-estimates-county-2001-2009. Accessed April 3, 2020.
6. United States Chronic Respiratory Disease Mortality Rates by County 1980-2014 | GHDx. http://ghdx.healthdata.org/record/ihme-data/united-states-chronic-respiratory-disease-mortality-rates-county-1980-2014. Accessed April 3, 2020.
7. Minn 2010-2014 County Cancer Profiles. https://pennstate.maps.arcgis.com/home/item.html?id=ab5ab6a44f124ecc876a9d7c9eaf859c. Accessed April 3, 2020.
8. GeoJSON and KML data for the United States - Eric Celeste. https://eric.clst.org/tech/usgeojson/. Accessed April 3, 2020.
9. COVID-19/Coronavirus Live Updates With Credible Sources in US and Canada | 1Point3Acres. https://coronavirus.1point3acres.com/. Accessed April 3, 2020.
10. NYTimes. NYtimes/covid-19-data: An ongoing repository of data on coronavirus cases and deaths in the U.S. https://github.com/nytimes/covid-19-data. Published 2020. Accessed April 1, 2020.