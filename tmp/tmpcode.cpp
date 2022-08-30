#include <iostream>
#include <bitset>
#include <string>
#include <cstring>

// "/home/alira/FYP/tmp/"tmpcode 0010100111 1101001110

// g++ -o /home/alira/FYP/tmp/tmpcode.o /home/alira/FYP/tmp/tmpcode.cpp
int main(int argc, char **argv)
{


// int argc=3; 
// std::string argv[3] = {"","0010100111","1101001110"};


if(argc!=3){std::cout <<"ERROR!!! \nIncorrect No of Inputs\n"; return -1;}

for (int i = 1; i < argc; ++i){
      std::cout<<strlen(argv[i]) <<"\n";
      for(int j=0;j<10;j++){
      std::cout << argv[i][j]<<" ";
      }
      std::cout<< "\n";

      // if(strlen(argv[i])!=10){std::cout <<"ERROR!!! \nInputs not 10 bits\n"; return -1;}
}
  return 0;

// for(int j=0;j<10;j++){
//       std::cout << argv[i][j];
//       }
//       std::cout<< "\n";

}