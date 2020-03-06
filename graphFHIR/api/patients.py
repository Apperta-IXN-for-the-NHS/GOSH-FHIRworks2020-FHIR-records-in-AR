'''
api/patients.py: contains Patient API routes.
Below is a summary of all implemented routes for GraphFHIR application:
    [HTTP Method, Resource URL, Notes]
1. GET,  /api/patients/<id>,          Return a patient with all blood pressure-related observation data
2. GET,  /api/patients/pages/<page>,  Return the collection of a selected number of pages of patient with their blood pressure-related observation data
3. GET,  /api/patients,               Return the collection of all patients with their blood pressure-related observation data
'''

from flask import jsonify
from graphFHIR.api import bp, parser

@bp.route('/patients/<id>', methods=['GET'])
def get_patient(id):
    return jsonify(parser.patient_to_dict(id))

@bp.route('/patients/pages/<page>', methods=['GET'])
def get_patients_pages(page):
    return jsonify(parser.pages_of_patients_to_dict(page))

@bp.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(parser.all_patients_to_dict())
