from src.utils import *
import re

        # bench=re.sub(i[1],tmpstr,bench)
        # bench=re.sub(i[0],tmpstr0,bench)
        # print(re.findall(i[0]+" = DFF\("+i[1]+"\)",bench))
        # print()
        # break
    # print(i)
        # bench=re.sub("OUTPUT({})".format(i[1]),"",bench)

        # tmpstr="FFQ_"+str(x) #i[0]+"FQ"
        # tmpstr0="FFD_"+str(x)

def rm_DFF(bench):
    tmpx=""
    tmpd=re.findall("(.*) = DFF\((.*)\)",bench)
    # inp=extract_io_b(bench)
    # out=extract_io_b(bench,mode="output")
    inp=[]
    out=[]
    for x,i in enumerate(tmpd):
        # print(reg_input,reg_output)    
        tmpx+=i[0]+" = DFF("+i[1]+")\n"      
        if(i[1] in inp):
            bench=re.sub(i[0]+" = DFF\("+i[1]+"\)","",bench)
            bench=re.sub(i[0],i[1],bench)
            print("inp",i)
        elif(i[0] in out):
            bench=re.sub(i[0]+" = DFF\("+i[1]+"\)","",bench)
            bench=re.sub(i[0],i[1],bench)
            print("out",i)
        else:
            tmpstr=i[0]+"FQ"#"FFQ_" #str(x)
            # tmpstr0="FFD_"+str(x)
            print(i)
            bench=re.sub(i[0]+" = DFF\("+i[1]+"\)","INPUT({})\nOUTPUT({})".format(i[0],tmpstr),bench)
            bench=re.sub(i[1],tmpstr,bench)

    return bench,x,tmpx



bench1=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench").read()
print("DONE1a")
bench2=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench").read()
print("DONE1b")


bench1,x1,tmpx1=rm_DFF(bench1)
print("DONE1")
bench2,x2,tmpx2=rm_DFF(bench2)
print("DONE2")
print(x2,x2)

with open("/home/alira/FYP/tmp/seqtmp2.bench","w") as f:
    f.write(tmpx2)

with open("/home/alira/FYP/tmp/seqtmp.bench","w") as f:
    f.write(tmpx1)

with open("/home/alira/FYP/tmp.bench","w") as f:
    f.write(bench1)

with open("/home/alira/FYP/tmp2.bench","w") as f:
    f.write(bench2)








# bench=open("/home/alira/FYP/python/tmpcir.bench").read()
# circuit=LogicLocking(bench)

# key=randKey(10, seed=10)
# print(key)
# circuit.RLL(n=10, key=key[0])

# circuit.graph_to_bench("/home/alira/FYP/tmp/tmp.bench")

# tmp=extract_gates_b(bench)

# print(tmp[0].keys())
# print(tmp[1])



# bench=open("/home/alira/FYP/tmp/tmp.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/obf.v","w") as f:
#     f.write(verilog)



# bench=open("/home/alira/FYP/tmp/tmp.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/tmpobf.v","w") as f:
#     f.write(verilog)


# bench=open("/home/alira/FYP/oracle/oracle.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/tmpobf.v","a") as f:
#     f.write("\n\n\n\n#oracle\n"+verilog)

# txt="#RESTORE DFF VALUES\n"

# for i in tmpd:
#     tmpi="{} = DFF({})".format(i[0],i[1])
#     txt+=tmpi+"\n"


# tmp=re.sub("(.*) = DFF\((.*)\)\n",r"INPUT(\1)\nOUTPUT(\2)\n",bench)

# with open("/home/alira/FYP/tmp/combo.bench","w") as f:
#     f.write(tmp)


# with open("/home/alira/FYP/tmp/seq.bench","w") as f:
#     f.write(txt)


# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp/tmprtl.v /home/alira/FYP/tmp/ortl.v
# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp/combo.bench /home/alira/FYP/tmp/combo2.bench

# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench b


# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp.bench /home/alira/FYP/tmp2.bench