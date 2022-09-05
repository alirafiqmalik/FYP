import logging
import logicwire
import baseutils
from monosat import *
import copy

ERR_PR = 3
WAR_PR = 2
INF_PR = 1
DBG_PR = 0

def reduced_sat_attack(args):

    obf_bench_name = args.obfuscated
    orig_bench_address = args.original

    exe_func_time = 0
    exe_non_func_time = 0

    orgwires, orgpinwires, orgkeywires, orginterwires, orgpoutwires = logicwire.wire_dep(orig_bench_address)
    obfwires, obfpinwires, obfkeywires, obfinterwires, obfpoutwires = logicwire.wire_dep(obf_bench_name)

    list_dip = []
    orgcirc = [None] * len(orgpoutwires)
    str_dip = [None] * len(obfpinwires)
    list_str_dip = []
    list_orgcirc = []
    list_cpy_dip = []
    res = 1

    logging.debug("-------------obf wires------------")
    for i in range(0, len(obfwires)):
        logicwire.wire_print(obfwires[i], DBG_PR)

    logging.debug("-------------obf pin wires------------")
    for i in range(0, len(obfpinwires)):
        logicwire.wire_print(obfpinwires[i], DBG_PR)

    logging.debug("-----------obf key wires--------------")
    for i in range(0, len(obfkeywires)):
        logicwire.wire_print(obfkeywires[i], DBG_PR)

    logging.debug("-----------obf inter wires--------------")
    for i in range(0, len(obfinterwires)):
        logicwire.wire_print(obfinterwires[i], DBG_PR)

    logging.debug("-----------obf pout wires--------------")
    for i in range(0, len(obfpoutwires)):
        logicwire.wire_print(obfpoutwires[i], DBG_PR)

    logging.info("#############################################################")

    logging.debug("-----------org wires--------------")
    for i in range(0, len(orgwires)):
        logicwire.wire_print(orgwires[i], DBG_PR)

    logging.debug("-------------org pin wires------------")
    for i in range(0, len(orgpinwires)):
        logicwire.wire_print(orgpinwires[i], DBG_PR)

    logging.debug("-------------org key wires------------")
    for i in range(0, len(orgkeywires)):
        logicwire.wire_print(orgkeywires[i], DBG_PR)

    logging.debug("-------------org inter wires------------")
    for i in range(0, len(orginterwires)):
        logicwire.wire_print(orginterwires[i], DBG_PR)

    logging.debug("-------------org pout wires------------")
    for i in range(0, len(orgpoutwires)):
        logicwire.wire_print(orgpoutwires[i], DBG_PR)

    logging.warning("########## looking for DIPs (Iterative SAT Calls)  ##########")

    iter = 0
    keyin1 = [None] * len(obfkeywires)
    keyin2 = [None] * len(obfkeywires)
    keyinc = [None] * len(obfkeywires)

    for i in range(0, len(obfkeywires)):
        keyin1[i] = Var()
        keyin1[i].symbol = obfkeywires[i].name + "_1" + str(iter)
        logging.debug("keyin1 {} ==> {}".format(i, keyin1[i].getSymbol()))
        keyin2[i] = Var()
        keyin2[i].symbol = obfkeywires[i].name + "_2" + str(iter)
        logging.debug("keyin2 {} ==> {}".format(i, keyin2[i].getSymbol()))
        keyinc[i] = Var()
        keyinc[i].symbol = obfkeywires[i].name + "c"
        logging.debug("keyinc {} ==> {}".format(i, keyinc[i].getSymbol()))

    while res == 1:
        res, dscinp, new_func_time = baseutils.finddip(obfpinwires, obfkeywires, obfinterwires, obfpoutwires, list_dip,
                                                       list_orgcirc, keyin1, keyin2,
                                                       exe_func_time)  # duplicate and find dip

        # print("HERE ",list_dip,dscinp)
        if res == 1:
            orgcirc = logicwire.var_log_sim(dscinp, orgwires, iter)
            iter += 1
            list_dip.append(dscinp)
            # list_dip=list(set(list_dip)|set(dscinp))

            # print(dscinp)
            

            cpy_dscinp = dscinp.copy()
            
            #copy.deepcopy(dscinp)
            list_cpy_dip.append(cpy_dscinp)

            for i in range(0, len(dscinp)):
                if str(dscinp[i].value()) == "True":
                    str_dip[i] = "1"
                else:
                    str_dip[i] = "0"
            list_str_dip.append(str_dip)
            str_dip = [None] * len(obfpinwires)
            list_orgcirc.append(orgcirc)

            exe_func_time = new_func_time
        else:
            logging.info("=============================================================")
            logging.info("No more DIP ------------------------------- Iterations = {}".format(iter))
            logging.info("=============================================================")
            Monosat().newSolver()
        print("TsHERE ",len(list_dip),len(dscinp))
    
    
    logging.debug("================ re-initializing DIPs")
    new_list_dips = Var(true())
    for i in range(0, len(list_str_dip)):
        for j in range(0, len(list_str_dip[i])):
            if list_str_dip[i][j] == "1":
                list_dip[i][j] = Var(true())
                Solve(list_dip[i][j])
            elif list_str_dip[i][j] == "0":
                list_dip[i][j] = Var(false())
                Solve(Not(list_dip[i][j]))
            new_list_dips = And(new_list_dips, list_dip[i][j])
    logging.debug("================ keyFind SAT call")

    for i in range(0, len(list_dip)):
        for j in range(0, len(list_dip[i])):
            logging.debug("DIP {} [{}] = {}".format(i, j, list_dip[i][j].value()))
        logging.debug("")

    logging.warning("---------------- looking for key (Last SAT Call) ------------")
    func_keys = baseutils.findkey(obfkeywires, obfinterwires, obfpoutwires, list_dip, list_orgcirc, keyinc)

    found_keys = func_keys

    logging.info("=============================================================")
    logging.info("========================== keys ... =========================")
    logging.info("=============================================================")

    for i in range(0, len(func_keys)):
        logging.info("{} = {}".format(func_keys[i].getSymbol(), str(func_keys[i].value())))

    combined_key = [None] * len(found_keys)
    for i in range(0, len(found_keys)):
        key_name = found_keys[i].getSymbol()
        key_index = int(key_name[key_name.find("keyinput") + 8: key_name.find("c")])
        combined_key[key_index] = str(found_keys[i].value())
    # found_keys.sort(key=operator.attrgetter('symbol'))

    correct_key = [None] * len(combined_key)
    for i in range(0, len(combined_key)):
        if combined_key[i] == "True":
            correct_key[i] = "1"
        else:
            correct_key[i] = "0"





    logging.warning("=============================================================")
    logging.warning("=============================================================")
    logging.error("==================  Finish SAT solver ...  ==================")
    logging.warning("=============================================================")
    logging.warning("=============================================================")

    logging.error("key= {}".format(''.join(correct_key)))
    logging.error("func_iteration= {}; func_exe_time= {}; nonfunc_exe_time= {}".format(iter, exe_func_time, exe_non_func_time))

