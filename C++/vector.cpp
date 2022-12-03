#include <iostream>

class Vector {
private:
	int size;
	int capacity;
	int* arr;
public:
	Vector();
	Vector(int size, int* data);
	Vector(const Vector& other);
	Vector(Vector&& obj);
    ~Vector();
	Vector& operator = (const Vector& obj);
	Vector operator+(const Vector& v);
	void push_back(int elem);
	void print();



};
Vector::Vector() :size(0), capacity(0), arr(nullptr) {
	std::cout << "default ctor has called" << std::endl; }

Vector::Vector(int size, int* data) {
	this->size = size;
	capacity = size * 2;
	this->arr = new int[capacity];
	for (int i = 0; i < size; i++) {
		this->arr[i] = data[i];
	}
	std::cout << " ctor has called" << std::endl;
}

Vector::Vector(const Vector& other) {
	this->size = other.size;
	this->capacity = other.capacity;
	this->arr = new int[other.capacity];
	for (int i = 0; i < size; i++) {
		this->arr[i] = other.arr[i];
	}
	std::cout << "copy ctor has called" << std::endl;
}

Vector::Vector(Vector&& obj) {
	this->size = obj.size;
	this->capacity = obj.capacity;
	this->arr = obj.arr;
	obj.size = 0;
	obj.capacity = 0;
	obj.arr = nullptr;
	std::cout << "move ctor has called" << std::endl;
}


Vector& Vector::operator = (const Vector& obj) {
	if (this == &obj) {
		return *this;
	}
	delete[] arr;
	this->size = obj.size;
	this->capacity = obj.capacity;
	arr = new int[capacity];
	for (int i = 0; i < size; i++) {
		arr[i] = obj.arr[i];
	}
	std::cout << "op= has called" << std::endl;
	return *this;
	

}

Vector Vector::operator+(const Vector& v) {
	Vector r;
	r.size = this->size + v.size;
	r.capacity = this->capacity + v.capacity;
	r.arr = new int[r.capacity];
	for (int i = 0; i < this->size; i++) {
		r.arr[i] = this->arr[i] + v.arr[i];
	}
	for (int i = 0; i < v.size; i++) {
		r.arr[i] = this->arr[i] + v.arr[i];
	}
	std::cout << "op+ has called" << std::endl;
	return r;
	

}

void Vector::push_back(int elem) {
	if (size == 0) {
		capacity = 1;
		arr = new int[capacity];
	}
	else if (size == capacity) {
		capacity = size * 2;
		int* tmp = new int[capacity];
		for (int i = 0; i < size; i++) {
			tmp[i] = arr[i];
		}
		delete[] arr;
		arr = tmp;
	}
	arr[size] = elem;
	size++;
}

Vector::~Vector() {
	delete[] arr;
	std::cout << "dtor has called" << std::endl;
}
void Vector::print() {
	for (int i = 0; i < size; i++) {
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;
}
int main() {
	int data[] = { 1,2,3,5 };
	int data2[] = { 4,5,6,9 };
	Vector v(4, data);
	//Vector v2(4, data2);
	//Vector v3(v2);
	//v2 = v;
	//v2.print();
	//Vector v3;
	//v.operator+(v2).print();
	Vector v1(4, data2);
	Vector v3;
	v3 = v + v1;
	v3.print();
}