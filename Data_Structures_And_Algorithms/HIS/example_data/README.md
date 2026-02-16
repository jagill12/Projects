# Example Data Structure

This directory demonstrates the expected filesystem layout used by the
Healthcare Information System.

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
