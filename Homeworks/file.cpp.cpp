#include <iostream>
#include <string>
#include <fstream>
#include <elf.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>


void load_obj_file()
{
      struct stat sb;
      
      //trying open object file
      int fd = open("obj.o", O_RDONLY);
      if(fd <= 0)
      {
            perror("cant open obj.o");
            exit(errno);
      }
      //gets information specified by the open descriptor 
      if (fstat(fd, &sb))
      {
            perror("Failed to get obj.o info");
            exit(errno);
      }
}

std::string run_obj_file(std::string file_name)
{
      char buff[1024];
      FILE* in;
      std::string res = "";
      in = fopen("obj.o", "r");
      if(in == NULL)
      {
            return "cant open file";
      }
      while(!feof(in))
      {
            if(fgets(buff, 1024, in) != nullptr)
            {
                  res += buff;
            }
      }
      pclose(in);
      return res;
}

int main()
{
      load_obj_file();
      std::string s = run_obj_file("readelf -a a.out");
      std::cout<<s;
}