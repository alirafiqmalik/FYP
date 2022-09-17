class Node():
    def __init__(self, name, inputs, type2):
        self.name = name
        self.inputs = inputs
        self.type = type2
        self.z3_repr = None
        # print("HERE = ",name,"-",inputs,"-",type2)
        # print("THERE = ",type(name),type(inputs),type(type2))

    def __str__(self):
        return "<" + str(self.name) + ": " + str(self.type) + " " + str(self.inputs) + ">"

    def __repr__(self):
        return "<" + str(self.name) + ": " + str(self.type) + " " + str(self.inputs) + ">"
