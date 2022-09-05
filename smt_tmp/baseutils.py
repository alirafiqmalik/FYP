import logging
from monosat import *
import converts

def finddip(pinwires, keywires, interwires, poutwires, list_dip, list_orgcirc, keyin1, keyin2, exe_time):
    # print(list_dip)
    discinp = [None] * len(pinwires)

    outxored_right = [None] * len(poutwires)

    if list_dip:
        iter = len(list_dip)
    else:
        iter = 0

    outxnored_left = []

    dip_list = []

    for i in range(0, len(pinwires)):
        discinp[i] = Var()
        discinp[i].symbol = pinwires[i].name + "_" + str(iter)

    output_list1 = converts.circuit2bool(interwires, poutwires, discinp, keyin1)
    output_list2 = converts.circuit2bool(interwires, poutwires, discinp, keyin2)

    if list_dip:
        logging.warning("============================================= iteration: {}".format(len(list_dip)))

        # for i in range(0, len(list_dip)):
        print("DIPh: ",list_dip)
        for j in range(0, len(list_dip[len(list_dip) - 1])):
            logging.debug("{} = {}".format(list_dip[len(list_dip) - 1][j].symbol, str(list_dip[len(list_dip) - 1][j].value())))
        print("DIPh: ",list_dip)
        logging.debug("")
        for j in range(0, len(list_orgcirc[len(list_dip) - 1])):
            logging.debug("{} = {}".format(list_orgcirc[len(list_dip) - 1][j].symbol, str(list_orgcirc[len(list_dip) - 1][j].value())))
        logging.debug("")

        output_list_temp1 = converts.circuit2bool(interwires, poutwires, list_dip[len(list_dip) - 1], keyin1)
        output_list_temp2 = converts.circuit2bool(interwires, poutwires, list_dip[len(list_dip) - 1], keyin2)

        for j in range(0, len(output_list_temp1)):
            outxnored_left.append(Xnor(output_list_temp1[j], list_orgcirc[len(list_dip) - 1][j]))
            outxnored_left.append(Xnor(output_list_temp2[j], list_orgcirc[len(list_dip) - 1][j]))

        for i in range(0, len(list_dip)):
            for j in range(0, len(list_dip[i])):
                if str(list_dip[i][j].value()) == "True":
                    Assert(list_dip[i][j])
                elif str(list_dip[i][j].value()) == "False":
                    Assert(Not(list_dip[i][j]))

        # left_codition = And(outxnored_left)
        # dip_assert = And(dip_list)
        Assert(And(outxnored_left))
        # Assert(And(dip_list))

    else:
        logging.warning("============================================= iteration: {}".format(0))
        left_codition = Var(true())
        dip_assert = Var(true())

    for i in range(0, len(poutwires)):
        outxored_right[i] = Xor(output_list1[i], output_list2[i]) #different outputs
        logging.debug("{}A XOR {}B !!".format(output_list1[i].getSymbol(), output_list2[i].getSymbol()))

    # right_condition = Or(outxored_right)
    # Assert(Or(outxored_right))
    new_time = time.time()
    result = Solve(Or(outxored_right))  # Solve the instance in MonoSAT, return either True if the instance is SAT, and False if it is UNSAT
    new_time = time.time() - new_time
    # result = Solve()  # Solve the instance in MonoSAT, return either True if the instance is SAT, and False if it is UNSAT

    if result:
        logging.info("SAT")
        for i in range(0, len(pinwires)):
            logging.info("{} = {}".format(discinp[i].getSymbol(), str(discinp[i].value())))

        for i in range(0, len(keywires)):
            logging.info("{} = {}".format(keyin1[i].getSymbol(), str(keyin1[i].value())))

        for i in range(0, len(keywires)):
            logging.info("{} = {}".format(keyin2[i].getSymbol(),str(keyin2[i].value())))
        return 1, discinp, new_time+exe_time
    else:
        logging.warning("UNSAT")
        return -1, discinp, new_time+exe_time

