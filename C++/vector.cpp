#include <iostream>

class Vector
{
      private:
         int size;
         int capacity;
         int* arr;
      public:
           Vector();
           Vector(int size, int* tmparr);
          ~Vector();
           Vector(const Vector& obj);
           Vector(Vector&& oth);
           void push_back(int elem);
           Vector& operator=(const Vector& ob);
           Vector operator+(const Vector& v1);
           void print();
           int& operator[](int index);
           
};


Vector::Vector():size(0), capacity(0), arr(nullptr){std::cout<<"default ctor has called"<<std::endl;}

Vector::Vector(int size, int* tmparr):size(size)
{
      capacity = size * 2;
      this->arr = new int[capacity];
      for(int i = 0; i < size; i++){
            this->arr[i] = tmparr[i];
      }
      std::cout<<"ctor has called"<<std::endl;
}

Vector::~Vector()
{
      delete[] arr;
      std::cout<<"dtor has called"<<std::endl;
}

Vector::Vector(const Vector& obj)
{
      this->size = obj.size;
      this->capacity = obj.capacity;
      this->arr = new int[obj.capacity];
      for(int i = 0;  i < size; i++)
      {
            this->arr[i] = obj.arr[i];
      }
      std::cout<<"copy ctor has called"<<std::endl;
}

Vector::Vector(Vector&& other)
{
      this->size = other.size;
      this->capacity = other.capacity;
      this->arr = other.arr;
      other.size = 0;
      other.capacity = 0;
      other.arr = nullptr;
      std::cout<<"move ctor has called"<<std::endl;
}

void Vector::push_back(int elem)
{
      if(size == 0){
            capacity = 1;
            arr = new int[capacity];
      }
      else if(size == capacity){
            capacity = size * 2;
            int* tmp = new int[capacity];
            for(int i = 0; i < size; i++){
                  tmp[i] = arr[i];
            }
      delete[] arr;
      arr = tmp;
      }
      arr[size] = elem;
      ++size;
}

Vector& Vector::operator=(const Vector& ob)
{
      if(this == &ob){
            return *this;
      }
      delete[] arr;
      this->size = ob.size;
      this->capacity = ob.capacity;
      arr = new int[capacity];
      for(int i = 0; i < size; i++){
            arr[i] = ob.arr[i];
      }
      return *this;
      std::cout<<"op= has called"<<std::endl;
}

Vector Vector::operator+(const Vector& v)
{
      Vector r;
      r.size = this->size + v.size;
      r.capacity = this->capacity + v.capacity;
      r.arr = new int[r.capacity];
      for(int i = 0; i < this->size; i++){
            r.arr[i] = this->arr[i] + v.arr[i];
      }
      for(int i = 0; i < v.size; i++){
            r.arr[i] = this->arr[i] + v.arr[i];
      }
      return r;
}

void Vector::print()
{
      for(int i = 0; i < size; i++){
            std::cout<<arr[i]<<" ";
      }
      std::cout<<std::endl;
}

int& Vector::operator[](int index)
{
     return arr[index];
}
int main()
{
     int data[] = {1,2,3,4,5};
     Vector v1(5, data);
     int s[] = {6,7,8};
     Vector v2(3, s);
     v1.operator+(v2).print();
}   