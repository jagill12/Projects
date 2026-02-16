//Preprocessor Directives Section
#include <stdio.h> //For I/O functions.
#include <stdlib.h> //For standard library functions including memory management.
#include <string.h> //For string handling functions.
#include <windows.h> //Windows-specific API functions.
#include <dirent.h> //Directory traversal functions.
#include <direct.h> //Directory creation and manipulation functions.
#include <sys/types.h> //Data types used in system calls, specifically with directory operations.
#include <sys/stat.h> //Used for obtaining information about files and directories.
#include <errno.h> //Defines macros for reporting and retrieving error codes.

#define MAX_NAME_LENGTH 100
#define MAX_ADDRESS_LENGTH 200
#define MAX_PHONE_LENGTH 15
#define MAX_DOB_LENGTH 12  // format: YYYY-MM-DD
#define MAX_GENDER_LENGTH 10
#define MAX_BLOOD_TYPE_LENGTH 5
#define MAX_SSN_LENGTH 13  // format: XXX-XX-XXXX
#define MAX_POSITION_LENGTH 50
#define MAX_DEPARTMENT_LENGTH 50
#define MAX_EMPLOYEE_ID_LENGTH 20
#define MAX_EMAIL_LENGTH 100
#define MAX_LINE_LENGTH 256

#define max(a, b) ((a) > (b) ? (a) : (b))

//Structs and Typedefs Section
typedef struct PatientNode { //Struct for PatientNode to hold all relevant Patient data in the 'patients' AVL tree.
    char firstName[MAX_NAME_LENGTH];
    char lastName[MAX_NAME_LENGTH];
    char dateOfBirth[MAX_DOB_LENGTH];
    char gender[MAX_GENDER_LENGTH];
    char address[MAX_ADDRESS_LENGTH];
    char phone[MAX_PHONE_LENGTH];
    char email[MAX_EMAIL_LENGTH];
    char bloodType[MAX_BLOOD_TYPE_LENGTH];
    char ssn[MAX_SSN_LENGTH];
    int patientID;
    int severity;
    struct PatientNode* left;
    struct PatientNode* right;
    int height;
} PatientNode;

typedef struct EmployeeNode { //Struct for EmployeeNode to hold all relevant Employee data in the 'employees' AVL trees.
    char firstName[MAX_NAME_LENGTH];
    char lastName[MAX_NAME_LENGTH];
    char dateOfBirth[MAX_DOB_LENGTH];
    char gender[MAX_GENDER_LENGTH];
    char address[MAX_ADDRESS_LENGTH];
    char phone[MAX_PHONE_LENGTH];
    char email[MAX_EMAIL_LENGTH];
    char ssn[MAX_SSN_LENGTH];
    char position[MAX_POSITION_LENGTH];
    char department[MAX_DEPARTMENT_LENGTH];
    char employeeID[MAX_EMPLOYEE_ID_LENGTH];
    char salary[MAX_LINE_LENGTH];
    char dateOfHire[MAX_DOB_LENGTH];
    struct EmployeeNode* left;
    struct EmployeeNode* right;
    int height;
} EmployeeNode;

typedef struct DepartmentNode { //Struct for DepartmentNode, which functions to make a linked list of employee departments and display all employees in all departments.
    char department[MAX_DEPARTMENT_LENGTH];
    EmployeeNode* employees; //Points to the root of the employee AVL tree of employees in the current department.
    struct DepartmentNode* next; //Moves to the next department in the linked list.
} DepartmentNode;

typedef struct PriorityQueueNode { //Struct for PriorityQueueNode, which functions to process patients in the priority queue.
    PatientNode* patient;
    struct PriorityQueueNode* next;
} PriorityQueueNode;

typedef struct { //Struct that initializes the use of PriorityQueue.
    PriorityQueueNode* front;
} PriorityQueue;

//Function declarations section


//Patient and EmployeeNode functions.
PatientNode* createPatientNode(PatientNode patient); //Function to create a new patient node that will be used for the patients AVL tree.
EmployeeNode* createEmployeeNode(EmployeeNode employee); //Function to create a new employee node that will be used for the employees AVL tree.

PatientNode* insertPatient(PatientNode* node, PatientNode* newPatient); //Function that inserts a patient into the patients AVL tree.
EmployeeNode* insertEmployee(EmployeeNode* node, EmployeeNode* newEmployee); //Function that inserts an employee into the employees AVL tree.

PatientNode* deletePatient(PatientNode* root, const char* firstName, const char* lastName); //Function to delete a patient from the patients AVL tree, as well as from the filepath holding all of their data.
EmployeeNode* deleteEmployee(EmployeeNode* root, const char* firstName, const char* lastName); //Function to delete an employee from the employees AVL tree, as well as from the filepath holding all of their data.

PatientNode* leftRotate(PatientNode* x); //Function that balances the patients AVL tree to the left if one is added to or removed from it.
EmployeeNode* leftRotate(EmployeeNode* x); //Function that balances the employees AVL tree to the left if one is added to or removed from it.

PatientNode* rightRotate(PatientNode* y); //Function that balances the patients AVL tree to the right if one is added to or removed from it.
EmployeeNode* rightRotate(EmployeeNode* y); //Function that balances the employees AVL tree to the right if one is added to or removed from it.


//Departmnent linked-list generating function, and patient and employee AVL tree-generating functions.
void loadPatients(const char* directory, PatientNode** patientRoot); //Function that reads through patient files and loads patient data into an AVL tree.
void loadEmployees(const char* directory, DepartmentNode** departmentHead); //Function that reads through employee files and loads employees into AVL trees associated with their spot in the departments linked list.
void addEmployeeToDepartment(DepartmentNode** head, const char* department, EmployeeNode* newEmployee); //Function that constructs a linked list of departments based on departments found in employees' data,--
//--then displays employees organized by department.
void deletePatientOrEmployee(const char* directoryPath); //Function that removes a patient or employee from their respective AVL tree, as well as from their respective filepath.


//AVL tree adjustment functions.
int height(PatientNode* node); //Function that gets the height of a patient node for the patients AVL tree.
int height(EmployeeNode* node); //Function that gets the height of an employee node for the patients AVL tree.

int getBalance(PatientNode* node); //Function to read the current balance status of the patient AVL tree.
int getBalance(EmployeeNode* node); //Function to read the current balance status of the employee AVL tree.


//Directory-editing functions.
void handleVisits(PatientNode* patient, const char* basePath); //Function that either displays visits, or adds a new visit for a patient.
void createDirectory(const char* path); //Function that creates a new patient or employee file in the designated filepath.

void updatePatientData(PatientNode* patient, const char* filename); //Function that propmts the user to edit existing patient data.
void writePatientData(const char* filename, const PatientNode* patient); //Function that appends edits from updatePatientData into the patient's file.
void readPatientData(const char* filename, PatientNode* patient); //Function that reads patient data from the filepath given to it.

void updateEmployeeData(EmployeeNode* employee, const char* filename); //Function that prompts the user to edit existing employee data.
void writeEmployeeData(const char* filename, const EmployeeNode* employee); //Function that appends edits from updateEmployeeData into the employee's file.
void readEmployeeData(const char* filename, EmployeeNode* employee); //Function that reads employee data from the filepath given to it. 


//Printing Functions.
void inOrderPrintPatients(PatientNode* root);
void printDepartments(DepartmentNode* head);
void inOrderPrintEmployees(EmployeeNode* root);

//UI and choice functions.
void promptAndProcessData(PatientNode** patientRoot, DepartmentNode** departmentHead); //Function that allows the user to view, add, search for, or remove patients or employees to and from their respective filepaths. 
void displayMenu(); //Function that prompts the user to work with subject data, check patients into the priority queue, process the queue, or free all loaded data and exit the program. 


//Queue functions.
void initializePriorityQueue(PriorityQueue* queue); //Function to begin the queue if it's empty.
void enqueuePatient(PriorityQueue* queue, PatientNode* patient); //Function to queue the next patient checked in.
PatientNode* dequeue(PriorityQueue* pq); //Dequeues next patient in the queue.
int isEmpty(PriorityQueue* pq); //Initializes a scanning operation that checks if the queue is empty.
void handlePatientCheckIn(PriorityQueue* queue, PatientNode** patientRoot); //Function that adds checked-in patients to the priority queue, and prompts the creation of a new patient file if none exists already.
void processQueue(PriorityQueue* queue); //Function that lets the user view everyone in the queue by calling displayQueue, see the next person in the queue, and dequeue the next person. 
void displayQueue(PriorityQueue* queue); //Function that shows everyone currently checked into the queue.

//CleanupFunctions
void cleanupPatientTree(PatientNode* root); //Function that frees all data from the patient AVL tree.
void freeEmployeeTree(EmployeeNode* root); //Function that frees all data from the employee AVL tree.
void cleanupDepartmentList(DepartmentNode* head); //Function that frees all allocated memory for the department linked list.
void cleanupQueue(PriorityQueue* pq); //Function to free the queue from working memory.


//Function to create a new PatientNode.
PatientNode* createPatientNode(PatientNode patient) {
    PatientNode* newNode = (PatientNode*)malloc(sizeof(PatientNode));
    if (newNode) {
        *newNode = patient;
        newNode->left = NULL;
        newNode->right = NULL;
        newNode->height = 1;  //New node has a height of 1.
    }
    return newNode;
}

//Function to create a new EmployeeNode.
EmployeeNode* createEmployeeNode(EmployeeNode employee) {
    EmployeeNode* newNode = (EmployeeNode*)malloc(sizeof(EmployeeNode));
    if (newNode) {
        *newNode = employee;
        newNode->left = NULL;
        newNode->right = NULL;
        newNode->height = 1;  //New node has a height of 1.
    }
    return newNode;
}

