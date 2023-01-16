import re
from src.utils import format_verilog,io_port,extract_gates_b,extract_io_b,extract_io_v,extract_gates_v


def bench_to_verilog(bench,clkpin="Clock",modulename="top"):
    gates,gate_count = extract_gates_b(bench)
    # print("HERE ",gates)
    inputs = extract_io_b(bench, mode="input")
    outputs = extract_io_b(bench, mode="output")

    gate_list = list(gates.keys())

    # print("tmpcheck",gates["DFF"])

    if(("DFF" in gate_list) and clkpin not in inputs):
        print("DFF IN CIRCUIT")
        clockp=","+clkpin
        clockio="input {};".format(clkpin)
    else:
        clockio=""
        clockp=""

    porti, input_dec,replace_i = io_port(inputs, mode="input")
    porto, output_dec,replace_o = io_port(outputs, mode="output")
    verilog = "module {} ({},{});{}".format(modulename,
        porti+clockp, porto, input_dec+output_dec+clockio)

    # clock=""
    # if("DFF" in gate_list):
    #     for k in inputs:
    #         if(("clk" in k.lower()) or ("clock" in k.lower())):
    #             clock=k
    #     if(clock==""):
    #         print("################### ERROR ###################")
        
    #     for i in gates["DFF"]:
    #         verilog += "reg "+i[0]+" ;"

    #     verilog+="always@(posedge {})begin ".format(clock)
    #     for i in gates["DFF"]:
    #         verilog += i[0]+" = "+i[1]+" ;"
    #     verilog+=" end "
        

    
    for i in gate_list:
        tmp = gates[i]
        
        if i == 'NOT':
            for j in tmp:
                verilog += "assign " + j[0]+" = ~"+j[1]+" ;"
        elif i == 'BUF':
            for j in tmp:
                verilog += "assign " + j[0]+" = "+j[1]+" ;"
        elif i == "AND":
            for j in tmp:
                verilog += "assign " + j[0]+" = "+j[1]+" & "+j[2]+" ;"
        elif i == "NAND":
            for j in tmp:
                verilog += "assign " + j[0]+" = ~("+j[1]+" & "+j[2]+") ;"
        elif i == "OR":
            for j in tmp:
                verilog += "assign " + j[0]+" = "+j[1]+" | "+j[2]+" ;"
        elif i == "NOR":
            for j in tmp:
                verilog += "assign " + j[0]+" = ~("+j[1]+" | "+j[2]+") ;"
        elif i == "XOR":
            for j in tmp:
                verilog += "assign " + j[0]+" = "+j[1]+" ^ "+j[2]+" ;"
        elif i == "XNOR":
            for j in tmp:
                verilog += "assign " + j[0]+" = ~("+j[1]+" ^ "+j[2]+") ;"
        elif i == "DFF":
            # print(tmp)
            for j in tmp:
                verilog += "reg {};always@(posedge {})begin {}<={}; end ".format(j[0],clkpin,j[0],j[1])


    verilog += "endmodule"

    
    verilog = format_verilog(verilog)
    # # print("CHECK VAL=",replace_i,replace_o)
    # # print(porti)
    # # print(porto)
    # if(replace_i):
    #     # print("replacei")
    #     for i in replace_i:
    #         # print(i)
    #         # print(re.findall(i+"_\d+_?",verilog))
    #         verilog=re.sub(i+"_(\d+)_?",i+"["+r"\1"+"]",verilog)
    # if(replace_o):
    #     # print("replaceo")
    #     for i in replace_o:
    #         # print(i)
    #         # print(re.findall(i+"_\d+_?",verilog))
    #         verilog=re.sub(i+"_(\d+)_?",i+"["+r"\1"+"]",verilog)


    return verilog, gate_count



####################################################################################################################################
####################################################################################################################################
# ver=open("/home/alira/FYP/linux/output.v").read()
# verilog_to_bench(ver)