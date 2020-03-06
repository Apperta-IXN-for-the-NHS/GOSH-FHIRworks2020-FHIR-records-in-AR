from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()

ages = []
for patient in patients:
    ages.append(patient.age())

print("patients' average age: " + str(sum(ages)/len(ages)))

def datetimeToString(datetime):
    return datetime.strftime('%Y-%m-%d')

patient_1_comps = []
patient_1_date = []
patient_1_bp = []   # Blood Pressure
patient_1_bp_date = []
patient_1_dbp = []  # Diastolic Blood Pressure
patient_1_dbp_date = []
patient_1_sbp = []  # Systolic Blood Pressure
patient_1_sbp_date = []

patient_1 = patients[0]
print(patient_1.uuid)
patient_1_obs = fhir.get_patient_observations(patient_1.uuid)   # list of observations
for observation in patient_1_obs:
    components = observation.components  # list of components for a single observation
    for component in components:
        if component.display == 'Blood Pressure': 
            patient_1_bp.append(component.value)
            patient_1_bp_date.append(observation.issued_datetime)
        elif component.display == 'Diastolic Blood Pressure':
            patient_1_dbp.append(component.value)
            patient_1_dbp_date.append(observation.issued_datetime)
        elif component.display == 'Systolic Blood Pressure':
            patient_1_sbp.append(component.value)
            patient_1_sbp_date.append(observation.issued_datetime)

# print(patient_1_bp)
# print(patient_1_bp_date)
# print(patient_1_dbp)
# print(patient_1_dbp_date)
# print(patient_1_sbp)
# print(patient_1_sbp_date)

def sortByTime(data, date):
    sorted_zip = sorted(zip(date, data))
    sorted_data = [x for y, x in sorted_zip]
    sorted_date = [y for y, x in sorted_zip]
    return sorted_data, sorted_date


def getAverage(data):
    # map 'None' and 'N/A' to 0
    arr = [0 if (value is None or value == 'N/A') else value for value in data]
    print("arr: ")
    print(arr)
    return sum(arr)/len(arr)

def check_all_none(data):
    return all(value is None for value in data)

def patient_blood_presure(patient_id):
    patient_bp = [] 
    patient_observations = fhir.get_patient_observations(patient_id)   # list of observations

    for observation in patient_observations:
        components = observation.components 
        for component in components:
            if component.display == 'Blood Pressure': 
                patient_bp.append(component.value)

    return patient_bp

def test():
    patient = fhir.get_patient_page(int("10"))
    print(len(patient))

test()



'''
observations = []

for patient in patients:
    observations.extend(fhir.get_patient_observations(patient.uuid))

print("Total of {} observations".format(len(observations)))

observation_types = [observation.type for observation in observations]
most_frequent_observation_type = max(set(observation_types), key=observation_types.count)
print("Most common observation type: {}".format(most_frequent_observation_type))

observation_components = []
for observation in observations:
    observation_components.extend(observation.components)

print("Total of {} observation components".format(len(observation_components)))

observation_component_types = [observation_component.display for observation_component in observation_components]
most_frequent_observation_component_type = max(set(observation_types), key=observation_types.count)
print("Most common observation component type: {}".format(most_frequent_observation_component_type))
'''