//Function to load patient data into the AVL tree.
void loadPatients(const char* directory, PatientNode** patientRoot) {
    WIN32_FIND_DATA findFileData; //WIN32_FIND_DATA is a necessary Windows API structure for storing file and directory information found in a directory search.
    char searchPath[MAX_LINE_LENGTH];
    snprintf(searchPath, sizeof(searchPath), "%s\\*", directory); //Search pattern for all files and subdirectories within the specified directory, in this case, the 'Patients' folder.
    HANDLE hFind = FindFirstFile(searchPath, &findFileData); //Start a file search in 'searchPath', then retrieve and store information about the first file or directory to 'findFileData.'

    if (hFind == INVALID_HANDLE_VALUE) { //Check if the 'hFind' file is valid.
        printf("Error opening directory: %s\n", directory);
        return;
    }

    do {
        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) { //Checks if 'findFileData' is a directory by checking if the 'FILE_ATTRIBUTE_DIRECTORY' flag sets off.
            
            if (strcmp(findFileData.cFileName, ".") != 0 && strcmp(findFileData.cFileName, "..") != 0) { //Skip the current '.' and parent '..' directories.
                
				//Build path to the individual patient folder.
                char patientFolder[MAX_LINE_LENGTH]; 
                snprintf(patientFolder, sizeof(patientFolder), "%s\\%s", directory, findFileData.cFileName); //Create a 'patientFolder' string that represents the full path to the patient's folder.

                //Build 'patientFile' that represents the full path to their file within their folder.
                char patientFile[MAX_LINE_LENGTH];
                snprintf(patientFile, sizeof(patientFile), "%s\\%s.txt", patientFolder, findFileData.cFileName); //The file within the folder shares the same name with '.txt' at the end of it.

                //Create a 'PatientNode' structure to store the patient's data.
                PatientNode patient;
                readPatientData(patientFile, &patient);

                //Insert the patient into the AVL tree.
                PatientNode* newPatient = createPatientNode(patient); //Create a new patient node using the 'patient' data, with a 'newPatient' pointer to the new node.
                *patientRoot = insertPatient(*patientRoot, newPatient); //Insert the patient into the patient AVL tree at '*patientRoot.' If the AVL tree is updated, '*patientRoot' is reassigned to the result of 'insertPatient.'
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0); //Loop thorugh all files in the search until there are no more.
    FindClose(hFind); //Close 'hFIND' and release all associated resources.
}

//Function to load employee data into the AVL tree. No comments because this is structured identically to 'loadPatients.'
void loadEmployees(const char* directory, DepartmentNode** departmentHead) {
    WIN32_FIND_DATA findFileData;
    char searchPath[MAX_LINE_LENGTH];
    snprintf(searchPath, sizeof(searchPath), "%s\\*", directory); 
    HANDLE hFind = FindFirstFile(searchPath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening directory: %s\n", directory);
        return;
    }

    do {
        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            
            if (strcmp(findFileData.cFileName, ".") != 0 && strcmp(findFileData.cFileName, "..") != 0) {
                
                char employeeFolder[MAX_LINE_LENGTH];
                snprintf(employeeFolder, sizeof(employeeFolder), "%s\\%s", directory, findFileData.cFileName);

               
                char employeeFile[MAX_LINE_LENGTH];
                snprintf(employeeFile, sizeof(employeeFile), "%s\\%s.txt", employeeFolder, findFileData.cFileName);

                
                EmployeeNode employee;
                readEmployeeData(employeeFile, &employee);

                
                EmployeeNode* newEmployee = createEmployeeNode(employee);
                addEmployeeToDepartment(departmentHead, employee.department, newEmployee); //This is the only line in this function different from 'loadPatients.'--
                //This uses the department extracted from 'readEmployeeData', and the employee's information stored in newEmployee to operate.
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0);
    FindClose(hFind);
}

//Function to add an employee to the department linked list.
void addEmployeeToDepartment(DepartmentNode** head, const char* department, EmployeeNode* newEmployee) { //Add an employee to a department in a linked list--
    //--set a parameter that is a pointer to a pointer to the head of the department linked list,--
    //--construct a string representing the department name, and a pointer to the new employee node to be added.
    
    DepartmentNode* current = *head; //Initialize a pointer to traverse the department linked list starting at the head. 
    while (current != NULL && strcmp(current->department, department) != 0) { //Look for a matching department in the list or end if NULL.
        current = current->next; //Move to the next deparment in the list.
    }
    if (current == NULL) { //Create a new DepartmentNode if no department was found.
        DepartmentNode* newDepartment = (DepartmentNode*)malloc(sizeof(DepartmentNode)); //Allocate the memory for a new 'DepartmentNode*.'
        strncpy(newDepartment->department, department, MAX_DEPARTMENT_LENGTH); //Copy department name to the DepartmentNode.
        newDepartment->employees = NULL; //Initialize the employee list for a new department.
        newDepartment->next = *head; //Link new department node to the beginning of the department list.
        *head = newDepartment; //Update the head of the list to the new node.
        current = newDepartment; //Point the new department
    }
    current->employees = insertEmployee(current->employees, newEmployee); //Insert new employee to the employee list for the current department.
}

//Function to get the balance factor of a PatientNode.
int getBalance(PatientNode* node) {
    return node ? height(node->left) - height(node->right) : 0; //Checks the difference in height between the right and left subtrees from root, called the balance factor of the node.
}

//Function to get the balance factor of an EmployeeNode.
int getBalance(EmployeeNode* node) {
    return node ? height(node->left) - height(node->right) : 0; //Identical implementation to the getBalance function for PatientNode*.
}

//Function to get the height of a PatientNode.
int height(PatientNode* node) {
    return node ? node->height : 0;
}

//Function to get the height of an EmployeeNode.
int height(EmployeeNode* node) {
    return node ? node->height : 0;
}

//Function to perform a right rotation on a PatientNode.
PatientNode* rightRotate(PatientNode* y) {
    PatientNode* x = y->left; //Sets x as the left child of y.
    PatientNode* T2 = x->right; //T2 is the right child of x. T2 is an unsubstantial name, just a placeholder.

    //Perform rotation.
    x->right = y; //x becomes the new root of the subtree, and y becomes the right child of x.
    y->left = T2; //T2 now becomes the left child of y.

    //Update heights.
    y->height = max(height(y->left), height(y->right)) + 1; //Height of y is determined as 1 plus the maximum height of its children.
    x->height = max(height(x->left), height(x->right)) + 1; //Height of x is updated in the same way.

    //Return new root.
    return x;
}

//Function to perform a left rotation on a PatientNode. Essentially the same as rightRotate, but mirrored.
PatientNode* leftRotate(PatientNode* x) {
    PatientNode* y = x->right; //Sets y as the right child of x.
    PatientNode* T2 = y->left; //Sets T2 as the left child of y.

    // Perform rotation
    y->left = x; //y becomes the new root of the subtree, and x becomes the left child of y.
    x->right = T2; //T2 becomes the right child of x.

    // Update heights
    x->height = max(height(x->left), height(x->right)) + 1; //Increase the height of x by 1 plus max height of its children.
    y->height = max(height(y->left), height(y->right)) + 1; //Determine height of y the same way. 

    //Return new root.
    return y;
}

//Function to perform a right rotation on an EmployeeNode. Operates identically to rightRotate of PatientNode*.
EmployeeNode* rightRotate(EmployeeNode* y) {
    EmployeeNode* x = y->left;
    EmployeeNode* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    return x;
}

//Function to perform a left rotation on an EmployeeNode. Operates identically to leftRotate of PatientNode*.
EmployeeNode* leftRotate(EmployeeNode* x) {
    EmployeeNode* y = x->right;
    EmployeeNode* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

//Function to insert a PatientNode into an AVL tree that will be occupied by a patient file within another function.
PatientNode* insertPatient(PatientNode* node, PatientNode* newPatient) {
    if (node == NULL) //Insert the new patient at the NULL location in the tree. 
        return newPatient;

	//This portion recursively determines to put the new patient on the left subtree or the right subtree based on alphabetical order.
    if (strcmp(newPatient->lastName, node->lastName) < 0) //If the new patient's last name comes before the last name of the patient at the current node-- 
        node->left = insertPatient(node->left, newPatient); //-- this recursively calls insertPatient on the left subtree.
    else if (strcmp(newPatient->lastName, node->lastName) > 0) //And if the new patient's last name comes after the last name of the patient at the current node--
        node->right = insertPatient(node->right, newPatient); //-- this recursively calls insertPatient on the right subtree.
    else
        return node;  //No duplicates allowed.

    node->height = 1 + max(height(node->left), height(node->right)); //Update height of the current node based on children's heights.

    int balance = getBalance(node); //Check if the tree is balanced.

    // Left Left Case
    if (balance > 1 && strcmp(newPatient->lastName, node->left->lastName) < 0) //If the left subtree is taller, and the new patient comes before current patient, rotate the tree right.
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && strcmp(newPatient->lastName, node->right->lastName) > 0) //If right subtree is taller, and the new patient comes after the current patientrotate left.
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && strcmp(newPatient->lastName, node->left->lastName) > 0) { //If the left subtree is taller, and the new patient comes after the current patient, rotate the tree right.
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && strcmp(newPatient->lastName, node->right->lastName) < 0) { //If the right subtree is taller, and the new patient comes before the current patient, rotate the tree left.
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

//Function to insert an EmployeeNode into an AVL tree. There are no comments in this one because it functions identically to insertPatient.
EmployeeNode* insertEmployee(EmployeeNode* node, EmployeeNode* newEmployee) {
    if (node == NULL)
        return newEmployee;

    if (strcmp(newEmployee->lastName, node->lastName) < 0)
        node->left = insertEmployee(node->left, newEmployee);
    else if (strcmp(newEmployee->lastName, node->lastName) > 0)
        node->right = insertEmployee(node->right, newEmployee);
    else
        return node;

    node->height = 1 + max(height(node->left), height(node->right));

    int balance = getBalance(node);

    // Left Left Case
    if (balance > 1 && strcmp(newEmployee->lastName, node->left->lastName) < 0)
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && strcmp(newEmployee->lastName, node->right->lastName) > 0)
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && strcmp(newEmployee->lastName, node->left->lastName) > 0) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && strcmp(newEmployee->lastName, node->right->lastName) < 0) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

//Function to delete a patient node from the AVL tree.
PatientNode* deletePatient(PatientNode* root, const char* firstName, const char* lastName) {
    if (root == NULL) return root; //If the tree is empty, return NULL.

    int cmp = strcmp(lastName, root->lastName); //Compare the last name passed to the function with the last name at the current node.
    if (cmp < 0) {
        root->left = deletePatient(root->left, firstName, lastName); //Recursively call this function on the left subtree if the last name is alphabetically before the current node's last name.
    } else if (cmp > 0) {
        root->right = deletePatient(root->right, firstName, lastName); //And recursively call this function on the right subtree if it's alphabetically after.
    } else { //Otherwise, if the last name passed to the function matches the current node's last name:
        int firstCmp = strcmp(firstName, root->firstName); //Compare the first name passed to the function with the first name value at the current root.
        if (firstCmp == 0) { //If the first name also matches:
            if (root->left == NULL || root->right == NULL) { //If the left or right subtree is NULL,
                PatientNode* temp = root->left ? root->left : root->right; //--set temp to the non-NULL child, or NULL if both are NULL.
                if (temp == NULL) { //If the current node has no children,
                    temp = root; //Store the current node in temp,
                    root = NULL; //And the current node becomes NULL.
                } else {
                    *root = *temp; //Otherwise, copy the non-NULL child into the current node.
                }
                free(temp); //Free the memory allocated for the original node..
            } else { //If the node has two children:
                PatientNode* temp = root->right; //Start by moving to the right child.
                while (temp->left != NULL) temp = temp->left; //Find the smallest node in the right subtree.
                strcpy(root->firstName, temp->firstName); //Copy the first name at the next successor to the current node.
                strcpy(root->lastName, temp->lastName); //Do the same for the last name.
                root->right = deletePatient(root->right, temp->firstName, temp->lastName); //Recursively delete the in-order successor from the right subtree.
            }

            //Remove the directory corresponding to the patient.
            char basePath[MAX_LINE_LENGTH];
            snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s",
                     firstName, lastName); //Construct a string variable the full path to the patient's directory.

            deletePatientOrEmployee(basePath); //Delete the patient's folder from the 'Patients' folder.
        }
    }

    if (root == NULL) return root; //If the root is NULL after deletion, return NULL.

    root->height = 1 + max(height(root->left), height(root->right)); //Recalculate the height of the current node.

    int balance = getBalance(root); //Get the balance of the current node.
    if (balance > 1 && getBalance(root->left) >= 0) return rightRotate(root); //If the node is left-heavy and the left child is balanced or left-heavy, perform a right rotation.
    if (balance > 1 && getBalance(root->left) < 0) { //If the node is left-heavy but the left child is right-heavy:
        root->left = leftRotate(root->left); //Rotate the left child to the left,
        return rightRotate(root); //then perform a right rotation on the current node.
    }
    if (balance < -1 && getBalance(root->right) <= 0) return leftRotate(root); //If the node is right-heavy and the right child is balanced or right-heavy, perform a left rotation.
    if (balance < -1 && getBalance(root->right) > 0) { //If the node is right-heavy but the right child is left-heavy:
        root->right = rightRotate(root->right); //Rotate the right child to the right,
        return leftRotate(root); //Then perform a left rotation on the current node.
    }

    return root; //Return the root of the subtree.
}

