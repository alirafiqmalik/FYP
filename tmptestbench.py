import re





module_input_init=".N1(N1),.N107(N107),.N116(N116),.N124(N124),.N125(N125),.N128(N128),.N13(N13),.N132(N132),.N137(N137),.N143(N143),.N150(N150),.N159(N159),.N169(N169),.N179(N179),.N190(N190),.N20(N20),.N200(N200),.N213(N213),.N222(N222),.N223(N223),.N226(N226),.N232(N232),.N238(N238),.N244(N244),.N250(N250),.N257(N257),.N264(N264),.N270(N270),.N274(N274),.N283(N283),.N294(N294),.N303(N303),.N311(N311),.N317(N317),.N322(N322),.N326(N326),.N329(N329),.N33(N33),.N330(N330),.N343(N343),.N349(N349),.N350(N350),.N41(N41),.N45(N45),.N50(N50),.N58(N58),.N68(N68),.N77(N77),.N87(N87),.N97(N97),.keyinput_4(keyinput_4),.keyinput_3(keyinput_3),.keyinput_2(keyinput_2),.keyinput_0(keyinput_0),.keyinput_1(keyinput_1),"

key_inputs_p="keyinput_4,keyinput_3,keyinput_2,keyinput_0,keyinput_1,"
cir_inputs_p="N1,N107,N116,N124,N125,N128,N13,N132,N137,N143,N150,N159,N169,N179,N190,N20,N200,N213,N222,N223,N226,N232,N238,N244,N250,N257,N264,N270,N274,N283,N294,N303,N311,N317,N322,N326,N329,N33,N330,N343,N349,N350,N41,N45,N50,N58,N68,N77,N87,N97,"









x=testbench.format(key_inputs_p=key_inputs_p[:-1],
                    cir_inputs_p=cir_inputs_p[:-1],
                    log_path="logfile.txt",
                    top_port=module_input_init[:-1]
                    )

