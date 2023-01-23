import re
from src.utils import extract_io_b

bench=open("/home/alira/FYP/oracle/oracle.bench").read()
inputs= extract_io_b(bench,mode='input')
outputs= extract_io_b(bench,mode='output')

# print(inputs,outputs)


ri=""
for i,k in enumerate(inputs):
  ri+="top.p_{}.set<uint32_t>(get_bool(argv[1][{}]));\n".format(k,str(len(inputs)-i-1))


ro=""
for k in outputs:
   ro+="top.p_{}.get<bool>()<<".format(k)

# print(ro)

print(len(inputs))
print(inputs)

# code="""
# #include "tmp.cpp"
# #include <iostream>
# #include <bitset>
# #include <string>
# #include <cstring>

# int get_bool(char s){
# if(s=='1') return 1;
# else return 0;
# }

# int main(int argc, char **argv)
# {
#    if(argc!=2){std::cout <<\"ERROR!!! \\nIncorrect No of Inputs\n\"; return -1;}
#    for (int i = 1; i < argc; ++i){if(strlen(argv[i])!=10){std::cout <<"ERROR!!! \nInputs not 10 bits\n"; return -1;}}
   
#    cxxrtl_design::p_top top;\n"""+ri+ """top.step(); \n
#    std::cout <<"""+ro+""";\n 
#    return 0;
# }
# """



# with open("/home/alira/FYP/oracle/main.cpp",'w') as f:
#   f.write(code)