//Function to delete an employee node from the AVL tree.
EmployeeNode* deleteEmployee(EmployeeNode* root, const char* firstName, const char* lastName) { //There are no comments since this function operates identically to the deletePatient pointer function.
    if (root == NULL) return root;

    int cmp = strcmp(lastName, root->lastName);
    if (cmp < 0) {
        root->left = deleteEmployee(root->left, firstName, lastName);
    } else if (cmp > 0) {
        root->right = deleteEmployee(root->right, firstName, lastName);
    } else {
        if (strcmp(firstName, root->firstName) == 0) {
            if (root->left == NULL || root->right == NULL) {
                EmployeeNode* temp = root->left ? root->left : root->right;
                if (temp == NULL) {
                    temp = root;
                    root = NULL;
                } else {
                    *root = *temp;
                }
                free(temp);
            } else {
                EmployeeNode* temp = root->right;
                while (temp->left != NULL) temp = temp->left;
                strcpy(root->firstName, temp->firstName);
                strcpy(root->lastName, temp->lastName);
                root->right = deleteEmployee(root->right, temp->firstName, temp->lastName);
            }

            char basePath[MAX_LINE_LENGTH];
            snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Employees/%s_%s",
                     firstName, lastName);

            deletePatientOrEmployee(basePath); 
        }
    }

    if (root == NULL) return root;

    root->height = 1 + max(height(root->left), height(root->right));

    int balance = getBalance(root);
    if (balance > 1 && getBalance(root->left) >= 0) return rightRotate(root);
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    if (balance < -1 && getBalance(root->right) <= 0) return leftRotate(root);
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

//Function to create a directory (Windows-specific).
void createDirectory(const char* path) {
    if (_mkdir(path) != 0) { //Makes a new directory in the located path if one with the specified title does not already exist in it.
        if (errno != EEXIST) { //If the error is unrelated to the directory already existing. 
            printf("Error creating directory: %s\n", path);
        }
    }
}

void deletePatientOrEmployee(const char* path) {
    DIR* dir = opendir(path); //Open the directory using the 'opendir' function, which returns a 'DIR*' pointer that iterates over the entries in the directory.
    struct dirent* ent; //Declares a pointer 'ent' of a 'dirent' structure that represents a directory entry within the current directory.
    if (dir) { //Ensure 'dir' is not NULL.
        while ((ent = readdir(dir)) != NULL) { //While the directory is not empty, or the next spot in the directory isn't:
            struct stat st; //Declare a 'stat' structure named 'st' that holds information about the current directory.
            char fullPath[MAX_LINE_LENGTH];
            snprintf(fullPath, sizeof(fullPath), "%s/%s", path, ent->d_name); //Construct a string that represents the full path to the current directory.
            stat(fullPath, &st); //Store information about the file or directory in the 'st' structure.
            if (S_ISREG(st.st_mode)) { //Checks if the current directory entry is a regular file using the 'S_ISREG' macro to test the file type stored in 'st.st_mode.'
                remove(fullPath);  //Remove the file specified by 'fullpath.'
            } else if (S_ISDIR(st.st_mode)) { //Checks if current directory entry is a directory using the 'S_ISDIR' macro to test the file type stored in 'st.st_mode.'
                if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0) { //Make sure the current directory is not the special entries of '.' or '..'
                    deletePatientOrEmployee(fullPath);  //Recursively delete files and subdirectories within the directory.
                    rmdir(fullPath);  //Remove the now-empty directory itself.
                }
            }
        }
        closedir(dir); //Release any resources associated with the directory stream.
    }
    rmdir(path);  //Remove the main directory after all its directories have been recursively deleted.
}

//Function to search for a PatientNode in an AVL tree.
PatientNode* searchPatient(PatientNode* root, const char* firstName, const char* lastName) {
    if (root == NULL) { //If the tree is empty or the patient is not found, return NULL.
        return NULL;
    }
    int cmp = strcmp(lastName, root->lastName);
    if (cmp == 0) { //If the last name matches the current node's last name, check the first name.
        int firstCmp = strcmp(firstName, root->firstName);
        if (firstCmp == 0) { //And if the first name also matches, the patient is found and we return the current node.
            return root;
        }
        return NULL; //If the first name doesn't match, return NULL.
    } else if (cmp < 0) { //If the last name is alphabetically less than the current node's last name--
        return searchPatient(root->left, firstName, lastName); //--search the left subtree.
    } else { //And if it's alphabetically more--
        return searchPatient(root->right, firstName, lastName); //--search the right subtree. 
    }
}

//Function to search for an EmployeeNode in an AVL tree. No comments provided because it functions identically to searchPatient.
EmployeeNode* searchEmployee(EmployeeNode* root, const char* firstName, const char* lastName) {
    if (root == NULL) {
        return NULL;
    }
    int cmp = strcmp(lastName, root->lastName);
    if (cmp == 0) {
        if (strcmp(firstName, root->firstName) == 0) {
            return root;
        }
        return NULL;
    } else if (cmp < 0) {
        return searchEmployee(root->left, firstName, lastName);
    } else {
        return searchEmployee(root->right, firstName, lastName);
    }
}

//Function to read patient data from a file.
void readPatientData(const char* filename, PatientNode* patient) {
    FILE* file = fopen(filename, "r"); //Open the file associated with the Patient filepath passed to the function.
    if (file) {
        fgets(patient->firstName, MAX_NAME_LENGTH, file); 
        patient->firstName[strcspn(patient->firstName, "\n")] = '\0';
        fgets(patient->lastName, MAX_NAME_LENGTH, file); 
        patient->lastName[strcspn(patient->lastName, "\n")] = '\0';
        fgets(patient->dateOfBirth, MAX_DOB_LENGTH, file); 
        patient->dateOfBirth[strcspn(patient->dateOfBirth, "\n")] = '\0';
        fgets(patient->gender, MAX_GENDER_LENGTH, file); 
        patient->gender[strcspn(patient->gender, "\n")] = '\0';
        fgets(patient->address, MAX_ADDRESS_LENGTH, file); 
        patient->address[strcspn(patient->address, "\n")] = '\0';
        fgets(patient->phone, MAX_PHONE_LENGTH, file); 
        patient->phone[strcspn(patient->phone, "\n")] = '\0';
        fgets(patient->email, MAX_EMAIL_LENGTH, file); 
        patient->email[strcspn(patient->email, "\n")] = '\0';
        fgets(patient->bloodType, MAX_BLOOD_TYPE_LENGTH, file); 
        patient->bloodType[strcspn(patient->bloodType, "\n")] = '\0';
        fgets(patient->ssn, MAX_SSN_LENGTH, file); 
        patient->ssn[strcspn(patient->ssn, "\n")] = '\0';
        fscanf(file, "%d", &patient->patientID);
        fclose(file);
    } else {
        printf("Error reading patient file.\n");
    }
}

