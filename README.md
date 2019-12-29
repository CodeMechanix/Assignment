# REST API Based Key-Value Store

#### Type those URLs to the browser:
* Get all the values of the store: http://127.0.0.1:8000/api/patients
* Get specific values from the store: http://127.0.0.1:8000/api/patients/id
* Create a new value: http://127.0.0.1:8000/api/patients/add/

#### API monitoring the outputs
* Status code 200 = Retrive Data Successfully 
* Status code 400 = Bad Request
* Status code 204 = Deleted Value Successfully 
* Status code 201 = Created New Data

#### Retrive all Data from Store
![All Data](https://github.com/CodeMechanix/Assignment/blob/master/Workflow-Image/All-Store-Value.PNG)

#### Add New data From Store 
![Add New Data](https://github.com/CodeMechanix/Assignment/blob/master/Workflow-Image/Add-New-Data.PNG)

#### Update Specific Data
![update Data](https://github.com/CodeMechanix/Assignment/blob/master/Workflow-Image/Specific-Data-Update.PNG)

#### Delete Data from Store
![Delete Data](https://github.com/CodeMechanix/Assignment/blob/master/Workflow-Image/Delete-Data.PNG)

#### Package Dependency
* pip install djangorestframework
* pip install psycopg2 (I Used PostgreSQL for data store)




