#include "tmp.cpp"
#include <iostream>
#include <bitset>
#include <string>
#include <cstring>

// using namespace std;

// clang++ -g -O3 -std=c++14 -I `yosys-config --datdir`/include main.cpp -o tb
// clang++ -g -O3 -std=c++14 -I `/home/alira/FYP/linux/yosys/build/yosys-config --datdir` -I'/home/alira/FYP/linux/yosys/'  /include /home/alira/FYP/tmp/main.cpp -o tb
//-I`/home/alira/FYP/linux/yosys/build/yosys-config --datdir`
// g++ -I`/home/alira/FYP/linux/yosys/build/yosys-config --datdir` -I/home/alira/FYP/linux/yosys -o /home/alira/FYP/oracle/oracle /home/alira/FYP/oracle/main.cpp

int get_bool(char s){
if(s=='1') return 1;
else return 0;
}



int main(int argc, char **argv)
{

   if(argc!=2){std::cout <<"ERROR!!! \nIncorrect No of Inputs\n"; return -1;}

for (int i = 1; i < argc; ++i){
      if(strlen(argv[i])!=10){std::cout <<"ERROR!!! \nInputs not 10 bits\n"; return -1;}
}




   cxxrtl_design::p_top top;



   // top.p_vdd.set<uint32_t>(get_bool(argv[1][9]));
   // top.p_pi8.set<uint32_t>(get_bool(argv[1][8]));
   // top.p_pi7.set<uint32_t>(get_bool(argv[1][7]));
   // top.p_pi6.set<uint32_t>(get_bool(argv[1][6]));
   // top.p_pi5.set<uint32_t>(get_bool(argv[1][5]));
   // top.p_pi4.set<uint32_t>(get_bool(argv[1][4]));
   // top.p_pi3.set<uint32_t>(get_bool(argv[1][3]));
   // top.p_pi2.set<uint32_t>(get_bool(argv[1][2]));
   // top.p_pi1.set<uint32_t>(get_bool(argv[1][1]));
   // top.p_pi0.set<uint32_t>(get_bool(argv[1][0]));

   top.p_vdd.set<uint32_t>(0);
   top.p_pi8.set<uint32_t>(1);
   top.p_pi7.set<uint32_t>(1);
   top.p_pi6.set<uint32_t>(1);
   top.p_pi5.set<uint32_t>(0);
   top.p_pi4.set<uint32_t>(1);
   top.p_pi3.set<uint32_t>(1);
   top.p_pi2.set<uint32_t>(0);
   top.p_pi1.set<uint32_t>(1);
   top.p_pi0.set<uint32_t>(0);




   std::cout << top.p_po00.get<bool>()<< 
   top.p_po18.get<uint32_t>()<<  
   top.p_po17.get<uint32_t>()<< 
   top.p_po16.get<uint32_t>()<< 
   top.p_po15.get<uint32_t>()<< 
   top.p_po14.get<uint32_t>()<< 
   top.p_po13.get<uint32_t>()<< 
   top.p_po12.get<uint32_t>()<< 
   top.p_po11.get<uint32_t>()<< 
   top.p_po10.get<uint32_t>()<< 
   top.p_po09.get<uint32_t>()<< 
   top.p_po08.get<uint32_t>()<< 
   top.p_po07.get<uint32_t>()<< 
   top.p_po06.get<uint32_t>()<< 
   top.p_po05.get<uint32_t>()<< 
   top.p_po04.get<uint32_t>()<< 
   top.p_po03.get<uint32_t>()<< 
   top.p_po02.get<uint32_t>()<< 
   top.p_po01.get<uint32_t>()<<
   top.p_po00.get<uint32_t>()<< "\n"; 

   return 0;

}
