import re

code=open("/home/alira/FYP/linux/final.v").read()

FF=re.findall("( DFFSR .* \( .C\((\d+'h\d+|.*)\), .D\((\d+'h\d+|.*)\), .Q\((\d+'h\d+|.*)\), .R\((\d+'h\d+|.*)\), .S\((\d+'h\d+|.*)\) \) ;)",code)
ionodes=[]
for i in FF:
    ionodes=list(set(ionodes)|set(i[1:]))
print(len(ionodes))
# print(ionodes)

assign=re.findall("(assign (.*) = (.*) ;)",code)

print(len(assign))
print(assign[0][0])
print(assign[0][1])
print(assign[0][2])

re.sub("]",r"\[","")
# assign[0][1]=re.sub(r"]",r"\]",assign[0][1])

print(re.findall(assign[0][1],code))


with open("/home/alira/FYP/tmptxt.v","w") as f:
    f.write(code)
