'''
routes.py: containing handlers for the application routes (the view functions)
view functions are mapped to one or more route URLs so that Flask knows 
what logic to execute when a client requests a given URL
'''

from flask import render_template, flash, redirect, request
from graphFHIR import app, data
from graphFHIR.forms import PatientIDForm

'''
labels = ['JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 
          'JUL', 'AUG','SEP', 'OCT', 'NOV', 'DEC']
values = [967.67, 1190.89, 1079.75, 1349.19,2328.91, 2504.28, 
          2873.83, 4764.87,4349.29, 6458.30, 9907, 16297]
colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", 
          "#ABCABC", "#4169E1", "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
'''

all_patients = data.get_all_patients()

''' Define and initialise necessary data fields '''
patient_observations = []

patient_bp_unit = []
patient_bp = []
patient_bp_date = []
patient_dbp_unit = []
patient_dbp = []
patient_dbp_date = []
patient_sbp_unit = []
patient_sbp = []
patient_sbp_date = []

labels = []
values = []
colors = []

def getData(patient_id):
    # access the above global variables
    global patient_observations
    global patient_bp_unit
    global patient_bp
    global patient_bp_date
    global patient_dbp_unit
    global patient_dbp
    global patient_dbp_date
    global patient_sbp_unit
    global patient_sbp
    global patient_sbp_date

    patient_observations = data.get_patient_observations(patient_id)
    patient_bp_unit, patient_bp, patient_bp_date = data.patient_blood_presure(patient_observations)
    patient_dbp_unit, patient_dbp, patient_dbp_date = data.patient_diastolic_blood_pressure(patient_observations)
    patient_sbp_unit, patient_sbp, patient_sbp_date = data.patient_systolic_blood_pressure(patient_observations)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    patient_id = None
    form = PatientIDForm(request.form)
    if request.method == 'POST':
        patient_id = request.form['patient_id']
    if form.validate() and data.checkPatientID(patient_id):
        getData(patient_id)
        # if the patient exists, proceed to graphing
        return redirect('/bar')
    
    return render_template('index.html', title='Home page', form=form)

@app.route('/bar')
def bar():
    #print(patient_observations)
    #print(patient_dbp_date)
    #print(patient_dbp)
    return render_template('bar_chart.html', title='Bar Chart', max=17000, 
                            labels=patient_dbp_date, values=patient_dbp)

@app.route('/line')
def line():
    line_labels = labels
    line_values = values
    return render_template('line_chart.html', title='Line Graph', max=17000, 
                            labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    pie_colors = colors
    return render_template('pie_chart.html', title='Pie Chart', 
                            labels=pie_labels, values=pie_values, colors = pie_colors)