Hello!
This is a miniature Healthcare Information System I wrote in C++. It manages a local database of sample patient and employee information stored in .txt files on my personal computer -- though, it can be modified to handle them in SQL libraries.
Upon launch, it automatically reads the relevant file directories to load patient and employee data into working memory, stored in AVL trees so they can be easily organized alphabetically.
Any time a patient or employee's data is added, removed, or updated within working memory, that change is updated in the associated .txt file automatically. Employee trees are built based on department, whereas all patients are stored in one tree.
This program allows the user to look through all patient and employee data, and edit, add, and delete patients and employees.
It also has a "queue" function that serves as an ER. The queue works in order of severity: higher severity gets put further up on the queue; but, people with the same severity get put to the back of that severity level.
