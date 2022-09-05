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
      if(strlen(argv[i])!=41){std::cout <<"ERROR!!! \nInputs not 10 bits\n"; return -1;}
}




   cxxrtl_design::p_top top;


top.p_G99gat.set<uint32_t>(get_bool(argv[1][40]));
top.p_G92gat.set<uint32_t>(get_bool(argv[1][39]));
top.p_G8gat.set<uint32_t>(get_bool(argv[1][38]));
top.p_G85gat.set<uint32_t>(get_bool(argv[1][37]));
top.p_G78gat.set<uint32_t>(get_bool(argv[1][36]));
top.p_G71gat.set<uint32_t>(get_bool(argv[1][35]));
top.p_G64gat.set<uint32_t>(get_bool(argv[1][34]));
top.p_G57gat.set<uint32_t>(get_bool(argv[1][33]));
top.p_G50gat.set<uint32_t>(get_bool(argv[1][32]));
top.p_G43gat.set<uint32_t>(get_bool(argv[1][31]));
top.p_G36gat.set<uint32_t>(get_bool(argv[1][30]));
top.p_G29gat.set<uint32_t>(get_bool(argv[1][29]));
top.p_G233gat.set<uint32_t>(get_bool(argv[1][28]));
top.p_G232gat.set<uint32_t>(get_bool(argv[1][27]));
top.p_G231gat.set<uint32_t>(get_bool(argv[1][26]));
top.p_G230gat.set<uint32_t>(get_bool(argv[1][25]));
top.p_G22gat.set<uint32_t>(get_bool(argv[1][24]));
top.p_G229gat.set<uint32_t>(get_bool(argv[1][23]));
top.p_G228gat.set<uint32_t>(get_bool(argv[1][22]));
top.p_G227gat.set<uint32_t>(get_bool(argv[1][21]));
top.p_G226gat.set<uint32_t>(get_bool(argv[1][20]));
top.p_G225gat.set<uint32_t>(get_bool(argv[1][19]));
top.p_G218gat.set<uint32_t>(get_bool(argv[1][18]));
top.p_G211gat.set<uint32_t>(get_bool(argv[1][17]));
top.p_G204gat.set<uint32_t>(get_bool(argv[1][16]));
top.p_G1gat.set<uint32_t>(get_bool(argv[1][15]));
top.p_G197gat.set<uint32_t>(get_bool(argv[1][14]));
top.p_G190gat.set<uint32_t>(get_bool(argv[1][13]));
top.p_G183gat.set<uint32_t>(get_bool(argv[1][12]));
top.p_G176gat.set<uint32_t>(get_bool(argv[1][11]));
top.p_G169gat.set<uint32_t>(get_bool(argv[1][10]));
top.p_G162gat.set<uint32_t>(get_bool(argv[1][9]));
top.p_G15gat.set<uint32_t>(get_bool(argv[1][8]));
top.p_G155gat.set<uint32_t>(get_bool(argv[1][7]));
top.p_G148gat.set<uint32_t>(get_bool(argv[1][6]));
top.p_G141gat.set<uint32_t>(get_bool(argv[1][5]));
top.p_G134gat.set<uint32_t>(get_bool(argv[1][4]));
top.p_G127gat.set<uint32_t>(get_bool(argv[1][3]));
top.p_G120gat.set<uint32_t>(get_bool(argv[1][2]));
top.p_G113gat.set<uint32_t>(get_bool(argv[1][1]));
top.p_G106gat.set<uint32_t>(get_bool(argv[1][0]));


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




   top.step();

std::cout<<top.p_G1355gat.get<bool>()<<top.p_G1354gat.get<bool>()<<top.p_G1353gat.get<bool>()<<top.p_G1352gat.get<bool>()<<top.p_G1351gat.get<bool>()<<top.p_G1350gat.get<bool>()<<top.p_G1349gat.get<bool>()<<top.p_G1348gat.get<bool>()<<top.p_G1347gat.get<bool>()<<top.p_G1346gat.get<bool>()<<top.p_G1345gat.get<bool>()<<top.p_G1344gat.get<bool>()<<top.p_G1343gat.get<bool>()<<top.p_G1342gat.get<bool>()<<top.p_G1341gat.get<bool>()<<top.p_G1340gat.get<bool>()<<top.p_G1339gat.get<bool>()<<top.p_G1338gat.get<bool>()<<top.p_G1337gat.get<bool>()<<top.p_G1336gat.get<bool>()<<top.p_G1335gat.get<bool>()<<top.p_G1334gat.get<bool>()<<top.p_G1333gat.get<bool>()<<top.p_G1332gat.get<bool>()<<top.p_G1331gat.get<bool>()<<top.p_G1330gat.get<bool>()<<top.p_G1329gat.get<bool>()<<top.p_G1328gat.get<bool>()<<top.p_G1327gat.get<bool>()<<top.p_G1326gat.get<bool>()<<top.p_G1325gat.get<bool>()<<top.p_G1324gat.get<bool>();

   // std::cout <<   
   // top.p_po18.get<bool>()<<  
   // top.p_po17.get<bool>()<< 
   // top.p_po16.get<bool>()<< 
   // top.p_po15.get<bool>()<< 
   // top.p_po14.get<bool>()<< 
   // top.p_po13.get<bool>()<< 
   // top.p_po12.get<bool>()<< 
   // top.p_po11.get<bool>()<< 
   // top.p_po10.get<bool>()<< 
   // top.p_po09.get<bool>()<< 
   // top.p_po08.get<bool>()<< 
   // top.p_po07.get<bool>()<< 
   // top.p_po06.get<bool>()<< 
   // top.p_po05.get<bool>()<< 
   // top.p_po04.get<bool>()<< 
   // top.p_po03.get<bool>()<< 
   // top.p_po02.get<bool>()<< 
   // top.p_po01.get<bool>()<<
   // top.p_po00.get<bool>(); 

   return 0;

}
