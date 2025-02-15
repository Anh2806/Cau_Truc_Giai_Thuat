#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node* prev;

    Node(int data) {
        this->data = data;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

class DoublyLinkedList {
public:
    Node* head;

    DoublyLinkedList() {
        head = nullptr;
    }

    void insert(int data) {
        Node* new_node = new Node(data);
        new_node->next = head;
        if (head) {
            head->prev = new_node;
        }
        head = new_node;
    }

    void deleteNode(int key) {
        Node* temp = head;
        if (temp && temp->data == key) {
            head = temp->next;
            if (head) {
                head->prev = nullptr;
            }
            delete temp;
            return;
        }

        while (temp && temp->data != key) {
            temp = temp->next;
        }

        if (!temp) return;

        if (temp->next) {
            temp->next->prev = temp->prev;
        }
        if (temp->prev) {
            temp->prev->next = temp->next;
        }
        delete temp;
    }

    void display() {
        Node* temp = head;
        while (temp) {
            std::cout << temp->data << " <-> ";
            temp = temp->next;
        }
        std::cout << "None" << std::endl;
    }
};

int main() {
    DoublyLinkedList dll;
    dll.insert(10);
    dll.insert(20);
    dll.insert(30);
    dll.display();
    dll.deleteNode(20);
    dll.display();
    return 0;
}