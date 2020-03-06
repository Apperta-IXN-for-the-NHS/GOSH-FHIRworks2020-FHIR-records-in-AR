'''
data.py: includes methods used to fetch relevant data from GOSH FHIR records
         and methods used to pre-processing data for visualisation.
'''

from fhir_parser import FHIR

fhir = FHIR()

# A helper function defined to convert a Datetime object to a Sting of format "YYYY-MM-DD"
def datetime_to_string(datetime):
    return datetime.strftime('%Y-%m-%d')

# Get all patients in a given FHIR record dataset 
# (the dataset is GOSH FHIR DRIVE in this case)
def get_all_patients():
    return fhir.get_all_patients()

# A boolean function defined to check if the patient ID exists in the FHIR records
def check_patient_id(patient_id):
    return fhir.get_patient(patient_id) != None

def get_patient_name(patient_id):
    patient = fhir.get_patient(patient_id)
    return str(patient.name)

# Return the list of observations for a single patient
def get_patient_observations(patient_id):
    return fhir.get_patient_observations(patient_id)

# Sort a patient's observation data according to the observation date
def sortByTime(data, date):
    sorted_zip = sorted(zip(date, data))
    sorted_data = [x for y, x in sorted_zip]
    sorted_date = [y for y, x in sorted_zip]
    return sorted_data, sorted_date

# Get a single patient's Blood Presure data, measurement unit & observation dates
# the returned data are sorted according to the observation dates
def patient_blood_presure(patient_observations):
    bp_unit = None
    patient_bp = [] 
    patient_bp_date = []
    sorted_bp = []
    sorted_bp_date = []

    # get a patient's observation data from FHIR records
    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Blood Pressure': 
                bp_unit = component.unit
                patient_bp.append(component.value)
                patient_bp_date.append(observation.issued_datetime)

    # sort the patient's observation data by dates
    sorted_bp, temp = sortByTime(patient_bp, patient_bp_date)
    for date in temp:
        sorted_bp_date.append(datetime_to_string(date))

    return bp_unit, sorted_bp, sorted_bp_date

# Get a single patient's Diastolic Blood Presure data, measurement unit & observation dates
# the returned data are sorted according to the observation dates
def patient_diastolic_blood_pressure(patient_observations):
    dbp_unit = None
    patient_dbp = []
    patient_dbp_date = []
    sorted_dbp = []
    sorted_dbp_date = []

    # get a patient's observation data from FHIR records
    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Diastolic Blood Pressure':
                dbp_unit = component.unit
                patient_dbp.append(component.value)
                patient_dbp_date.append(observation.issued_datetime)

    # sort the patient's observation data by dates
    sorted_dbp, temp = sortByTime(patient_dbp, patient_dbp_date)
    for date in temp:
        sorted_dbp_date.append(datetime_to_string(date))
    
    return dbp_unit, sorted_dbp, sorted_dbp_date

# Get a single patient's Systolic Blood Presure data, measurement unit & observation dates
# the returned data are sorted according to the observation dates
def patient_systolic_blood_pressure(patient_observations):
    sbp_unit = None
    patient_sbp = [] 
    patient_sbp_date = []
    sorted_sbp = []
    sorted_sbp_date = []

    # get a patient's observation data from FHIR records
    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Systolic Blood Pressure':
                sbp_unit = component.unit
                patient_sbp.append(component.value)
                patient_sbp_date.append(observation.issued_datetime)

    # sort the patient's observation data by dates
    sorted_sbp, temp = sortByTime(patient_sbp, patient_sbp_date)
    for date in temp:
        sorted_sbp_date.append(datetime_to_string(date))
    
    return sbp_unit, sorted_sbp, sorted_sbp_date

# Get the mean of a given data array
def get_average(data):
    # map 'None' and 'N/A' to 0
    arr = [0 if (value is None or value == 'N/A') else value for value in data]
    return sum(arr)/len(arr)

# A boolean function defined to check if all elements in an arry are None
def check_all_none(data):
    return all(value is None for value in data)