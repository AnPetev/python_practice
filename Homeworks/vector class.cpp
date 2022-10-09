
#include <iostream>
class Vector
{
      private:
         int size;
         int capacity;
         int *arr;
      public:
          Vector();
          Vector(int size, int* tmparr);
          ~Vector();
          Vector(const Vector& other);
          void push_back(int elem);
          Vector& operator=(const Vector& v);
          void print();
};

Vector::Vector():size(0),capacity(0),arr(nullptr){}

Vector::Vector(int size, int* tmparr){
     this->size = size;
     capacity = size * 2;
     this->arr = new int[capacity];
     for(int i = 0; i < size; i++){
           this->arr[i] = tmparr[i];
     }
}

Vector::~Vector(){
      delete[] arr;
}

Vector::Vector(const Vector& other){
      this->size = other.size;
      this->capacity = other.capacity;
      this->arr = new int[other.capacity];
      for(int i = 0; i < size; i++){
            this->arr[i] = other.arr[i];
      }
}

void Vector::push_back(int elem){
      if(size == 0){
            capacity = 1;
            arr = new int[capacity];
      }
      else if(size == capacity){
            capacity = size * 2;
            int *tmp = new int[capacity];
            for(int i = 0; i < size; i++){
                  tmp[i] = arr[i];
            }
            delete[] arr;
            arr = tmp;
      }
      arr[size] = elem;
      size++;
}

void Vector::print(){
      for(int i = 0; i < this->size; i++){
            std::cout<<this->arr[i]<<" ";
      }
}
Vector& Vector::operator=(const Vector& v){
      if(this == &v){
            return *this;
      }
      delete[] arr;
      size = v.size;
      capacity = v.capacity;
      arr = new int[capacity];
      for(int i = 0; i < size; i++){
            arr[i] = v.arr[i];
      }
      return *this;
}
int main()
{
   int data[] = {1,4,5,6,9};
   Vector v(5, data);
   v.push_back(11);
   v.print();
   std::cout<<std::endl;
   Vector v1(v);
   v1.print();
   std::cout<<std::endl;
   Vector v3;
   v3 = v1;
   v3.print();
   
   
   

    return 0;
}