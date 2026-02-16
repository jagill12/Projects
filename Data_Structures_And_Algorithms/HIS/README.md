# Healthcare Information System (HIS)

## AVL Tree-Backed Patient and Employee Management System
This is a command-line Healthcare Information System implemented in pure C, which is designed to demonstrate my aptitude with practical applacations of classic data structures and algorithms in a real-world setting.

This project manages patient and employee records using self-balancing AVL trees, supports department organization, and implements a severity-based patient "ER" queue while persisting all added/edited data directly to the file system.

# Dependencies / Requirements
This project was written in standard C and has minimal external requirements. It is Windows-only in its current form.

## Compiler
  GCC or Microsoft Visual Studio C compiler (MSVC)
  
## Required Libraries

## Windows API (Platform Requirement)
  - windows.h
  - WIN32_FIND_DATA
  - FindFirstFile/FindNextFile
  - _mkdir
  - Windows directory handling

## Standard C Libraries
  - stdio.h
  - stdlib.h
  - string.h
  - errno.h
  - sys/types.h
  - sys/stat.h

## Overview
This system simulates a simple electronic healthcare record environment. In it: patients and employees are stored as structured records, which are indexed using balanced search trees; employees are stored by department, which 
dynamically organize employees; patients are checked into the ER using a priority queue triage that orders them by severity and time, if multiple patients have the same severity; and ensures all data persists as structured 
directories and files, which are .txt files in this project for the sake of demonstration.

The specified file path which houses all patient and employee data is automatically, recursively read upon launching the program such that all patients and employees that have been saved from previous runs are loaded into working memory.
They are then put into their own AVL trees: one for all patients, ordered by last name alphabetically; and several for the employees -- one for each department, where the employees' data is stored. During each run of the program, as patients'
and employees' information is modified -- whether by adding new ones, removing existing ones, or updating what's already there -- each commit automatically updates the corresponding files in the file path in real time.

## Core Data Structures

### AVL Trees
These are used to store data of patients and employees (by department). They guarantee O(log n) time complexity for search, insertion, and deletion. The self-balancing of the trees is achieved through rotations:
left rotation, right rotation, left-right rotation, and right-left rotation. Records are ordered lexicographically by last name.

### Linked Lists
Departments are stored as a singly linked list; each department node owns its own employee AVL tree. I did this to demonstrate hybrid data structure composition: linked list for categorical grouping, and balanced trees for indexed lookup.

### Priority Queue
At the main menu, there is an option to enter the ER and check patients in. They'll come in, give their name and their severity, then be put in the queue accordingly. If they have higher severity (on a scale of 1-10), they're put
in the appropriate spot, with 10 at the front of the line. If someone else in line has the same severity as them, they're put at the back of that severity level due to arriving last. When patients give their name, if they are already in 
the system, a prompt asking them to describe their reason for visiting will pop up, then they will ahve a new visit .txt file added to the /visits/ folder in their patient folder within the /patients/ directory. If it's their first time,
the user will be prompted to put in all their information, which will then be used to make a new folder in the /patients/ directory with their name, with a .txt file containing that information, and a new visit .txt file that contains
the information describing why they're visiting.

### Filesystem Persistence
Instead of a database, records are persisted as directories, which demonstrates directory traversal, recursive deletion, structured file I/O, and state reconstruction at program startup.

## Algorithms Utilized
  - AVL tree balancing
  - Binary search tree insertion/deletion
  - In-order traversal (sorted output)
  - Recursive memory cleanup
  - Recursive filesystem traversal
  - Ordered linked-list insertion
  - Sequential search
  - Dynamic memory allocation (malloc/free)

## Features
### Patient and Employee Management
  - Add, search update, and delete patients.
  - Automatic file creation.
  - Visit history tracking.
  - Sorted patient listing.
  - Department-based organization (for employees).
  - AVL-tree indexed lookup.
  - Record editing and persistence.

### Triage Queue
  - Patient check-in with severity scoring and ordering.
  - Queue visualization.
  - Controlled dequeue processing.

### Data Persistence
  - Automatic loading of records at startup.
  - Directory-based storage.
  - Recursive cleanup on deletion.

## Program Architecture
```
main()
  Load filesystem data
    Patient AVL Tree
    Department List -> Employe AVL Trees
  Interactive CLI Menu
    Data Management
    Patient Check-In
    Queue Processing
Memory Cleanup
```
## Compilation
This project is written in C and uses Windows filesystem APIs.
Compile using:
  gcc Healthcare_Information_System.c -o his

## Running
./his
  - You will be presented with a menu allowing:
1. Patient/Employee data management
2. Patient check-in (priority queue)
3. Queue processing
4. Exit and cleanup

## Example Complexity
  - Operation                Complexity
  - Patient search           O(log n)
  - Patient insert/delete    O(log n)
  - Department lookup        O(d)
  - Queue enqueue            O(n)
  - Queue dequeue            O(1)
  - Tree traversal           O(n)

## Educational Goals
This project was built to demonstrate my understanding of the practical application of balanced trees, manual memory management, hybrid data structure design, algorithmic performance guarantees, systems-level file handling, and CLI-driven
software architecture.

## Future Improvements
Possible Extensions
  - Replace filesystem storage with SQL backend
  - Hash-table indexing for IDs
  - Cross-platform filesystem abstraction
  - Multi-threaded queue processing
  - REST API interface
  - GUI frontend
  - Access logging for security purposes
    
# Author
John Gill
M.S. Bioinformatics - Northeastern University
Focus areas: Algorithms, Bioinformatics Pipelines, Systems Programming, and Data Engineering

## License
MIT License