//Function to read employee data from a file.
void readEmployeeData(const char* filename, EmployeeNode* employee) { //Functions identically to the readPatientData function, with the only difference being the data printed out.
    FILE* file = fopen(filename, "r");
    if (file) {
        fgets(employee->firstName, MAX_NAME_LENGTH, file); employee->firstName[strcspn(employee->firstName, "\n")] = '\0';
        fgets(employee->lastName, MAX_NAME_LENGTH, file); employee->lastName[strcspn(employee->lastName, "\n")] = '\0';
        fgets(employee->dateOfBirth, MAX_DOB_LENGTH, file); employee->dateOfBirth[strcspn(employee->dateOfBirth, "\n")] = '\0';
        fgets(employee->gender, MAX_GENDER_LENGTH, file); employee->gender[strcspn(employee->gender, "\n")] = '\0';
        fgets(employee->address, MAX_ADDRESS_LENGTH, file); employee->address[strcspn(employee->address, "\n")] = '\0';
        fgets(employee->phone, MAX_PHONE_LENGTH, file); employee->phone[strcspn(employee->phone, "\n")] = '\0';
        fgets(employee->email, MAX_EMAIL_LENGTH, file); employee->email[strcspn(employee->email, "\n")] = '\0';
        fgets(employee->ssn, MAX_SSN_LENGTH, file); employee->ssn[strcspn(employee->ssn, "\n")] = '\0';
        fgets(employee->position, MAX_POSITION_LENGTH, file); employee->position[strcspn(employee->position, "\n")] = '\0';
        fgets(employee->department, MAX_DEPARTMENT_LENGTH, file); employee->department[strcspn(employee->department, "\n")] = '\0';
        fgets(employee->employeeID, MAX_EMPLOYEE_ID_LENGTH, file); employee->employeeID[strcspn(employee->employeeID, "\n")] = '\0';
        fgets(employee->salary, MAX_LINE_LENGTH, file); employee->salary[strcspn(employee->salary, "\n")] = '\0';
        fgets(employee->dateOfHire, MAX_DOB_LENGTH, file); employee->dateOfHire[strcspn(employee->dateOfHire, "\n")] = '\0';
        fclose(file);
    } else {
        printf("Error reading employee file.\n");
    }
}

//Function to write patient data to a file.
void writePatientData(const char* filename, const PatientNode* patient) { 
    FILE* file = fopen(filename, "w"); //Write to a .txt file at the filepath passed to the function, with all the patient data associated with the patient argument passed to the function.
    if (file) {
        fprintf(file, "%s\n", patient->firstName);
        fprintf(file, "%s\n", patient->lastName);
        fprintf(file, "%s\n", patient->dateOfBirth);
        fprintf(file, "%s\n", patient->gender);
        fprintf(file, "%s\n", patient->address);
        fprintf(file, "%s\n", patient->phone);
        fprintf(file, "%s\n", patient->email);
        fprintf(file, "%s\n", patient->bloodType);
        fprintf(file, "%s\n", patient->ssn);
        fprintf(file, "%d\n", patient->patientID);
        fclose(file);
    } else {
        printf("Error creating patient file.\n");
    }
}

//Function to write employee data to a file.
void writeEmployeeData(const char* filename, const EmployeeNode* employee) { //Operates identically to the writePatientData function.
    FILE* file = fopen(filename, "w");
    if (file) {
        fprintf(file, "%s\n", employee->firstName);
        fprintf(file, "%s\n", employee->lastName);
        fprintf(file, "%s\n", employee->dateOfBirth);
        fprintf(file, "%s\n", employee->gender);
        fprintf(file, "%s\n", employee->address);
        fprintf(file, "%s\n", employee->phone);
        fprintf(file, "%s\n", employee->email);
        fprintf(file, "%s\n", employee->ssn);
        fprintf(file, "%s\n", employee->position);
        fprintf(file, "%s\n", employee->department);
        fprintf(file, "%s\n", employee->employeeID);
        fprintf(file, "%s\n", employee->salary);
        fprintf(file, "%s\n", employee->dateOfHire);
        fclose(file);
    } else {
        printf("Error creating employee file.\n");
    }
}

//Function to update patient data and write it back to the file.
void updatePatientData(PatientNode* patient, const char* filename) {
    char choice[10];
    int fieldToChange;

    while (1) { //Continuously prompt the user for data to update until they exit the function by selecting 'b' for back.
        printf("\nHere is all the patient's data:\n"); //Display all the data in the file. Each line has the proper header, the information for the patient relating to the header, then the next line, for all the data.
        printf("1. First Name: %s\n", patient->firstName);
        printf("2. Last Name: %s\n", patient->lastName);
        printf("3. Date of Birth: %s\n", patient->dateOfBirth);
        printf("4. Gender: %s\n", patient->gender);
        printf("5. Address: %s\n", patient->address);
        printf("6. Phone: %s\n", patient->phone);
        printf("7. Email: %s\n", patient->email);
        printf("8. Blood Type: %s\n", patient->bloodType);
        printf("9. SSN: %s\n", patient->ssn);
        printf("10. Patient ID: %d\n", patient->patientID);

        printf("\nWhich detail would you like to change? (Enter the number or 'b' for back): ");
        fgets(choice, sizeof(choice), stdin);
        choice[strcspn(choice, "\n")] = '\0';

        if (strcmp(choice, "b") == 0) { //Go back to the last choice.
            return;
        }

        fieldToChange = atoi(choice); //Convert a string number into an integer variable.

        switch (fieldToChange) { //The number the user typed is associated with the line representing the data they chose.
            case 1:
                printf("Enter new First Name: ");
                fgets(patient->firstName, MAX_NAME_LENGTH, stdin); //Grab what data they updated for this piece of information.
                patient->firstName[strcspn(patient->firstName, "\n")] = '\0'; //Construct a string variable for this piece of data that houses the new information.
                break; //Same process for all the next pieces of information that they would have chosen.
            case 2:
                printf("Enter new Last Name: ");
                fgets(patient->lastName, MAX_NAME_LENGTH, stdin);
                patient->lastName[strcspn(patient->lastName, "\n")] = '\0';
                break;
            case 3:
                printf("Enter new Date of Birth (YYYY-MM-DD): ");
                fgets(patient->dateOfBirth, MAX_DOB_LENGTH, stdin);
                patient->dateOfBirth[strcspn(patient->dateOfBirth, "\n")] = '\0';
                break;
            case 4:
                printf("Enter new Gender: ");
                fgets(patient->gender, MAX_GENDER_LENGTH, stdin);
                patient->gender[strcspn(patient->gender, "\n")] = '\0';
                break;
            case 5:
                printf("Enter new Address: ");
                fgets(patient->address, MAX_ADDRESS_LENGTH, stdin);
                patient->address[strcspn(patient->address, "\n")] = '\0';
                break;
            case 6:
                printf("Enter new Phone: ");
                fgets(patient->phone, MAX_PHONE_LENGTH, stdin);
                patient->phone[strcspn(patient->phone, "\n")] = '\0';
                break;
            case 7:
                printf("Enter new Email: ");
                fgets(patient->email, MAX_EMAIL_LENGTH, stdin);
                patient->email[strcspn(patient->email, "\n")] = '\0';
                break;
            case 8:
                printf("Enter new Blood Type: ");
                fgets(patient->bloodType, MAX_BLOOD_TYPE_LENGTH, stdin);
                patient->bloodType[strcspn(patient->bloodType, "\n")] = '\0';
                break;
            case 9:
                printf("Enter new SSN (XXX-XX-XXXX): ");
                fgets(patient->ssn, MAX_SSN_LENGTH, stdin);
                patient->ssn[strcspn(patient->ssn, "\n")] = '\0';
                break;
            case 10:
                printf("Enter new Patient ID: ");
                scanf("%d", &patient->patientID);
                getchar();  //Clear newline character left by scanf.
                break;
            default:
                printf("Invalid choice. Please try again.\n");
                continue; //Reprompt the user for a valid field to change if they put something out of the bounts of 1 to 10.
        }

        writePatientData(filename, patient); //Run the writePatientData function with the updated information.
        printf("Patient data updated successfully.\n"); 
    } //Reprompt for the choice until the user selects to go back.
}

