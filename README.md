# GOSH-FHIRworks2020-GraphFHIR
The GraphFHIR open source package aims to help hospitals optimising the the use of clinical data for research by **data visualisation**. This package uses the FHIR (Fast Healthcare Interoperability Resources) standard data, and focuses on data related to **Blood Pressure, Diastolic Blood Pressure, and Systolic Blood Pressure**.

The GraphFHIR package also provides **API endpoints** to access data used for visualisation for future research and development purposes.

## Deployment Guide
### Running the GOSH Drive (the data source for GraphFHIR) following the instructions on this [link](https://github.com/goshdrive/FHIRworks_2020).

Note: To successfully run the GOSH Drive, you are required to have its Azure FHIR API credentials.

### Installing necessary dependencies using terminal
Open a new terminal and run the following commands.
- Install [FHIR-Parser](https://pypi.org/project/FHIR-Parser/)
  ```
  pip install FHIR-Parser
  ```
- Install [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/install.html)
  ```
  pip install Flask-WTF
  ```
### (For Windows user only) Installing [Git Bash](https://gitforwindows.org/)
### Running the app
1. Clone the project and open it in Visual Studio Code.
2. For Windows user, open a new Git Bash terminal (you can type in "Git Bash" in Windows searching window). 

   For Mac user, open a new terminal.
3. In the terminal, navigate to the directory **GOSH-FHIRworks2020-GraphFHIR** then run the following commands:
   ```
   $ source virtual_env/bin/activate 
   $ export FLASK_APP=graphFHIR.py
   $ flask run
   ```
   Note: If the default localhost port is being used, you can manually allocated another port (e.g. port 2000) to run it by replacing the last commend `flask run` with
     
   ```
   $ flask run --port=2000
   ```
4. If successfully run the package, your terminal will display the following messages:
   ```
   Serving Flask app "graphFHIR.py"
   Environment: production
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   Debug mode: off
   Running on http://127.0.0.1:2000/ (Press CTRL+C to quit)
   ```
5. Open a web browser and navigate to your localhost port. 
   
   In this case, navigate to [http://127.0.0.1:2000/](http://127.0.0.1:2000/) to start.


To exit the package, press CTRL+C. 

To exit the virtual enironment in terminal, run the following command:
```
$ deactivate
```

## List of API endpoints
- GET all patients’ blood pressure-related observation data: **/api/patients**
- GET a patient’s blood pressure-related observation data: **/api/patients/** *patient id*
- GET blood pressure-related observation data for a selected number of pages of patient: **/api/patients/pages/** *number of pages*
