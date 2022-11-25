#include <iostream>
#include <string.h>

class MyString
{
   private:
      char *str;
      int length;
   public:
      MyString();
      MyString(char *str);
      MyString(const MyString& other);
      MyString(MyString&& other);
     ~MyString();
      MyString& operator=(const MyString& other);
      MyString operator+(const MyString& other);
      void print();
      
};

MyString::MyString(){
      str = nullptr;
}

MyString::MyString(char *str){
      int length = strlen(str);
      this->str = new char[length];
      for(int i = 0; i < length; i++){
            this->str[i] = str[i];
      }
      this->str[length] = '\0';
      std::cout<<"ctor has called"<<std::endl;
}

MyString::MyString(const MyString& other){
      int length = strlen(other.str);
      this->str = new char[length + 1];
      for(int i = 0; i < length; i++){
            this->str[i] = other.str[i];
      }
      this->str[length] = '\0';
      std::cout<<"move ctor has called"<<std::endl;
}

MyString::MyString(MyString&& other){
      this->str = other.str;
      this->length = other.length;
      other.str = nullptr;
      std::cout<<"move ctor has called"<<std::endl;
}

MyString::~MyString(){
      delete[] this->str;
      std::cout<<"dtor has called"<<std::endl;
}

MyString& MyString::operator=(const MyString& other){
      int length = strlen(other.str);
      this->str = new char[length + 1];
      for(int i = 0; i < length; i++){
            this->str[i] = other.str[i];
      }
      this->str[length] = '\0';
      return *this;
      std::cout<<"op= has called"<<std::endl;
}

MyString MyString::operator+(const MyString& other){
      MyString res;
      int thislength = strlen(this->str);
      int otherlength = strlen(other.str);
      res.str = new char[thislength + otherlength + 1];
      int i = 0;
      for(; i < thislength; i++){
            res.str[i] = this->str[i];
      }
      for(int j = 0; j < otherlength; j++, i++){
            res.str[i] = other.str[j];
      }
      res.str[thislength + otherlength] = '\0';
      return res;
}

void MyString::print(){
      std::cout<<str<<std::endl;
}
int main(){
      MyString a("hello");
      MyString b("anna");
      MyString r;
      r = a + b;
      r.print();
}