//Function to update employee data and write it back to the file.
void updateEmployeeData(EmployeeNode* employee, const char* filename) { //This function works identically to the 'updatePatientData' function, but for employee data.
    char choice[10];
    int fieldToChange;

    while (1) {
        printf("\nHere is all the employee's data:\n");
        printf("1. First Name: %s\n", employee->firstName);
        printf("2. Last Name: %s\n", employee->lastName);
        printf("3. Date of Birth: %s\n", employee->dateOfBirth);
        printf("4. Gender: %s\n", employee->gender);
        printf("5. Address: %s\n", employee->address);
        printf("6. Phone: %s\n", employee->phone);
        printf("7. Email: %s\n", employee->email);
        printf("8. SSN: %s\n", employee->ssn);
        printf("9. Position: %s\n", employee->position);
        printf("10. Department: %s\n", employee->department);
        printf("11. Employee ID: %s\n", employee->employeeID);
        printf("12. Salary: %s\n", employee->salary);
        printf("13. Date of Hire: %s\n", employee->dateOfHire);

        printf("\nWhich detail would you like to change? (Enter the number or 'b' for back): ");
        fgets(choice, sizeof(choice), stdin);
        choice[strcspn(choice, "\n")] = '\0';

        if (strcmp(choice, "b") == 0) {
            return;
        }

        fieldToChange = atoi(choice);

        switch (fieldToChange) {
            case 1:
                printf("Enter new First Name: ");
                fgets(employee->firstName, MAX_NAME_LENGTH, stdin);
                employee->firstName[strcspn(employee->firstName, "\n")] = '\0';
                break;
            case 2:
                printf("Enter new Last Name: ");
                fgets(employee->lastName, MAX_NAME_LENGTH, stdin);
                employee->lastName[strcspn(employee->lastName, "\n")] = '\0';
                break;
            case 3:
                printf("Enter new Date of Birth (YYYY-MM-DD): ");
                fgets(employee->dateOfBirth, MAX_DOB_LENGTH, stdin);
                employee->dateOfBirth[strcspn(employee->dateOfBirth, "\n")] = '\0';
                break;
            case 4:
                printf("Enter new Gender: ");
                fgets(employee->gender, MAX_GENDER_LENGTH, stdin);
                employee->gender[strcspn(employee->gender, "\n")] = '\0';
                break;
            case 5:
                printf("Enter new Address: ");
                fgets(employee->address, MAX_ADDRESS_LENGTH, stdin);
                employee->address[strcspn(employee->address, "\n")] = '\0';
                break;
            case 6:
                printf("Enter new Phone: ");
                fgets(employee->phone, MAX_PHONE_LENGTH, stdin);
                employee->phone[strcspn(employee->phone, "\n")] = '\0';
                break;
            case 7:
                printf("Enter new Email: ");
                fgets(employee->email, MAX_EMAIL_LENGTH, stdin);
                employee->email[strcspn(employee->email, "\n")] = '\0';
                break;
            case 8:
                printf("Enter new SSN (XXX-XX-XXXX): ");
                fgets(employee->ssn, MAX_SSN_LENGTH, stdin);
                employee->ssn[strcspn(employee->ssn, "\n")] = '\0';
                break;
            case 9:
                printf("Enter new Position: ");
                fgets(employee->position, MAX_POSITION_LENGTH, stdin);
                employee->position[strcspn(employee->position, "\n")] = '\0';
                break;
            case 10:
                printf("Enter new Department: ");
                fgets(employee->department, MAX_DEPARTMENT_LENGTH, stdin);
                employee->department[strcspn(employee->department, "\n")] = '\0';
                break;
            case 11:
                printf("Enter new Employee ID: ");
                fgets(employee->employeeID, MAX_EMPLOYEE_ID_LENGTH, stdin);
                employee->employeeID[strcspn(employee->employeeID, "\n")] = '\0';
                break;
            case 12:
                printf("Enter new Salary: ");
                fgets(employee->salary, MAX_LINE_LENGTH, stdin);
                employee->salary[strcspn(employee->salary, "\n")] = '\0';
                break;
            case 13:
                printf("Enter new Date of Hire (YYYY-MM-DD): ");
                fgets(employee->dateOfHire, MAX_DOB_LENGTH, stdin);
                employee->dateOfHire[strcspn(employee->dateOfHire, "\n")] = '\0';
                break;
            default:
                printf("Invalid choice. Please try again.\n");
                continue;
        }

        //Save updated employee data.
        writeEmployeeData(filename, employee);
        printf("Employee data updated successfully.\n");
    }
}

//Function to list all patients or employees.
void listAllAndSelect(PatientNode* patientRoot, DepartmentNode* departmentHead, int isPatient) {
    if (isPatient) { //If we are working with patient data,--
        inOrderPrintPatients(patientRoot); //Print the patients in alphabetical order.
    } else { //Otherwise,--
        printDepartments(departmentHead); //Print departments in the hospital with each employee under each department.
    }
}

//Function to recursively print patients in order (in-order traversal).
void inOrderPrintPatients(PatientNode* root) {
    if (root != NULL) { //This recursively processes the left subtree, the current node, and then the right subtree. Once it finds a NULL value, it goes back to the last call that was processing the last--
	//--unprocessed node and proceeds through the loop.
        inOrderPrintPatients(root->left); //Start at root, continue left until reaching NULL.
        printf("First Name: %s, Last Name: %s, Date of Birth: %s\n", root->firstName, root->lastName, root->dateOfBirth); //Once left subtree is complete, print current node.
        inOrderPrintPatients(root->right); //Then print the right subtree.
    } //So it begins processing at the root node, and recursively calls the entire left subtree to print it, print the root node, then the entire right subtree in the same recursive fashion.
}

//Function to print all departments and their employees.
void printDepartments(DepartmentNode* head) {
    DepartmentNode* current = head; //Start at the beggining of the list.
    while (current != NULL) { //Iterate through each node in the list.
        printf("Department: %s\n", current->department); //Print current DepartmentNode's value.
        inOrderPrintEmployees(current->employees); //Print the employees in that department.
        current = current->next; //Move to the next node in the list.
    }
}

//Function to print employees in order (in-order traversal). This operates identcally to inOrderPrintPatients.
void inOrderPrintEmployees(EmployeeNode* root) {
    if (root != NULL) {
        inOrderPrintEmployees(root->left);
        printf("First Name: %s, Last Name: %s, Position: %s\n", root->firstName, root->lastName, root->position);
        inOrderPrintEmployees(root->right);
    }
}

