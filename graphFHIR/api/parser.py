'''
api/parser.py: defines helper functions to parser GraphFHIR data into JSON format
               as a preparation for Patient API (api/patients.py).
Relevant data fetching and clean-up is done by calling methods defined in data.py.
'''

from graphFHIR.data import *

# Parse a single patient's blood pressure observation data into a json object
def patient_to_dict(patient_id):
    patient = get_patient(patient_id)
    patient_observations = get_patient_observations(patient_id)

    bp_unit, patient_bp, patient_bp_date = patient_blood_presure(patient_observations)
    dbp_unit, patient_dbp, patient_dbp_date = patient_diastolic_blood_pressure(patient_observations)
    sbp_unit, patient_sbp, patient_sbp_date = patient_systolic_blood_pressure(patient_observations)

    avg_bp = get_average(patient_bp)
    avg_dbp = get_average(patient_dbp)
    avg_sbp = get_average(patient_sbp)
    
    dates = patient_sbp_date
    obs_unit = sbp_unit

    prefix = patient.name.prefix_list
    family_name = patient.name.family
    given_name = patient.name.given_list
    
    data = {
        'id': patient_id,
        'name': {
            'prefix': prefix,
            'family': family_name,
            'given': given_name,
        },
        'avg_bp': avg_bp,
        'avg_dbp': avg_dbp,
        'avg_sbp': avg_sbp,
        'bp_data': {
            'obs_dates': dates,
            'values': patient_bp,
            'unit': obs_unit
        },
        'dbp_data': {
            'obs_dates': dates,
            'values': patient_dbp,
            'unit': obs_unit
        },
        'bp_data': {
            'obs_dates': dates,
            'values': patient_sbp,
            'unit': obs_unit
        },
    }
    return data

# Get a collection of patients up to the specific page number, then
# parse the patients' blood pressure observation data into a json object
def pages_of_patients_to_dict(page):
    patients = get_pages_of_patients(int(page))
    all_patients_id = [patient.uuid for patient in patients]
    size = len(patients)

    data = {
        'items': [patient_to_dict(patient_id) for patient_id in all_patients_id],
        '_meta': {
            'total_pages': page,
            'total_patients': size
        }
    }
    return data

# Get all patients in the GOSH FHIR dataset, then
# parse the patients' blood pressure observation data into a json object
def all_patients_to_dict():
    patients = get_all_patients()
    all_patients_id = [patient.uuid for patient in patients]
    size = len(patients)

    data = {
        'items': [patient_to_dict(patient_id) for patient_id in all_patients_id],
        '_meta': {
            'total_patients': size
        }
    }
    return data
