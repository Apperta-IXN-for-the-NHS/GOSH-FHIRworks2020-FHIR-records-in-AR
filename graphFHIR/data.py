from fhir_parser import FHIR

fhir = FHIR()
#patients = fhir.get_all_patients()

#patient_1_id = patients[0].uuid

'''
A helper converter that converts a Datetime object 
to a Sting of format "YYYY-MM-DD"
'''
def datetimeToString(datetime):
    return datetime.strftime('%Y-%m-%d')

def get_all_patients():
    return fhir.get_all_patients()

def checkPatientID(patient_id):
    return fhir.get_patient(patient_id) != None

# return the list of observations for a single patient
def get_patient_observations(patient_id):
    return fhir.get_patient_observations(patient_id)

def patient_blood_presure(patient_observations):
    patient_bp_unit = None
    patient_bp = [] 
    patient_bp_date = []

    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Blood Pressure': 
                patient_bp_unit = component.unit
                patient_bp.append(component.value)
                patient_bp_date.append(datetimeToString(observation.issued_datetime))
        
    return patient_bp_unit, patient_bp, patient_bp_date

def patient_diastolic_blood_pressure(patient_observations):
    patient_dbp_unit = None
    patient_dbp = []
    patient_dbp_date = []

    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Diastolic Blood Pressure':
                patient_dbp_unit = component.unit
                patient_dbp.append(component.value)
                patient_dbp_date.append(datetimeToString(observation.issued_datetime))

    return patient_dbp_unit, patient_dbp, patient_dbp_date

def patient_systolic_blood_pressure(patient_observations):
    patient_sbp_unit = None
    patient_sbp = [] 
    patient_sbp_date = []

    for observation in patient_observations:
        # list of components for a single observation
        components = observation.components 
        for component in components:
            if component.display == 'Systolic Blood Pressure':
                patient_sbp_unit = component.unit
                patient_sbp.append(component.value)
                patient_sbp_date.append(datetimeToString(observation.issued_datetime))

    return patient_sbp_unit, patient_sbp, patient_sbp_date