//Core function of the program that handles patient and employee data viewing and manipulation outside of the queue.
void promptAndProcessData(PatientNode** patientRoot, DepartmentNode** departmentHead) {
    char firstName[MAX_NAME_LENGTH]; //First part of the search operation.
    char lastName[MAX_NAME_LENGTH]; //Second part of the search operation.
    char choice; //This function works by asking the user what they want to do.
    int isPatient; //If we are working with patient data, then patient functions are implemented, and vice versa for employee data.

    while (1) {
        printf("\nAre you working with patient or employee data? (p/e) [b for back]: ");
        scanf(" %c", &choice);
        getchar();  //Clear the newline character.

        if (choice == 'p') { //If choice is 'p', 'isPatient' is true.
            isPatient = 1;
            break;
        } else if (choice == 'e') { //If choice is 'e', 'isPatient' is false.
            isPatient = 0;
            break;
        } else if (choice == 'b') { //If choice is 'b', we go back to the last page.
            return;
        } else {
            printf("Invalid choice. Please try again.\n");
        }
    }

    while (1) {
        printf("\nWould you like to view all, add one, search for one, or delete one? (v/a/s/d) [b for back]: ");
        scanf(" %c", &choice);
        getchar();

        if (choice == 'v') {
            listAllAndSelect(*patientRoot, *departmentHead, isPatient); //Run the 'listAllAndSelect' function if they want to view all. Patients or employees are determined by the truth value of 'isPatient.'
            continue;  //Go back to the main options after listing.
        } else if (choice == 'a') { //Adding a new patient or employee.
            printf("Enter the first name: "); //Begins the process of creating a new directory in the proper filepath based on first and last name.
            fgets(firstName, MAX_NAME_LENGTH, stdin);
            firstName[strcspn(firstName, "\n")] = '\0'; 

            printf("Enter the last name: ");
            fgets(lastName, MAX_NAME_LENGTH, stdin);
            lastName[strcspn(lastName, "\n")] = '\0';

            if (isPatient) { //If working with patient data, prompt for these next pieces of personal information about the patient.
                PatientNode patient;
                strcpy(patient.firstName, firstName);
                strcpy(patient.lastName, lastName);

                printf("Enter date of birth (YYYY-MM-DD): ");
                fgets(patient.dateOfBirth, MAX_DOB_LENGTH, stdin);
                patient.dateOfBirth[strcspn(patient.dateOfBirth, "\n")] = '\0';

                printf("Enter gender: ");
                fgets(patient.gender, MAX_GENDER_LENGTH, stdin);
                patient.gender[strcspn(patient.gender, "\n")] = '\0';

                printf("Enter address: ");
                fgets(patient.address, MAX_ADDRESS_LENGTH, stdin);
                patient.address[strcspn(patient.address, "\n")] = '\0';

                printf("Enter phone number: ");
                fgets(patient.phone, MAX_PHONE_LENGTH, stdin);
                patient.phone[strcspn(patient.phone, "\n")] = '\0';

                printf("Enter email: ");
                fgets(patient.email, MAX_EMAIL_LENGTH, stdin);
                patient.email[strcspn(patient.email, "\n")] = '\0';

                printf("Enter blood type: ");
                fgets(patient.bloodType, MAX_BLOOD_TYPE_LENGTH, stdin);
                patient.bloodType[strcspn(patient.bloodType, "\n")] = '\0';

                printf("Enter SSN (XXX-XX-XXXX): ");
                fgets(patient.ssn, MAX_SSN_LENGTH, stdin);
                patient.ssn[strcspn(patient.ssn, "\n")] = '\0';

                printf("Enter patient ID: ");
                scanf("%d", &patient.patientID);
                getchar();

                PatientNode* newPatient = createPatientNode(patient); //Function to create a new PatientNode with all this information.
                *patientRoot = insertPatient(*patientRoot, newPatient); //Insert this patient into the existing AVL tree.
                char basePath[MAX_LINE_LENGTH];
                snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s", firstName, lastName); //Create a 'basePath' string that will be used to make a folder--
				//--after the patient's name.
                _mkdir(basePath); //Make a new folder in the 'Patients' folder named after the patient.
                char filename[MAX_LINE_LENGTH];
                snprintf(filename, sizeof(filename), "%s/%s_%s.txt", basePath, firstName, lastName); //Make a string representing the filename to the .txt file that will be created after the patient's name,--
				//--which will hold all of their data.
                writePatientData(filename, newPatient); //Write the patient's data into the .txt file at the filepath specified in the previous line.
                printf("Patient added and file created successfully.\n");
            } else { //Do everything that we just did for patients, except for an employee with the specified employee information.
                EmployeeNode employee;
                strcpy(employee.firstName, firstName);
                strcpy(employee.lastName, lastName);

                printf("Enter date of birth (YYYY-MM-DD): ");
                fgets(employee.dateOfBirth, MAX_DOB_LENGTH, stdin);
                employee.dateOfBirth[strcspn(employee.dateOfBirth, "\n")] = '\0';

                printf("Enter gender: ");
                fgets(employee.gender, MAX_GENDER_LENGTH, stdin);
                employee.gender[strcspn(employee.gender, "\n")] = '\0';

                printf("Enter address: ");
                fgets(employee.address, MAX_ADDRESS_LENGTH, stdin);
                employee.address[strcspn(employee.address, "\n")] = '\0';

                printf("Enter phone number: ");
                fgets(employee.phone, MAX_PHONE_LENGTH, stdin);
                employee.phone[strcspn(employee.phone, "\n")] = '\0';

                printf("Enter email: ");
                fgets(employee.email, MAX_EMAIL_LENGTH, stdin);
                employee.email[strcspn(employee.email, "\n")] = '\0';

                printf("Enter SSN (XXX-XX-XXXX): ");
                fgets(employee.ssn, MAX_SSN_LENGTH, stdin);
                employee.ssn[strcspn(employee.ssn, "\n")] = '\0';

                printf("Enter position: ");
                fgets(employee.position, MAX_POSITION_LENGTH, stdin);
                employee.position[strcspn(employee.position, "\n")] = '\0';

                printf("Enter department: ");
                fgets(employee.department, MAX_DEPARTMENT_LENGTH, stdin);
                employee.department[strcspn(employee.department, "\n")] = '\0';

                printf("Enter employee ID: ");
                fgets(employee.employeeID, MAX_EMPLOYEE_ID_LENGTH, stdin);
                employee.employeeID[strcspn(employee.employeeID, "\n")] = '\0';

                printf("Enter salary: ");
                fgets(employee.salary, MAX_LINE_LENGTH, stdin);
                employee.salary[strcspn(employee.salary, "\n")] = '\0';

                printf("Enter date of hire (YYYY-MM-DD): ");
                fgets(employee.dateOfHire, MAX_DOB_LENGTH, stdin);
                employee.dateOfHire[strcspn(employee.dateOfHire, "\n")] = '\0';

                EmployeeNode* newEmployee = createEmployeeNode(employee); //Identical to patients portion.
                addEmployeeToDepartment(departmentHead, employee.department, newEmployee);
                char basePath[MAX_LINE_LENGTH];
                snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Employees/%s_%s", firstName, lastName);
                _mkdir(basePath);
                char filename[MAX_LINE_LENGTH];
                snprintf(filename, sizeof(filename), "%s/%s_%s.txt", basePath, firstName, lastName);
                writeEmployeeData(filename, newEmployee);
                printf("Employee added and file created successfully.\n");
            }
            continue;  //Go back to the main options after adding.
        } else if (choice == 's') { //Operation to look through the existing directory and find either a patient or employee based on their first and last name.
            printf("Enter the first name: ");
            fgets(firstName, MAX_NAME_LENGTH, stdin);
            firstName[strcspn(firstName, "\n")] = '\0'; //Enter first name exactly as it's stored.

            printf("Enter the last name: ");
            fgets(lastName, MAX_NAME_LENGTH, stdin);
            lastName[strcspn(lastName, "\n")] = '\0'; //Enter last name exactly as it's stored.

            if (isPatient) { //If working with patients.
                PatientNode* foundPatient = searchPatient(*patientRoot, firstName, lastName); //Search through patients for that first and last name.
                if (foundPatient) { //If that patient's first and last name were found:
                    printf("Patient found. Would you like to view or update it? (v/u) [b for back]: ");
                    while (1) { //Give the user a choice to view or update the patient's data.
                        scanf(" %c", &choice);
                        getchar();

                        if (choice == 'v') { //Display all the patient's saved personal data.
                            printf("Patient Data:\n");
                            printf("First Name: %s\n", foundPatient->firstName);
                            printf("Last Name: %s\n", foundPatient->lastName);
                            printf("Date of Birth: %s\n", foundPatient->dateOfBirth);
                            printf("Gender: %s\n", foundPatient->gender);
                            printf("Address: %s\n", foundPatient->address);
                            printf("Phone: %s\n", foundPatient->phone);
                            printf("Email: %s\n", foundPatient->email);
                            printf("Blood Type: %s\n", foundPatient->bloodType);
                            printf("SSN: %s\n", foundPatient->ssn);
                            printf("Patient ID: %d\n", foundPatient->patientID);
                            break;
                        } else if (choice == 'u') { //Give the user the option to change personal data of the patient, or add a new/view previous visits.
                            while (1) {
                                printf("Would you like to update information or handle visits? (u/v) [b for back]: ");
                                scanf(" %c", &choice);
                                getchar(); 

                                if (choice == 'u') { //If the user wants to update the patient's data:
                                    char basePath[MAX_LINE_LENGTH]; //Initialize a basePath character.
                                    snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s", firstName, lastName); //Set the basePath equal to a string representing--
									//--the folder location for the patient data.
                                    char filename[MAX_LINE_LENGTH]; //Initialize a filename character.
                                    snprintf(filename, sizeof(filename), "%s/%s_%s.txt", basePath, firstName, lastName); //Set filename equal to a string representing the path to the .txt file holding the patient's data.
                                    updatePatientData(foundPatient, filename); //Run the updatePatientData function for this patient at that file.
                                } else if (choice == 'v') { 
                                    char basePath[MAX_LINE_LENGTH];
                                    snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s", firstName, lastName); //Do the first half of the 'u' choice.
                                    handleVisits(foundPatient, basePath); //Run the handleVisits function for that patient at that patients folder's basePath.
                                    break;
                                } else if (choice == 'b') {
                                    return;
                                } else {
                                    printf("Invalid choice. Please try again.\n");
                                }
                            }
                            break;
                        } else if (choice == 'b') {
                            return;
                        } else {
                            printf("Invalid choice. Please try again.\n");
                        }
                    }
                } else {
                    printf("Patient not found.\n");
                }
            } else { //Else if working with employees.
                //Check if departmentHead is NULL.
                if (*departmentHead == NULL) {
                    printf("No departments loaded.\n");
                    return;
                }

                EmployeeNode* foundEmployee = searchEmployee((*departmentHead)->employees, firstName, lastName); //Run the searchEmployee function, which sorts by department.
                if (foundEmployee) { //At this point
                    printf("Employee found. Would you like to view or update it? (v/u) [b for back]: "); //By this point, this functions identically to searching for a patient. The only difference is the data that's stored.
                    while (1) {
                        scanf(" %c", &choice);
                        getchar();  

                        if (choice == 'v') {
                            printf("Employee Data:\n");
                            printf("First Name: %s\n", foundEmployee->firstName);
                            printf("Last Name: %s\n", foundEmployee->lastName);
                            printf("Date of Birth: %s\n", foundEmployee->dateOfBirth);
                            printf("Gender: %s\n", foundEmployee->gender);
                            printf("Address: %s\n", foundEmployee->address);
                            printf("Phone: %s\n", foundEmployee->phone);
                            printf("Email: %s\n", foundEmployee->email);
                            printf("SSN: %s\n", foundEmployee->ssn);
                            printf("Position: %s\n", foundEmployee->position);
                            printf("Department: %s\n", foundEmployee->department);
                            printf("Employee ID: %s\n", foundEmployee->employeeID);
                            printf("Salary: %s\n", foundEmployee->salary);
                            printf("Date of Hire: %s\n", foundEmployee->dateOfHire);
                            break;
                        } else if (choice == 'u') {
                            char basePath[MAX_LINE_LENGTH];
                            snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Employees/%s_%s", firstName, lastName);
                            char filename[MAX_LINE_LENGTH];
                            snprintf(filename, sizeof(filename), "%s/%s_%s.txt", basePath, firstName, lastName);
                            updateEmployeeData(foundEmployee, filename);
                            break;
                        } else if (choice == 'b') { //Go back to the last menu.
                            return;
                        } else {
                            printf("Invalid choice. Please try again.\n");
                        }
                    }
                } else {
                    printf("Employee not found.\n");
                }
            }
            continue;  //Go back to the main options after searching.
        } else if (choice == 'd') { //Delete a patient or employee from the AVL tree, as well as the directory holding all of their information.
            printf("Enter the first name: "); //Search for them by first and last name, just as in the search choice.
            fgets(firstName, MAX_NAME_LENGTH, stdin);
            firstName[strcspn(firstName, "\n")] = '\0';

            printf("Enter the last name: ");
            fgets(lastName, MAX_NAME_LENGTH, stdin);
            lastName[strcspn(lastName, "\n")] = '\0';

            if (isPatient) {
                *patientRoot = deletePatient(*patientRoot, firstName, lastName); //Run the deletePatient function to remove them from the AVL tree.
                char basePath[MAX_LINE_LENGTH];
                snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s", firstName, lastName);
                _rmdir(basePath); //Delete the folder for that patient containing all of their information.
                printf("Patient %s %s deleted.\n", firstName, lastName);
            } else {
                //Iterate through the department linked list to find the correct department.
		        DepartmentNode* current = *departmentHead; //Start at the head of the list.
		        DepartmentNode* prev = NULL;
		        while (current != NULL) {
		            EmployeeNode* departmentEmployees = current->employees; //Look through the employees in that department.
		            EmployeeNode* foundEmployee = searchEmployee(departmentEmployees, firstName, lastName); //Search for the employee in the current department's AVL tree.
		            if (foundEmployee != NULL) { //If the employee is found:
		                //Delete the employee from the department's AVL tree.
		                current->employees = deleteEmployee(departmentEmployees, firstName, lastName);
		
		                //If the department's AVL tree becomes empty, remove the department node as well.
		                if (current->employees == NULL) {
		                    if (prev == NULL) {
		                        *departmentHead = current->next; //If the department is the first in the list, update the head.
		                    } else {
		                        prev->next = current->next; //Otherwise, link the previous node to the next one, bypassing the current department.
		                    }
		                    free(current); //Free memory allocated for the department node.
		                }
		
		                //Delete the employee's directory from the file explorer.
		                char basePath[MAX_LINE_LENGTH];
		                snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Employees/%s_%s", firstName, lastName);
		                _rmdir(basePath);
		
		                printf("Employee %s %s deleted.\n", firstName, lastName);
		                break; //Exit loop after deleting the employee.
		            }
		            prev = current; //If employee not found in current department, move to the next department and search again.
		            current = current->next;
		        }
		
		        if (current == NULL) { //If the employee was not found in any department, display a message.
		            printf("Employee %s %s not found.\n", firstName, lastName);
		    	}
			}
        } else if (choice == 'b') { //Return to the main menu if 'b' is pressed.
            return;
        } else {
            printf("Invalid choice. Please try again.\n");
        }
    }
}

