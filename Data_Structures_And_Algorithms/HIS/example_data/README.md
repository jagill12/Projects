# Example Data Structure

This directory demonstrates the example file structure of the patient and employee data logged from real runs of the Healthcare Information System.

The name of the directory has been changed from "HIS data" to "example_data" on this repository for the sake of simplicity in communication.

These files are examples only and are not required for compilation.

At runtime, the program dynamically creates patient and employee
directories following this structure:
```
Patients/
 └── First_Last/
     ├── First_Last.txt
     └── Visits/

Employees/
 └── First_Last/
     └── First_Last.txt
```
While employees are listed by departments, which are stored in a singly-linked list in the application, they are stored as individual employees with the 
same directory structure as patients in the file explorer. The singly-linked list structure of departments was a decision I made to showcase my ability of 
recursively traversing the employee file directory, extracting department information, and organizing employees by department alphabetically.
