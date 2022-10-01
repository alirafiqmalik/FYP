from src.utils import extract_gates_b



b=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench").read()
print(extract_gates_b(b)[0].keys())



