/home/alira/FYP/linux/yosys/build/yosys -p '
read_verilog /home/alira/FYP/tmp/tmporg.v
hierarchy -check -top top
# flatten
write_cxxrtl /home/alira/FYP/oracle/tmp.cpp
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# {gettmpv}write_verilog -noattr {rtlv}
# dfflibmap -liberty mycells.lib
# abc -liberty mycells.lib
# clean
# write_verilog -noattr {outputfile}
'

g++ -I/home/alira/FYP/linux/yosys -o /home/alira/FYP/oracle/oracle /home/alira/FYP/oracle/main.cpp
# oracle/oracle 0101001001

# https://github.com/alirafiqmalik/FYP.git