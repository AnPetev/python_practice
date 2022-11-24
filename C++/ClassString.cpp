#include <iostream>
#include <string.h>

class MyString
{
      private:
          char *str;
      public:
          MyString()
          {
                str = nullptr;
          }
          MyString(char *str)
          {
            int length = strlen(str);
            this->str = new char[length];
            for(int i = 0; i < length; i++){
                  this->str[i] = str[i];
            }
            this->str[length] = '\0';
            std::cout<<"ctor has called"<<std::endl;
          }
          MyString(const MyString& other){
                int length = strlen(other.str);
                this->str = new char[length + 1];
                for(int i = 0; i < length; i++){
                      this->str[i] = other.str[i];
                }
                this->str[length] = '\0';
                std::cout<<"copy ctor has called"<<std::endl;
          }
          ~MyString()
          {
                delete[] this->str; 
                std::cout<<"dtor has called"<<std::endl;
          }
          MyString& operator=(const MyString& other)
          {
            if(this->str != nullptr){
                  delete[] str;
            }            
            int length = strlen(other.str);
            this->str = new char[length + 1];
            for(int i = 0; i < length; i++){
                  this->str[i] = other.str[i];
            }
            this->str[length] = '\0';
            return *this;
            std::cout<<"op= has called"<<std::endl;
                
          }
          MyString operator+(const MyString& other)
          {
            MyString result;
            int thislength = strlen(this->str);
            int otherlength = strlen(other.str);
            result.str = new char[thislength + otherlength + 1];
            int i = 0;
            for(; i < thislength; i++){
                  result.str[i] = this->str[i];
            }
            
            for(int j = 0; j < otherlength; j++,i++ ){
                  result.str[i] = other.str[j];
            }
            result.str[thislength + otherlength] = '\0';
            return result;
          }
      void print(){
            std::cout<< str <<std::endl;
      }
};
int main(){
      MyString a("hello");
      MyString b("anna");
      MyString c(b);
      MyString r = a + b;
      r.print();
      
      
}