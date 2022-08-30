from utils import format_verilog,io_port,extract_gates_b,extract_io_b,extract_gates_v,extract_io_v


def bench_to_verilog(bench):
    gates,gate_count = extract_gates_b(bench)
    inputs = extract_io_b(bench, mode="input")
    outputs = extract_io_b(bench, mode="output")

    gate_list = list(gates.keys())

    porti, input_dec = io_port(inputs, mode="input")
    porto, output_dec = io_port(outputs, mode="output")
    verilog = "module top ({},{});{}".format(
        porti, porto, input_dec+output_dec)

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

    verilog += "endmodule"

    verilog = format_verilog(verilog)

    return verilog, gate_count


def verilog_to_bench(verilog):
    verilog = format_verilog(verilog)
    gates = extract_gates_v(verilog)
    inputs = extract_io_v(verilog, mode="input")
    outputs = extract_io_v(verilog, mode="output")
    
    
    bench=""
    for i in inputs:
        bench+="INPUT({})".format(i)
    # print(bench)
    # print(gates)
    
    

    return bench

####################################################################################################################################
####################################################################################################################################
# ver=open("/home/alira/FYP/linux/output.v").read()
# verilog_to_bench(ver)