import argparse


parser = argparse.ArgumentParser()
# parser.add_argument("--algorithm", action="store", required=True, type=str, default="reduced_sat_attack", help="The selected algorithm (defense or attack)")
# parser.add_argument("--original", action="store", required=True, type=str, default="/home/alira/FYP/oracle/oracle.bench", help="original benchmark path")
# parser.add_argument("--obfuscated", action="store", required=True, type=str, default="/home/alira/FYP/tmp/tmp.bench", help="obfuscated benchmark path")
# parser.add_argument('--combined_dll', action="store", required=False, type=int, default=0, help="not used currently")
# parser.add_argument('--maximum_delay', action="store", required=False, type=int, default=10, help="Maximum Delay for a Combinational Cone")
# parser.add_argument('--minimum_delay', action="store", required=False, type=int, default=10, help="Minimum Delay for a Combinational Cone")
# parser.add_argument('--design_name', action="store", required=False, type=str, default="design", help="top module name")
# parser.add_argument('--iteration', action="store", required=False, type=int, default=0, help="iteration for limited run")
# parser.add_argument('--tag', action="store", required=False, type=str, default="run_0", help="current run tag")
# parser.add_argument('--rnd_percent', action="store", required=False, type=float, default=0.2, help="Percentage of Random Obfuscation")
# parser.add_argument('--key_str', action="store", required=False, type=str, default="0", help="Key used for SARLock")
# parser.add_argument("--verbose", action="store", required=False, type=int, default=0, help="verbosity level")

args = parser.parse_args()
args.obfuscated="/home/alira/FYP/smt_tmp/obf.bench"
args.original="/home/alira/FYP/smt_tmp/org.bench"


reduced_sat_attack(args)