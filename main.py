#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct Student {
    int id;
    string name;
    string dept;
};

vector<Student> students;

void loadData() {
    ifstream file("students.txt");
    Student s;
    while (file >> s.id >> s.name >> s.dept) {
        students.push_back(s);
    }
    file.close();
}

void saveData() {
    ofstream file("students.txt");
    for (auto s : students) {
        file << s.id << " " << s.name << " " << s.dept << endl;
    }
    file.close();
}

void addStudent() {
    Student s;
    cout << "Enter ID: ";
    cin >> s.id;
    cout << "Enter Name: ";
    cin >> s.name;
    cout << "Enter Department: ";
    cin >> s.dept;

    students.push_back(s);
    saveData();
    cout << "Student added successfully.\n";
}

void viewStudents() {
    if (students.empty()) {
        cout << "No records found.\n";
        return;
    }
    for (auto s : students) {
        cout << "ID: " << s.id
             << " Name: " << s.name
             << " Dept: " << s.dept << endl;
    }
}

void searchStudent() {
    int id;
    cout << "Enter ID to search: ";
    cin >> id;
    for (auto s : students) {
        if (s.id == id) {
            cout << "Found -> ID: " << s.id
                 << " Name: " << s.name
                 << " Dept: " << s.dept << endl;
            return;
        }
    }
    cout << "Student not found.\n";
}

void deleteStudent() {
    int id;
    cout << "Enter ID to delete: ";
    cin >> id;
    for (int i = 0; i < students.size(); i++) {
        if (students[i].id == id) {
            students.erase(students.begin() + i);
            saveData();
            cout << "Student deleted.\n";
            return;
        }
    }
    cout << "Student not found.\n";
}

int main() {
    loadData();
    int choice;

    do {
        cout << "\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: addStudent(); break;
            case 2: viewStudents(); break;
            case 3: searchStudent(); break;
            case 4: deleteStudent(); break;
            case 5: cout << "Exiting...\n"; break;
            default: cout << "Invalid choice.\n";
        }
    } while (choice != 5);

    return 0;
}