//Function to handle patient visits.
void handleVisits(PatientNode* patient, const char* basePath) {
    char visitsPath[MAX_LINE_LENGTH];
    snprintf(visitsPath, sizeof(visitsPath), "%s/Visits", basePath); //Construct a string character called 'visitsPath' represented by the basePath passed to the function,--
	//--with '/Visits' appended to the end of it (for the visits folder of that patient).

    createDirectory(visitsPath);  //Ensure the Visits directory exists. This creates the folder if not.

    WIN32_FIND_DATA findFileData; //Use the WIN32_FIND_DATA Windows API structure to find data regarding a specified filepath.
    char searchPath[MAX_LINE_LENGTH]; //Initialize a searchPath character.
    snprintf(searchPath, sizeof(searchPath), "%s\\*", visitsPath); //Create a string representing all data in the 'Visits' folder passed to it.
    HANDLE hFind = FindFirstFile(searchPath, &findFileData); //Start at the beginning of all the files in that folder.
    int visitCount = 0; //Initialize a visitCount.

    if (hFind != INVALID_HANDLE_VALUE) {
        do { //Do the next if statement, that iterates through each file and counts up each time, while the 'FindNextFile' command is still valid.
            if (!(findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
                visitCount++; //Increase visitCount by 1 per file located in the folder. This automatically happens upon the function call.
            }
        } while (FindNextFile(hFind, &findFileData) != 0);
        FindClose(hFind); //Once we've gone through every file in the folder, close this portion of the function that reads through it.
    }

    if (visitCount == 0) {
        printf("No visits found, creating Visit 1.\n"); //Automatically create the first visit if there are none yet. 
        char visitFilename[MAX_LINE_LENGTH];
        snprintf(visitFilename, sizeof(visitFilename), "%s/Visit 1.txt", visitsPath); //Create a string called 'visitFilename' named after the visitsPath with '/Visit 1.txt. 

        FILE* visitFile = fopen(visitFilename, "w"); //Write to the visitFilename.
        if (visitFile) {
            char visitDetails[MAX_LINE_LENGTH]; //Initialize a visitDetails character.
            printf("Enter visit details: ");
            fgets(visitDetails, MAX_LINE_LENGTH, stdin); //Collect what the user types in for the visit details.
            visitDetails[strcspn(visitDetails, "\n")] = '\0';
            fprintf(visitFile, "%s\n", visitDetails); //Print the visitDetails to the visitFile.
            fclose(visitFile); 
        } else {
            printf("Error creating visit file.\n");
        }
    } else {
        while (1) {
            printf("There are %d visits. Would you like to add a new visit or view previous visits? (a/v) [b for back]: ", visitCount);
            char choice;
            scanf(" %c", &choice);
            getchar();

            if (choice == 'a') { //Adding a new visit.
                char visitFilename[MAX_LINE_LENGTH]; //Create a 'visitFilename' character.
                snprintf(visitFilename, sizeof(visitFilename), "%s/Visit %d.txt", visitsPath, visitCount + 1); //Construct a 'visitFilename' string that is the path to the 'Visits' folder, then 'Visit' plus the visit number--
				//--(1 plus number of files in the folder) and .txt to ensure it's a .txt file.

                FILE* visitFile = fopen(visitFilename, "w"); //File pointer command that opens the new file to write to it.
                if (visitFile) {
                    char visitDetails[MAX_LINE_LENGTH];
                    printf("Enter visit details: "); 
                    fgets(visitDetails, MAX_LINE_LENGTH, stdin); //Type the details of the new visit and save them to 'visitDetails.'
                    visitDetails[strcspn(visitDetails, "\n")] = '\0';
                    fprintf(visitFile, "%s\n", visitDetails); //Print what's typed into the .txt file.
                    fclose(visitFile); //Close the visit file.
                } else {
                    printf("Error creating visit file.\n");
                }
                break;
            } else if (choice == 'v') { //View previous visits for the patient.
                WIN32_FIND_DATA findFileData; //Same details as previous lines that have this text.
                char searchPath[MAX_LINE_LENGTH];
                snprintf(searchPath, sizeof(searchPath), "%s\\*", visitsPath);
                HANDLE hFind = FindFirstFile(searchPath, &findFileData); //Find the first file in the directory to begin the count.
                char visits[100][MAX_LINE_LENGTH];  //Assuming max 100 visits for simplicity.
                int count = 0; //Initialize the count to 0.

                if (hFind != INVALID_HANDLE_VALUE) { //If a file is found in the directory:
                    do {
                        if (!(findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
                            strncpy(visits[count], findFileData.cFileName, MAX_LINE_LENGTH); //Create a 'visits' string represented by the FileName at each file.
                            count++; //Increase the count by 1 for each file found in the directory.
                        }
                    } while (FindNextFile(hFind, &findFileData) != 0); //Iterate through 
                    FindClose(hFind);
                }

                printf("Select a visit to view:\n");
                for (int i = 0; i < count; i++) { 
                    printf("%d. %s\n", i + 1, visits[i]); //Start at the first file with the number 1, and label each subsequent visit found in the folder on a new line with the next greater number.
                }

                int selection;
                while (1) {
                    printf("Enter the number of your choice [b for back]: ");
                    char choice;
                    scanf(" %c", &choice); //Scan the number that the user puts in.
                    getchar();

                    if (choice == 'b') {
                        return;
                    } else {
                        selection = choice - '0';
                        if (selection >= 1 && selection <= count) { //Make sure that the number the user put in is one of the numbers of the files listed. If it's valid, move to the next step.
                            break;
                        } else {
                            printf("Invalid choice. Please try again.\n");
                        }
                    }
                }

                char visitFilename[MAX_LINE_LENGTH];
                snprintf(visitFilename, sizeof(visitFilename), "%s\\%s", visitsPath, visits[selection - 1]); //Construct a 'visitFilename' string pointing to the file associated with the number they chose, minus 1 since the--
                //--computer starts at 0, and the UI displays the first selection as 1.

                FILE* visitFile = fopen(visitFilename, "r"); //Open the associated file they chose for reading.
                if (visitFile) { //If the file exists:
                    char line[MAX_LINE_LENGTH];
                    printf("Visit Details:\n");
                    while (fgets(line, sizeof(line), visitFile)) {
                        printf("%s", line); //Print what's in the file.
                    }
                    fclose(visitFile);
                } else {
                    printf("Error reading visit file.\n");
                }
                break;
            } else if (choice == 'b') {
                return; //Go back to the last choice prompt.
            } else {
                printf("Invalid choice. Please try again.\n");
            }
        }
    }
}

//Function to initialize the priority queue.
void initializePriorityQueue(PriorityQueue* queue) {
    queue->front = NULL;
}

//Function to check if the priority queue is empty.
int isEmpty(PriorityQueue* pq) {
    return pq->front == NULL; //Develops a truth value tied to the front of the queue being NULL.
}

//Function to enqueue a patient based on severity, FILO for same severity.
void enqueuePatient(PriorityQueue* queue, PatientNode* patient) {
    PriorityQueueNode* newNode = (PriorityQueueNode*)malloc(sizeof(PriorityQueueNode)); //Allocate memory for a node in the priority queue.
    newNode->patient = patient; //New node contains patient data associated with the 'patient' argument passed to the function.
    newNode->next = NULL; //Initialize the new node's next pointer to NULL.

    
    if (queue->front == NULL || patient->severity > queue->front->patient->severity) { //If the queue is empty or the patient has higher severity than the first patient:
        newNode->next = queue->front; //Point the new node's next pointer to the current front node.
        queue->front = newNode; //Make the new node the front of the queue, placing the higher-severity patient at the front.
    } else {
        PriorityQueueNode* current = queue->front; //Start traversing the queue from the front.
        PriorityQueueNode* prev = NULL; //Initialize the previous node pointer to NULL.

        //Traverse the queue to find the correct position for the new patient.
        while (current != NULL && current->patient->severity >= patient->severity) { //While the current node is not null,and the current patient has a severity greater than or equal to the new patient's:
            prev = current; //Previous pointer becomes the current node,
            current = current->next; //And current pointer becomes node in the queue.
        }

        //Insert the new node at the correct position.
        newNode->next = current; //Point the new node's next pointer to the current node, where the traversal stopped.
        prev->next = newNode; //If the previous node exists, link it to the new node, inserting the new node into the queue.
    }
}

//Function to dequeue a patient from the priority queue.
PatientNode* dequeue(PriorityQueue* pq) {
    if (pq->front == NULL) { //If the front of the priority queue is NULL, tell the user the queue is empty.
        printf("Queue is empty.\n");
        return NULL;
    }

    PriorityQueueNode* temp = pq->front; //Create a temporary pointer that points to the front node of the queue.
    pq->front = pq->front->next; //The front of the queue becomes the next spot in the queue.
    PatientNode* patient = temp->patient; //Extract the patient data from the node that was at the front of the queue.
    free(temp); //Free the memory allocated for the temp node.
    return patient; //Return the patient found at the front of the queue to the calling function. 
}

// Function to display the current queue
void displayQueue(PriorityQueue* queue) {
    if (isEmpty(queue)) { //Say the queue is empty if isEmpty returns a true value.
        printf("The queue is empty.\n");
        return;
    }

    printf("Current Queue:\n");
    PriorityQueueNode* current = queue->front; //Start at the front of the queue.
    while (current != NULL) { //Iterate through every node in the queue.
        PatientNode* patient = current->patient;
        printf("Patient: %s %s, Severity: %d\n", patient->firstName, patient->lastName, patient->severity); //Print the information at the current node.
        current = current->next; //Move to the next node.
    }
}

//Function to handle patient check-in to the priority queue.
void handlePatientCheckIn(PriorityQueue* queue, PatientNode** patientRoot) {
    char firstName[MAX_NAME_LENGTH]; //Take the first name, last name, and severity.
    char lastName[MAX_NAME_LENGTH];
    int severity;

    printf("Enter patient's first name: ");
    fgets(firstName, MAX_NAME_LENGTH, stdin);
    firstName[strcspn(firstName, "\n")] = '\0';

    printf("Enter patient's last name: ");
    fgets(lastName, MAX_NAME_LENGTH, stdin);
    lastName[strcspn(lastName, "\n")] = '\0';

    printf("Enter severity level (1-10): ");
    scanf("%d", &severity);
    getchar();

    PatientNode* foundPatient = searchPatient(*patientRoot, firstName, lastName); //Run the searchPatient function and return a truth value based on their presence in the 'patients' AVL tree.

    if (foundPatient) {
        printf("Patient found: %s %s\n", foundPatient->firstName, foundPatient->lastName);
        foundPatient->severity = severity;
        enqueuePatient(queue, foundPatient); //Enqueue them into the priority queue if they are found in the 'patients' AVL tree.

        printf("Patient %s %s has been checked in with severity %d.\n",
               foundPatient->firstName, foundPatient->lastName, severity); //Give the user a check-in notification.
    } else {
        printf("Patient not found. Creating new patient record.\n");

        PatientNode newPatient; //Construct a newPatient PatientNode.
        strcpy(newPatient.firstName, firstName); //Save the first name the user input to the newPatient's first name,
        strcpy(newPatient.lastName, lastName); //and do the same for the second.

        printf("Enter date of birth (YYYY-MM-DD): "); //Then, prompt the user for the rest of the relevant patient data--
        fgets(newPatient.dateOfBirth, MAX_DOB_LENGTH, stdin);
        newPatient.dateOfBirth[strcspn(newPatient.dateOfBirth, "\n")] = '\0';

        printf("Enter gender: ");
        fgets(newPatient.gender, MAX_GENDER_LENGTH, stdin);
        newPatient.gender[strcspn(newPatient.gender, "\n")] = '\0';

        printf("Enter address: ");
        fgets(newPatient.address, MAX_ADDRESS_LENGTH, stdin);
        newPatient.address[strcspn(newPatient.address, "\n")] = '\0';

        printf("Enter phone number: ");
        fgets(newPatient.phone, MAX_PHONE_LENGTH, stdin);
        newPatient.phone[strcspn(newPatient.phone, "\n")] = '\0';

        printf("Enter email: ");
        fgets(newPatient.email, MAX_EMAIL_LENGTH, stdin);
        newPatient.email[strcspn(newPatient.email, "\n")] = '\0';

        printf("Enter blood type: ");
        fgets(newPatient.bloodType, MAX_BLOOD_TYPE_LENGTH, stdin);
        newPatient.bloodType[strcspn(newPatient.bloodType, "\n")] = '\0';

        printf("Enter SSN (XXX-XX-XXXX): ");
        fgets(newPatient.ssn, MAX_SSN_LENGTH, stdin);
        newPatient.ssn[strcspn(newPatient.ssn, "\n")] = '\0';

        printf("Enter patient ID: ");
        scanf("%d", &newPatient.patientID);
        getchar();

        PatientNode* createdPatient = createPatientNode(newPatient); //--then create a PatientNode containing the newPatient information,
        *patientRoot = insertPatient(*patientRoot, createdPatient); //--and insert that patient into the 'patients' AVL tree using insertPatient.

        //Create directory and save the patient's file.
        char basePath[MAX_LINE_LENGTH];
        snprintf(basePath, sizeof(basePath), "C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients/%s_%s",
                 createdPatient->firstName, createdPatient->lastName); //Create a string representing the path to the new patient's folder, indicated by their name.

        _mkdir(basePath); //Make the directory located at the path of the string passed to this command.

        char filename[MAX_LINE_LENGTH];
        snprintf(filename, sizeof(filename), "%s/%s_%s.txt", basePath, firstName, lastName); //Construct a string called 'filename' representing the path to the .txt file.
        writePatientData(filename, createdPatient); //Write the patient data into that .txt file.

        createdPatient->severity = severity; //Attach the input severity to the createdPatient variable.
        enqueuePatient(queue, createdPatient); //Pass the createdPatient to the enqueuePatient function.

        printf("New patient %s %s has been created and checked in with severity %d.\n",
               createdPatient->firstName, createdPatient->lastName, severity);
               
        handleVisits(createdPatient, basePath); //Run the handleVisits function with the basePath argument passed to it to set up this new patient's first visit's details.
    }
}

//Function to process the patient queue with options.
void processQueue(PriorityQueue* queue) {
    while (!isEmpty(queue)) { //If the user chose to process the queue at the menu, and the queue is not empty, give the user these options.
        printf("\nChoose an option:\n");
        printf("1. Display the current queue\n");
        printf("2. Dequeue and process the next patient\n");
        printf("3. Show the next patient in line\n");
        printf("4. Exit queue processing\n");
        printf("Enter your choice: ");

        int choice;
        scanf("%d", &choice);
        getchar();  

        switch (choice) {
            case 1:
                displayQueue(queue); //Run the displayQueue function if the user just wants to see the queue.
                break;
            case 2: {
                PatientNode* patient = dequeue(queue); //Dequeue the next patient in line and print the processing message.
                if (patient) {
                    printf("Dequeued and processing patient: %s %s with severity %d\n", patient->firstName, patient->lastName, patient->severity);
                } else {
                    printf("No patients to dequeue.\n");
                }
                break;
            }
            case 3: {
                if (!isEmpty(queue)) { //While the queue isn't empty, peek at the front of the queue with a display message.
                    PatientNode* patient = queue->front->patient;
                    printf("Next patient in line: %s %s with severity %d\n", patient->firstName, patient->lastName, patient->severity);
                } else {
                    printf("No patients in the queue.\n");
                }
                break;
            }
            case 4:
                printf("Exiting queue processing.\n"); //Return to the menu.
                return;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
        }
    }
    printf("The queue is empty.\n");
}

//Function to display the main menu.
void displayMenu() { //Print out the options to choose from.
    printf("\nWelcome to the display menu of our healthcare information system. Choose an option:\n");
    printf("1. Process patient/employee data\n");
    printf("2. Patient Check-in (Priority Queue)\n");
    printf("3. Process the Patient Queue\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
}

int main() {
    PatientNode* patientRoot = NULL; //Initialize root the 'patients' AVL tree.
    DepartmentNode* departmentHead = NULL; //Initialize the head of the 'departments' linked list with the associated 'employees' AVL trees.
    PriorityQueue queue;

    //Initialize the priority queue.
    initializePriorityQueue(&queue);

    //Load existing data into binary trees and linked lists.
    loadPatients("C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Patients", &patientRoot);
    loadEmployees("C:/Users/johna/OneDrive/Documents/CS 5008/Final Project/HIS data/Employees", &departmentHead);

    while (1) { //Infinite loop to continuously display the menu until the user chooses to terminate.
        displayMenu(); //Display the main menu to the user.
        int choice;
        scanf("%d", &choice);
        getchar(); //Clear the newline character left in the input buffer by scanf.

        switch (choice) {
            case 1:
                promptAndProcessData(&patientRoot, &departmentHead); //Run the 'promptAndProcessData' function if they choose option 1.
                break;
            case 2:
                handlePatientCheckIn(&queue, &patientRoot); //Run the 'handlePatientCheckIn' function to add to the patient queue if they choose option 2.
                break;
            case 3:
                processQueue(&queue); //Run the 'processQueue' function if they choose option 3.
                break;
            case 4:
                cleanupQueue(&queue); //Release all patient, queue, and department data from working memory if they choose option 4.
                cleanupPatientTree(patientRoot); //Free the memory allocated for the 'patients' AVL tree.
                cleanupDepartmentList(departmentHead); //Free the memory allocated for the 'departments' linked list and its associated 'employees' AVL trees. 
                return 0;
            default: //Reprompt an input if the user put something other than a number from 1 to 4.
                printf("Invalid choice. Please try again.\n");
        }
    }
}

//Function to cleanup the patient tree.
void cleanupPatientTree(PatientNode* root) {
    if (root == NULL) {
        return;
    }
    cleanupPatientTree(root->left); //Recursively call this function to release memory allocated to the 'patients' AVL tree to the left subtree.
    cleanupPatientTree(root->right); //And do the same for the right subtree.
    free(root); //Release memory allocated to the current node.
}

//Function to cleanup the employee tree. No comments since it functions identically to the 'cleanupPatientTree' function.
void freeEmployeeTree(EmployeeNode* root) {
    if (root == NULL) {
        return;
    }
    freeEmployeeTree(root->left);
    freeEmployeeTree(root->right);
    free(root);
}

//Function to cleanup the department list.
void cleanupDepartmentList(DepartmentNode* head) {
    DepartmentNode* current = head;
    while (current != NULL) { //Loop through each department in the 'departments' linked list.
        //Free the employee tree in the current department.
        freeEmployeeTree(current->employees);

        //Move to the next department and free the current one.
        DepartmentNode* temp = current;
        current = current->next;
        free(temp);
    }
}

//Function to cleanup the priority queue.
void cleanupQueue(PriorityQueue* pq) {
    while (!isEmpty(pq)) {
        dequeue(pq); //Dequeue everyone in the priority queue.
    }
}
