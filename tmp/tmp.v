// Benchmark "/home/alira/FYP/org" written by ABC on Sat Oct 29 23:43:44 2022

module \/home/alira/FYP/org  ( 
    clk, rst, rxd_i, cts_i, sio_ce, sio_ce_x4, din_i_7_, din_i_6_,
    din_i_5_, din_i_4_, din_i_3_, din_i_2_, din_i_1_, din_i_0_, re_i, we_i,
    rx_sio_ce, rx_bit_cnt_3, rx_go, rx_bit_cnt_0, rx_bit_cnt_1,
    rx_bit_cnt_2, rx_valid, rx_valid_r, tx_fifo_mem_0, tx_fifo_mem_7,
    tx_fifo_mem_6, tx_fifo_mem_5, tx_fifo_mem_4, tx_fifo_mem_3,
    tx_fifo_mem_2, tx_fifo_mem_1, tx_fifo_mem_8, tx_fifo_mem_15,
    tx_fifo_mem_14, tx_fifo_mem_13, tx_fifo_mem_12, tx_fifo_mem_11,
    tx_fifo_mem_10, tx_fifo_mem_9, txf_empty_r, load, tx_fifo_gb,
    tx_bit_cnt_0, tx_bit_cnt_1, tx_bit_cnt_2, tx_bit_cnt_3, shift_en,
    tx_fifo_mem_16, tx_fifo_mem_23, tx_fifo_mem_22, tx_fifo_mem_21,
    tx_fifo_mem_20, tx_fifo_mem_19, tx_fifo_mem_18, tx_fifo_mem_17,
    tx_fifo_mem_24, tx_fifo_mem_31, hold_reg_8, tx_fifo_mem_30, hold_reg_7,
    tx_fifo_mem_29, hold_reg_6, tx_fifo_mem_28, hold_reg_5, tx_fifo_mem_27,
    hold_reg_4, tx_fifo_mem_26, hold_reg_3, tx_fifo_mem_25, hold_reg_2,
    hold_reg_1, rx_fifo_mem_16, rx_fifo_mem_23, rx_fifo_mem_22, rx_fifo_gb,
    dpll_state_0, dpll_state_1, rxr_9, rxr_8, rxr_7, rxr_6, rxr_5, rxr_4,
    rxr_3, tx_fifo_wp_0, tx_fifo_rp_0, tx_fifo_rp_1, rx_fifo_rp_0,
    rx_fifo_rp_1, rx_fifo_wp_1, rx_fifo_wp_0, rx_fifo_mem_21,
    rx_fifo_mem_20, rx_fifo_mem_19, rx_fifo_mem_18, rx_fifo_mem_17,
    rx_fifo_mem_0, rx_fifo_mem_7, rx_fifo_mem_6, rx_fifo_mem_5,
    rx_fifo_mem_4, rx_fifo_mem_3, rx_fifo_mem_2, rx_fifo_mem_1,
    rx_fifo_mem_8, rx_fifo_mem_24, rx_fifo_mem_15, rx_fifo_mem_14,
    rx_fifo_mem_13, rx_fifo_mem_12, rx_fifo_mem_11, rx_fifo_mem_10,
    rx_fifo_mem_9, rx_fifo_mem_31, rx_fifo_mem_30, rx_fifo_mem_29,
    rx_fifo_mem_28, rx_fifo_mem_27, rx_fifo_mem_26, rx_fifo_mem_25,
    tx_fifo_wp_1, rx_sio_ce_r2, rx_sio_ce_r1, shift_en_r, change, txd_o,
    rxr_2, hold_reg_9, hold_reg_0, rxd_r,
    rts_o, dout_o_7_, dout_o_6_, dout_o_5_, dout_o_4_, dout_o_3_,
    dout_o_2_, dout_o_1_, dout_o_0_, full_o, empty_o, rx_sio_ce_Q,
    rx_bit_cnt_3_Q, rx_go_Q, rx_bit_cnt_0_Q, rx_bit_cnt_1_Q,
    rx_bit_cnt_2_Q, rx_valid_D, tx_fifo_mem_0_Q, tx_fifo_mem_7_Q,
    tx_fifo_mem_6_Q, tx_fifo_mem_5_Q, tx_fifo_mem_4_Q, tx_fifo_mem_3_Q,
    tx_fifo_mem_2_Q, tx_fifo_mem_1_Q, tx_fifo_mem_8_Q, tx_fifo_mem_15_Q,
    tx_fifo_mem_14_Q, tx_fifo_mem_13_Q, tx_fifo_mem_12_Q, tx_fifo_mem_11_Q,
    tx_fifo_mem_10_Q, tx_fifo_mem_9_Q, txf_empty_r_Q, load_Q, tx_fifo_gb_Q,
    tx_bit_cnt_0_Q, tx_bit_cnt_1_Q, tx_bit_cnt_2_Q, tx_bit_cnt_3_Q,
    shift_en_Q, tx_fifo_mem_16_Q, tx_fifo_mem_23_Q, tx_fifo_mem_22_Q,
    tx_fifo_mem_21_Q, tx_fifo_mem_20_Q, tx_fifo_mem_19_Q, tx_fifo_mem_18_Q,
    tx_fifo_mem_17_Q, tx_fifo_mem_24_Q, tx_fifo_mem_31_Q, hold_reg_8_Q,
    tx_fifo_mem_30_Q, hold_reg_7_Q, tx_fifo_mem_29_Q, hold_reg_6_Q,
    tx_fifo_mem_28_Q, hold_reg_5_Q, tx_fifo_mem_27_Q, hold_reg_4_Q,
    tx_fifo_mem_26_Q, hold_reg_3_Q, tx_fifo_mem_25_Q, hold_reg_2_Q,
    hold_reg_1_Q, rx_fifo_mem_16_Q, rx_fifo_mem_23_Q, rx_fifo_mem_22_Q,
    rx_fifo_gb_Q, dpll_state_0_Q, dpll_state_1_Q, rxr_9_Q, rxr_8_Q,
    rxr_7_Q, rxr_6_Q, rxr_5_Q, rxr_4_Q, rxr_3_Q, tx_fifo_wp_0_Q,
    tx_fifo_rp_0_Q, tx_fifo_rp_1_Q, rx_fifo_rp_0_Q, rx_fifo_rp_1_Q,
    rx_fifo_wp_1_Q, rx_fifo_wp_0_Q, rx_fifo_mem_21_Q, rx_fifo_mem_20_Q,
    rx_fifo_mem_19_Q, rx_fifo_mem_18_Q, rx_fifo_mem_17_Q, rx_fifo_mem_0_Q,
    rx_fifo_mem_7_Q, rx_fifo_mem_6_Q, rx_fifo_mem_5_Q, rx_fifo_mem_4_Q,
    rx_fifo_mem_3_Q, rx_fifo_mem_2_Q, rx_fifo_mem_1_Q, rx_fifo_mem_8_Q,
    rx_fifo_mem_24_Q, rx_fifo_mem_15_Q, rx_fifo_mem_14_Q, rx_fifo_mem_13_Q,
    rx_fifo_mem_12_Q, rx_fifo_mem_11_Q, rx_fifo_mem_10_Q, rx_fifo_mem_9_Q,
    rx_fifo_mem_31_Q, rx_fifo_mem_30_Q, rx_fifo_mem_29_Q, rx_fifo_mem_28_Q,
    rx_fifo_mem_27_Q, rx_fifo_mem_26_Q, rx_fifo_mem_25_Q, tx_fifo_wp_1_Q,
    rx_sio_ce_r1_D, shift_en_r_Q, change_Q, txd_o_D, rxr_2_Q, hold_reg_9_Q,
    hold_reg_0_Q, rxd_r_Q  );
  input  clk, rst, rxd_i, cts_i, sio_ce, sio_ce_x4, din_i_7_, din_i_6_,
    din_i_5_, din_i_4_, din_i_3_, din_i_2_, din_i_1_, din_i_0_, re_i, we_i,
    rx_sio_ce, rx_bit_cnt_3, rx_go, rx_bit_cnt_0, rx_bit_cnt_1,
    rx_bit_cnt_2, rx_valid, rx_valid_r, tx_fifo_mem_0, tx_fifo_mem_7,
    tx_fifo_mem_6, tx_fifo_mem_5, tx_fifo_mem_4, tx_fifo_mem_3,
    tx_fifo_mem_2, tx_fifo_mem_1, tx_fifo_mem_8, tx_fifo_mem_15,
    tx_fifo_mem_14, tx_fifo_mem_13, tx_fifo_mem_12, tx_fifo_mem_11,
    tx_fifo_mem_10, tx_fifo_mem_9, txf_empty_r, load, tx_fifo_gb,
    tx_bit_cnt_0, tx_bit_cnt_1, tx_bit_cnt_2, tx_bit_cnt_3, shift_en,
    tx_fifo_mem_16, tx_fifo_mem_23, tx_fifo_mem_22, tx_fifo_mem_21,
    tx_fifo_mem_20, tx_fifo_mem_19, tx_fifo_mem_18, tx_fifo_mem_17,
    tx_fifo_mem_24, tx_fifo_mem_31, hold_reg_8, tx_fifo_mem_30, hold_reg_7,
    tx_fifo_mem_29, hold_reg_6, tx_fifo_mem_28, hold_reg_5, tx_fifo_mem_27,
    hold_reg_4, tx_fifo_mem_26, hold_reg_3, tx_fifo_mem_25, hold_reg_2,
    hold_reg_1, rx_fifo_mem_16, rx_fifo_mem_23, rx_fifo_mem_22, rx_fifo_gb,
    dpll_state_0, dpll_state_1, rxr_9, rxr_8, rxr_7, rxr_6, rxr_5, rxr_4,
    rxr_3, tx_fifo_wp_0, tx_fifo_rp_0, tx_fifo_rp_1, rx_fifo_rp_0,
    rx_fifo_rp_1, rx_fifo_wp_1, rx_fifo_wp_0, rx_fifo_mem_21,
    rx_fifo_mem_20, rx_fifo_mem_19, rx_fifo_mem_18, rx_fifo_mem_17,
    rx_fifo_mem_0, rx_fifo_mem_7, rx_fifo_mem_6, rx_fifo_mem_5,
    rx_fifo_mem_4, rx_fifo_mem_3, rx_fifo_mem_2, rx_fifo_mem_1,
    rx_fifo_mem_8, rx_fifo_mem_24, rx_fifo_mem_15, rx_fifo_mem_14,
    rx_fifo_mem_13, rx_fifo_mem_12, rx_fifo_mem_11, rx_fifo_mem_10,
    rx_fifo_mem_9, rx_fifo_mem_31, rx_fifo_mem_30, rx_fifo_mem_29,
    rx_fifo_mem_28, rx_fifo_mem_27, rx_fifo_mem_26, rx_fifo_mem_25,
    tx_fifo_wp_1, rx_sio_ce_r2, rx_sio_ce_r1, shift_en_r, change, txd_o,
    rxr_2, hold_reg_9, hold_reg_0, rxd_r;
  output rts_o, dout_o_7_, dout_o_6_, dout_o_5_, dout_o_4_, dout_o_3_,
    dout_o_2_, dout_o_1_, dout_o_0_, full_o, empty_o, rx_sio_ce_Q,
    rx_bit_cnt_3_Q, rx_go_Q, rx_bit_cnt_0_Q, rx_bit_cnt_1_Q,
    rx_bit_cnt_2_Q, rx_valid_D, tx_fifo_mem_0_Q, tx_fifo_mem_7_Q,
    tx_fifo_mem_6_Q, tx_fifo_mem_5_Q, tx_fifo_mem_4_Q, tx_fifo_mem_3_Q,
    tx_fifo_mem_2_Q, tx_fifo_mem_1_Q, tx_fifo_mem_8_Q, tx_fifo_mem_15_Q,
    tx_fifo_mem_14_Q, tx_fifo_mem_13_Q, tx_fifo_mem_12_Q, tx_fifo_mem_11_Q,
    tx_fifo_mem_10_Q, tx_fifo_mem_9_Q, txf_empty_r_Q, load_Q, tx_fifo_gb_Q,
    tx_bit_cnt_0_Q, tx_bit_cnt_1_Q, tx_bit_cnt_2_Q, tx_bit_cnt_3_Q,
    shift_en_Q, tx_fifo_mem_16_Q, tx_fifo_mem_23_Q, tx_fifo_mem_22_Q,
    tx_fifo_mem_21_Q, tx_fifo_mem_20_Q, tx_fifo_mem_19_Q, tx_fifo_mem_18_Q,
    tx_fifo_mem_17_Q, tx_fifo_mem_24_Q, tx_fifo_mem_31_Q, hold_reg_8_Q,
    tx_fifo_mem_30_Q, hold_reg_7_Q, tx_fifo_mem_29_Q, hold_reg_6_Q,
    tx_fifo_mem_28_Q, hold_reg_5_Q, tx_fifo_mem_27_Q, hold_reg_4_Q,
    tx_fifo_mem_26_Q, hold_reg_3_Q, tx_fifo_mem_25_Q, hold_reg_2_Q,
    hold_reg_1_Q, rx_fifo_mem_16_Q, rx_fifo_mem_23_Q, rx_fifo_mem_22_Q,
    rx_fifo_gb_Q, dpll_state_0_Q, dpll_state_1_Q, rxr_9_Q, rxr_8_Q,
    rxr_7_Q, rxr_6_Q, rxr_5_Q, rxr_4_Q, rxr_3_Q, tx_fifo_wp_0_Q,
    tx_fifo_rp_0_Q, tx_fifo_rp_1_Q, rx_fifo_rp_0_Q, rx_fifo_rp_1_Q,
    rx_fifo_wp_1_Q, rx_fifo_wp_0_Q, rx_fifo_mem_21_Q, rx_fifo_mem_20_Q,
    rx_fifo_mem_19_Q, rx_fifo_mem_18_Q, rx_fifo_mem_17_Q, rx_fifo_mem_0_Q,
    rx_fifo_mem_7_Q, rx_fifo_mem_6_Q, rx_fifo_mem_5_Q, rx_fifo_mem_4_Q,
    rx_fifo_mem_3_Q, rx_fifo_mem_2_Q, rx_fifo_mem_1_Q, rx_fifo_mem_8_Q,
    rx_fifo_mem_24_Q, rx_fifo_mem_15_Q, rx_fifo_mem_14_Q, rx_fifo_mem_13_Q,
    rx_fifo_mem_12_Q, rx_fifo_mem_11_Q, rx_fifo_mem_10_Q, rx_fifo_mem_9_Q,
    rx_fifo_mem_31_Q, rx_fifo_mem_30_Q, rx_fifo_mem_29_Q, rx_fifo_mem_28_Q,
    rx_fifo_mem_27_Q, rx_fifo_mem_26_Q, rx_fifo_mem_25_Q, tx_fifo_wp_1_Q,
    rx_sio_ce_r1_D, shift_en_r_Q, change_Q, txd_o_D, rxr_2_Q, hold_reg_9_Q,
    hold_reg_0_Q, rxd_r_Q;
  wire new_n939_, new_n717_, new_n827_, new_n786_, new_n1014_, new_n596_,
    new_n586_, new_n716_, new_n802_, new_n601_, new_n700_, new_n604_,
    new_n594_, new_n599_, new_n591_, new_n580_, new_n595_, new_n587_,
    new_n606_, new_n581_, new_n582_, new_n589_, new_n583_, new_n598_,
    new_n584_, new_n585_, new_n593_, new_n745_, new_n600_, new_n588_,
    new_n590_, new_n911_, new_n602_, new_n616_, new_n686_, new_n639_,
    new_n597_, new_n683_, new_n684_, new_n751_, new_n609_, new_n610_,
    new_n699_, new_n611_, new_n938_, new_n942_, new_n612_, new_n750_,
    new_n615_, new_n614_, new_n618_, new_n617_, new_n620_, new_n619_,
    new_n622_, new_n621_, new_n624_, new_n623_, new_n626_, new_n625_,
    new_n629_, new_n628_, new_n630_, new_n795_, new_n754_, new_n632_,
    new_n794_, new_n1102_, new_n633_, new_n721_, new_n736_, new_n636_,
    new_n637_, new_n638_, new_n744_, new_n641_, new_n660_, new_n640_,
    new_n642_, new_n644_, new_n646_, new_n676_, new_n645_, new_n648_,
    new_n647_, new_n650_, new_n649_, new_n652_, new_n651_, new_n654_,
    new_n653_, new_n656_, new_n655_, new_n658_, new_n657_, new_n662_,
    new_n661_, new_n664_, new_n663_, new_n666_, new_n665_, new_n668_,
    new_n667_, new_n670_, new_n669_, new_n672_, new_n671_, new_n674_,
    new_n673_, new_n678_, new_n677_, new_n921_, new_n681_, new_n679_,
    new_n680_, new_n682_, new_n828_, new_n917_, new_n1158_, new_n688_,
    new_n687_, new_n738_, new_n690_, new_n693_, new_n689_, new_n691_,
    new_n692_, new_n696_, new_n694_, new_n695_, new_n698_, new_n703_,
    new_n701_, new_n702_, new_n704_, new_n723_, new_n805_, new_n705_,
    new_n710_, new_n708_, new_n711_, new_n712_, new_n734_, new_n713_,
    new_n718_, new_n720_, new_n722_, new_n728_, new_n719_, new_n724_,
    new_n725_, new_n729_, new_n726_, new_n732_, new_n730_, new_n731_,
    new_n733_, new_n735_, new_n740_, new_n737_, new_n739_, new_n742_,
    new_n741_, new_n743_, new_n747_, new_n746_, new_n749_, new_n753_,
    new_n752_, new_n755_, new_n1108_, new_n782_, new_n757_, new_n769_,
    new_n760_, new_n761_, new_n801_, new_n762_, new_n764_, new_n763_,
    new_n773_, new_n776_, new_n767_, new_n775_, new_n766_, new_n768_,
    new_n770_, new_n771_, new_n772_, new_n774_, new_n780_, new_n777_,
    new_n778_, new_n783_, new_n779_, new_n781_, new_n785_, new_n784_,
    new_n803_, new_n788_, new_n791_, new_n789_, new_n790_, new_n792_,
    new_n793_, new_n796_, new_n798_, new_n1112_, new_n804_, new_n821_,
    new_n807_, new_n820_, new_n806_, new_n809_, new_n808_, new_n811_,
    new_n810_, new_n813_, new_n812_, new_n815_, new_n814_, new_n817_,
    new_n816_, new_n819_, new_n818_, new_n823_, new_n822_, new_n826_,
    new_n825_, new_n915_, new_n829_, new_n832_, new_n830_, new_n831_,
    new_n838_, new_n836_, new_n923_, new_n834_, new_n835_, new_n837_,
    new_n840_, new_n839_, new_n841_, new_n844_, new_n842_, new_n843_,
    new_n850_, new_n845_, new_n848_, new_n846_, new_n847_, new_n849_,
    new_n852_, new_n851_, new_n853_, new_n856_, new_n854_, new_n855_,
    new_n862_, new_n857_, new_n860_, new_n858_, new_n859_, new_n861_,
    new_n864_, new_n863_, new_n865_, new_n868_, new_n866_, new_n867_,
    new_n874_, new_n869_, new_n872_, new_n870_, new_n871_, new_n873_,
    new_n876_, new_n875_, new_n877_, new_n880_, new_n878_, new_n879_,
    new_n886_, new_n881_, new_n884_, new_n882_, new_n883_, new_n885_,
    new_n888_, new_n887_, new_n889_, new_n892_, new_n890_, new_n891_,
    new_n898_, new_n893_, new_n896_, new_n894_, new_n895_, new_n897_,
    new_n900_, new_n899_, new_n901_, new_n904_, new_n902_, new_n903_,
    new_n910_, new_n905_, new_n908_, new_n906_, new_n907_, new_n909_,
    new_n913_, new_n912_, new_n914_, new_n919_, new_n916_, new_n918_,
    new_n927_, new_n920_, new_n925_, new_n922_, new_n924_, new_n926_,
    new_n928_, new_n936_, new_n935_, new_n946_, new_n1001_, new_n941_,
    new_n940_, new_n944_, new_n1005_, new_n943_, new_n1009_, new_n948_,
    new_n1010_, new_n947_, new_n950_, new_n949_, new_n952_, new_n951_,
    new_n954_, new_n953_, new_n956_, new_n955_, new_n958_, new_n957_,
    new_n960_, new_n959_, new_n962_, new_n961_, new_n964_, new_n963_,
    new_n966_, new_n965_, new_n968_, new_n967_, new_n970_, new_n969_,
    new_n972_, new_n971_, new_n974_, new_n973_, new_n976_, new_n975_,
    new_n978_, new_n977_, new_n980_, new_n979_, new_n982_, new_n981_,
    new_n984_, new_n983_, new_n986_, new_n985_, new_n988_, new_n987_,
    new_n990_, new_n989_, new_n992_, new_n991_, new_n994_, new_n993_,
    new_n996_, new_n995_, new_n1000_, new_n999_, new_n1004_, new_n1003_,
    new_n1008_, new_n1007_, new_n1012_, new_n1011_, new_n1013_, new_n1016_,
    new_n1015_, new_n1021_, new_n1019_, new_n1097_, new_n1018_, new_n1020_,
    new_n1022_, new_n1026_, new_n1024_, new_n1023_, new_n1025_, new_n1028_,
    new_n1027_, new_n1032_, new_n1030_, new_n1029_, new_n1031_, new_n1033_,
    new_n1037_, new_n1035_, new_n1034_, new_n1036_, new_n1039_, new_n1038_,
    new_n1043_, new_n1041_, new_n1040_, new_n1042_, new_n1044_, new_n1048_,
    new_n1046_, new_n1045_, new_n1047_, new_n1050_, new_n1049_, new_n1054_,
    new_n1052_, new_n1051_, new_n1053_, new_n1055_, new_n1059_, new_n1057_,
    new_n1056_, new_n1058_, new_n1061_, new_n1060_, new_n1065_, new_n1063_,
    new_n1062_, new_n1064_, new_n1066_, new_n1068_, new_n1067_, new_n1072_,
    new_n1071_, new_n1076_, new_n1074_, new_n1073_, new_n1075_, new_n1077_,
    new_n1079_, new_n1078_, new_n1083_, new_n1082_, new_n1087_, new_n1085_,
    new_n1084_, new_n1086_, new_n1088_, new_n1090_, new_n1089_, new_n1095_,
    new_n1094_, new_n1101_, new_n1099_, new_n1098_, new_n1100_, new_n1105_,
    new_n1104_, new_n1111_, new_n1110_, new_n1115_, new_n1114_, new_n1117_,
    new_n1116_, new_n1118_, new_n697_, new_n643_, new_n756_, new_n727_,
    new_n937_, new_n929_, new_n1160_, new_n1177_, new_n1183_, new_n1175_,
    new_n1181_, new_n709_, new_n707_, new_n706_, new_n945_, new_n1179_,
    new_n1166_, new_n603_, new_n1113_, new_n1161_, new_n1162_, new_n1163_,
    new_n1164_, new_n1165_, new_n1167_, new_n1168_, new_n1169_, new_n1170_,
    new_n1171_, new_n931_, new_n934_, new_n932_, new_n1176_, new_n1173_,
    new_n787_, new_n1174_, new_n1178_, new_n1190_, new_n1180_, new_n1182_,
    new_n1184_, new_n1185_, new_n1186_, new_n1187_, new_n997_, new_n1191_,
    new_n1188_, new_n1189_, new_n748_, new_n824_;
  assign rxd_r_Q = rxd_i;
  assign rts_o = new_n1158_;
  assign new_n939_ = ~new_n946_ | ~new_n938_;
  assign new_n717_ = ~new_n709_ & ~new_n708_;
  assign new_n827_ = ~rx_fifo_rp_1;
  assign new_n786_ = ~new_n803_ & ~tx_fifo_rp_1;
  assign new_n1014_ = ~new_n803_ | ~tx_fifo_rp_1;
  assign new_n596_ = ~new_n597_ & ~new_n744_;
  assign new_n586_ = ~new_n787_;
  assign new_n716_ = new_n723_ | rx_bit_cnt_1;
  assign new_n802_ = new_n1112_ | cts_i;
  assign rx_sio_ce_r1_D = ~new_n692_ & ~dpll_state_1;
  assign new_n601_ = ~rx_valid_r;
  assign new_n700_ = change | dpll_state_0;
  assign new_n604_ = ~new_n751_ | ~rx_valid;
  assign new_n594_ = ~rx_fifo_rp_1 | ~new_n595_;
  assign new_n599_ = ~rx_valid;
  assign rx_fifo_mem_16_Q = ~new_n591_ | ~new_n590_;
  assign new_n591_ = ~new_n911_ | ~rxr_2;
  assign new_n580_ = new_n593_ & new_n594_;
  assign new_n595_ = ~new_n750_;
  assign new_n587_ = ~rx_fifo_mem_16;
  assign new_n606_ = ~rx_fifo_gb;
  assign new_n581_ = ~new_n588_;
  assign new_n582_ = ~new_n588_;
  assign new_n589_ = ~new_n588_;
  assign new_n583_ = ~new_n580_ | ~new_n748_;
  assign new_n598_ = ~new_n686_ & ~new_n606_;
  assign new_n584_ = ~new_n756_ & ~new_n787_;
  assign new_n585_ = ~new_n756_ & ~new_n787_;
  assign new_n593_ = ~new_n600_ & ~new_n599_;
  assign new_n745_ = ~rx_fifo_wp_0;
  assign new_n600_ = ~rx_fifo_wp_0 | ~new_n601_;
  assign rx_fifo_mem_15_Q = ~new_n647_ | ~new_n648_;
  assign rx_fifo_mem_14_Q = ~new_n649_ | ~new_n650_;
  assign rx_fifo_mem_13_Q = ~new_n651_ | ~new_n652_;
  assign rx_fifo_mem_12_Q = ~new_n653_ | ~new_n654_;
  assign rx_fifo_mem_11_Q = ~new_n655_ | ~new_n656_;
  assign rx_fifo_mem_10_Q = ~new_n657_ | ~new_n658_;
  assign rx_fifo_mem_9_Q = ~new_n661_ | ~new_n662_;
  assign rx_fifo_mem_31_Q = ~new_n663_ | ~new_n664_;
  assign rx_fifo_mem_30_Q = ~new_n665_ | ~new_n666_;
  assign rx_fifo_mem_29_Q = ~new_n667_ | ~new_n668_;
  assign rx_fifo_mem_28_Q = ~new_n669_ | ~new_n670_;
  assign rx_fifo_mem_27_Q = ~new_n671_ | ~new_n672_;
  assign rx_fifo_mem_26_Q = ~new_n673_ | ~new_n674_;
  assign rx_fifo_mem_25_Q = ~new_n677_ | ~new_n678_;
  assign rx_fifo_mem_8_Q = ~new_n640_ | ~new_n641_;
  assign rx_fifo_mem_24_Q = ~new_n645_ | ~new_n646_;
  assign new_n588_ = ~new_n602_;
  assign new_n590_ = new_n588_ | new_n587_;
  assign new_n911_ = ~new_n602_;
  assign new_n602_ = ~new_n603_ | ~new_n752_;
  assign new_n616_ = ~new_n580_ | ~new_n748_;
  assign new_n686_ = rx_fifo_rp_0 ^ rx_fifo_wp_0;
  assign new_n639_ = ~new_n683_ | ~new_n596_;
  assign new_n597_ = ~new_n748_ | ~new_n745_;
  assign new_n683_ = ~new_n598_ | ~new_n684_;
  assign new_n684_ = ~rx_fifo_rp_1 ^ rx_fifo_wp_1;
  assign new_n751_ = ~rx_fifo_wp_1;
  assign hold_reg_7_Q = new_n1037_ | new_n1036_;
  assign hold_reg_6_Q = new_n1048_ | new_n1047_;
  assign hold_reg_5_Q = new_n1059_ | new_n1058_;
  assign tx_fifo_wp_1_Q = new_n942_ & new_n612_;
  assign new_n609_ = tx_fifo_rp_1 & tx_fifo_rp_0;
  assign new_n610_ = new_n769_ | new_n768_;
  assign new_n699_ = new_n696_ | new_n695_;
  assign hold_reg_8_Q = new_n1026_ | new_n1025_;
  assign new_n611_ = ~tx_fifo_wp_0 | ~we_i;
  assign new_n938_ = ~tx_fifo_wp_1;
  assign new_n942_ = ~new_n932_ | ~new_n945_;
  assign new_n612_ = ~new_n611_ | ~new_n938_;
  assign new_n750_ = ~rx_fifo_gb | ~rx_fifo_rp_0;
  assign new_n615_ = ~new_n583_ | ~rx_fifo_mem_1;
  assign new_n614_ = ~new_n824_ | ~rxr_3;
  assign rx_fifo_mem_1_Q = ~new_n615_ | ~new_n614_;
  assign new_n618_ = ~new_n583_ | ~rx_fifo_mem_2;
  assign new_n617_ = ~new_n824_ | ~rxr_4;
  assign rx_fifo_mem_2_Q = ~new_n618_ | ~new_n617_;
  assign new_n620_ = ~new_n583_ | ~rx_fifo_mem_3;
  assign new_n619_ = ~new_n1191_ | ~rxr_5;
  assign rx_fifo_mem_3_Q = ~new_n619_ | ~new_n620_;
  assign new_n622_ = ~new_n583_ | ~rx_fifo_mem_4;
  assign new_n621_ = ~new_n824_ | ~rxr_6;
  assign rx_fifo_mem_4_Q = ~new_n622_ | ~new_n621_;
  assign new_n624_ = ~new_n583_ | ~rx_fifo_mem_5;
  assign new_n623_ = ~new_n1191_ | ~rxr_7;
  assign rx_fifo_mem_5_Q = ~new_n623_ | ~new_n624_;
  assign new_n626_ = ~new_n583_ | ~rx_fifo_mem_6;
  assign new_n625_ = ~new_n824_ | ~rxr_8;
  assign rx_fifo_mem_6_Q = ~new_n626_ | ~new_n625_;
  assign new_n629_ = ~new_n583_ | ~rx_fifo_mem_7;
  assign new_n628_ = ~new_n1191_ | ~rxr_9;
  assign rx_fifo_mem_7_Q = ~new_n628_ | ~new_n629_;
  assign new_n630_ = ~rx_sio_ce_r1;
  assign rx_sio_ce_Q = ~new_n630_ & ~rx_sio_ce_r2;
  assign new_n795_ = tx_fifo_rp_1 ^ new_n938_;
  assign new_n754_ = ~tx_fifo_wp_0;
  assign new_n632_ = new_n795_ ^ new_n754_;
  assign new_n794_ = ~tx_fifo_rp_0 ^ tx_fifo_wp_0;
  assign new_n1102_ = ~load | ~sio_ce;
  assign new_n633_ = ~new_n1102_ | ~tx_fifo_gb;
  assign new_n721_ = ~rx_bit_cnt_2;
  assign new_n736_ = ~new_n721_ | ~rx_bit_cnt_3;
  assign new_n636_ = ~rx_bit_cnt_0;
  assign new_n637_ = ~new_n636_ | ~rx_bit_cnt_1;
  assign rx_go_Q = new_n736_ | new_n637_;
  assign new_n638_ = ~new_n794_ | ~tx_fifo_gb;
  assign full_o = ~new_n638_ & ~new_n795_;
  assign new_n744_ = ~new_n601_ | ~rx_valid;
  assign new_n641_ = ~new_n639_ | ~rx_fifo_mem_8;
  assign new_n660_ = ~new_n639_;
  assign new_n640_ = ~new_n660_ | ~rxr_2;
  assign new_n642_ = ~new_n745_ | ~new_n751_;
  assign new_n644_ = ~new_n683_ | ~new_n643_;
  assign new_n646_ = ~new_n644_ | ~rx_fifo_mem_24;
  assign new_n676_ = ~new_n644_;
  assign new_n645_ = ~new_n676_ | ~rxr_2;
  assign new_n648_ = ~new_n639_ | ~rx_fifo_mem_15;
  assign new_n647_ = ~new_n660_ | ~rxr_9;
  assign new_n650_ = ~new_n639_ | ~rx_fifo_mem_14;
  assign new_n649_ = ~new_n660_ | ~rxr_8;
  assign new_n652_ = ~new_n639_ | ~rx_fifo_mem_13;
  assign new_n651_ = ~new_n660_ | ~rxr_7;
  assign new_n654_ = ~new_n639_ | ~rx_fifo_mem_12;
  assign new_n653_ = ~new_n660_ | ~rxr_6;
  assign new_n656_ = ~new_n639_ | ~rx_fifo_mem_11;
  assign new_n655_ = ~new_n660_ | ~rxr_5;
  assign new_n658_ = ~new_n639_ | ~rx_fifo_mem_10;
  assign new_n657_ = ~new_n660_ | ~rxr_4;
  assign new_n662_ = ~new_n639_ | ~rx_fifo_mem_9;
  assign new_n661_ = ~new_n660_ | ~rxr_3;
  assign new_n664_ = ~new_n644_ | ~rx_fifo_mem_31;
  assign new_n663_ = ~new_n676_ | ~rxr_9;
  assign new_n666_ = ~new_n644_ | ~rx_fifo_mem_30;
  assign new_n665_ = ~new_n676_ | ~rxr_8;
  assign new_n668_ = ~new_n644_ | ~rx_fifo_mem_29;
  assign new_n667_ = ~new_n676_ | ~rxr_7;
  assign new_n670_ = ~new_n644_ | ~rx_fifo_mem_28;
  assign new_n669_ = ~new_n676_ | ~rxr_6;
  assign new_n672_ = ~new_n644_ | ~rx_fifo_mem_27;
  assign new_n671_ = ~new_n676_ | ~rxr_5;
  assign new_n674_ = ~new_n644_ | ~rx_fifo_mem_26;
  assign new_n673_ = ~new_n676_ | ~rxr_4;
  assign new_n678_ = ~new_n644_ | ~rx_fifo_mem_25;
  assign new_n677_ = ~new_n676_ | ~rxr_3;
  assign new_n921_ = ~new_n827_ | ~rx_fifo_rp_0;
  assign new_n681_ = ~new_n921_ | ~re_i;
  assign new_n679_ = ~re_i;
  assign new_n680_ = ~new_n827_ | ~new_n679_;
  assign new_n682_ = ~new_n681_ | ~new_n680_;
  assign new_n828_ = ~rx_fifo_rp_0;
  assign new_n917_ = ~new_n828_ | ~rx_fifo_rp_1;
  assign rx_fifo_rp_1_Q = ~new_n682_ | ~new_n917_;
  assign new_n1158_ = ~new_n683_;
  assign new_n688_ = ~new_n684_ | ~new_n606_;
  assign new_n687_ = ~new_n686_;
  assign new_n738_ = ~new_n687_;
  assign empty_o = ~new_n688_ & ~new_n738_;
  assign rx_fifo_rp_0_Q = rx_fifo_rp_0 ^ re_i;
  assign new_n690_ = rxd_r_Q ^ rxd_r;
  assign new_n693_ = ~change;
  assign new_n689_ = ~new_n693_ & ~sio_ce_x4;
  assign new_n691_ = ~new_n690_ & ~new_n689_;
  assign change_Q = ~new_n691_ & ~new_n1166_;
  assign new_n692_ = ~dpll_state_0;
  assign new_n696_ = ~rx_sio_ce_r1_D & ~new_n693_;
  assign new_n694_ = ~dpll_state_0 & ~new_n697_;
  assign new_n695_ = ~new_n694_ & ~change;
  assign new_n698_ = ~dpll_state_0 | ~new_n697_;
  assign dpll_state_0_Q = ~new_n699_ | ~new_n698_;
  assign new_n703_ = ~rx_sio_ce_r1_D | ~sio_ce_x4;
  assign new_n701_ = ~new_n700_ | ~sio_ce_x4;
  assign new_n702_ = ~new_n701_ | ~dpll_state_1;
  assign dpll_state_1_Q = ~new_n703_ | ~new_n702_;
  assign new_n704_ = rx_sio_ce & rst;
  assign new_n723_ = ~new_n704_ | ~rx_go;
  assign new_n805_ = ~rx_go;
  assign new_n705_ = ~new_n805_ | ~rxd_r;
  assign new_n710_ = ~new_n727_ & ~rx_bit_cnt_0;
  assign new_n708_ = ~new_n723_ & ~rx_bit_cnt_0;
  assign rx_bit_cnt_0_Q = ~new_n710_ & ~new_n717_;
  assign new_n711_ = ~new_n723_;
  assign new_n712_ = ~new_n711_ | ~rx_bit_cnt_0;
  assign new_n734_ = ~rx_bit_cnt_1;
  assign new_n713_ = ~new_n712_ | ~new_n734_;
  assign new_n718_ = ~new_n717_ | ~new_n716_;
  assign new_n720_ = ~new_n718_ | ~rx_bit_cnt_2;
  assign new_n722_ = ~rx_bit_cnt_0 | ~rx_bit_cnt_1;
  assign new_n728_ = ~new_n723_ & ~new_n722_;
  assign new_n719_ = ~new_n728_ | ~new_n721_;
  assign rx_bit_cnt_2_Q = ~new_n720_ | ~new_n719_;
  assign new_n724_ = ~new_n722_ & ~new_n721_;
  assign new_n725_ = ~new_n724_ & ~new_n723_;
  assign new_n729_ = ~rx_bit_cnt_3;
  assign new_n726_ = ~new_n725_ & ~new_n729_;
  assign new_n732_ = ~new_n727_ | ~new_n726_;
  assign new_n730_ = ~new_n728_ | ~rx_bit_cnt_2;
  assign new_n731_ = ~new_n730_ | ~new_n729_;
  assign new_n733_ = ~new_n732_ | ~new_n731_;
  assign rx_bit_cnt_3_Q = ~new_n733_ | ~rst;
  assign new_n735_ = ~new_n734_ | ~rx_bit_cnt_0;
  assign rx_valid_D = ~new_n736_ & ~new_n735_;
  assign new_n740_ = new_n684_ ^ new_n745_;
  assign new_n737_ = ~new_n744_;
  assign new_n739_ = ~new_n738_ | ~new_n737_;
  assign new_n742_ = ~new_n740_ & ~new_n739_;
  assign new_n741_ = ~new_n606_ & ~re_i;
  assign new_n743_ = ~new_n742_ & ~new_n741_;
  assign rx_fifo_gb_Q = ~new_n743_ & ~new_n1166_;
  assign new_n747_ = ~new_n1158_ & ~new_n744_;
  assign new_n746_ = ~new_n745_;
  assign rx_fifo_wp_0_Q = new_n747_ ^ new_n746_;
  assign new_n749_ = ~new_n580_;
  assign new_n753_ = ~new_n749_ | ~new_n748_;
  assign new_n752_ = ~new_n595_ | ~new_n827_;
  assign rx_fifo_wp_1_Q = ~new_n753_ | ~new_n581_;
  assign new_n755_ = ~new_n754_;
  assign tx_fifo_wp_0_Q = new_n755_ ^ we_i;
  assign new_n1108_ = ~new_n756_ & ~new_n787_;
  assign new_n782_ = ~tx_bit_cnt_0;
  assign new_n757_ = ~new_n756_ & ~tx_bit_cnt_0;
  assign new_n769_ = ~new_n756_ | ~rst;
  assign new_n760_ = ~tx_bit_cnt_1;
  assign new_n761_ = ~new_n760_ | ~tx_bit_cnt_0;
  assign new_n801_ = ~shift_en;
  assign new_n762_ = ~tx_bit_cnt_0 | ~sio_ce;
  assign new_n764_ = ~new_n801_ & ~new_n762_;
  assign new_n763_ = ~new_n1102_ | ~rst;
  assign new_n773_ = ~new_n764_ & ~new_n763_;
  assign new_n776_ = ~tx_bit_cnt_0 | ~tx_bit_cnt_1;
  assign new_n767_ = ~new_n776_ & ~tx_bit_cnt_2;
  assign new_n775_ = ~tx_bit_cnt_2;
  assign new_n766_ = ~new_n775_ & ~tx_bit_cnt_1;
  assign new_n768_ = ~new_n767_ & ~new_n766_;
  assign new_n770_ = ~new_n773_ | ~tx_bit_cnt_2;
  assign tx_bit_cnt_2_Q = ~new_n610_ | ~new_n770_;
  assign new_n771_ = ~tx_bit_cnt_2 | ~tx_bit_cnt_1;
  assign new_n772_ = ~new_n756_ | ~new_n771_;
  assign new_n774_ = ~new_n772_ | ~tx_bit_cnt_3;
  assign new_n780_ = new_n774_ | new_n773_;
  assign new_n777_ = ~new_n776_ & ~new_n775_;
  assign new_n778_ = ~new_n756_ | ~new_n777_;
  assign new_n783_ = ~tx_bit_cnt_3;
  assign new_n779_ = ~new_n778_ | ~new_n783_;
  assign new_n781_ = ~new_n780_ | ~new_n779_;
  assign tx_bit_cnt_3_Q = ~new_n781_ | ~rst;
  assign new_n785_ = ~new_n783_ & ~new_n782_;
  assign new_n784_ = ~tx_bit_cnt_2 & ~tx_bit_cnt_1;
  assign shift_en_Q = ~new_n785_ | ~new_n784_;
  assign new_n803_ = ~tx_fifo_rp_0;
  assign new_n788_ = ~new_n786_;
  assign new_n791_ = ~new_n788_ | ~new_n787_;
  assign new_n789_ = ~tx_fifo_rp_1;
  assign new_n790_ = ~new_n586_ | ~new_n789_;
  assign new_n792_ = ~new_n791_ | ~new_n790_;
  assign tx_fifo_rp_1_Q = ~new_n792_ | ~new_n1178_;
  assign new_n793_ = ~tx_fifo_gb;
  assign new_n796_ = ~new_n794_ | ~new_n793_;
  assign new_n798_ = ~txf_empty_r & ~sio_ce;
  assign new_n1112_ = ~new_n801_;
  assign load_Q = ~new_n802_ & ~txf_empty_r;
  assign tx_fifo_rp_0_Q = new_n803_ ^ new_n586_;
  assign new_n804_ = ~rx_sio_ce;
  assign new_n821_ = ~new_n805_ & ~new_n804_;
  assign new_n807_ = ~new_n821_ | ~rxd_r_Q;
  assign new_n820_ = ~new_n821_;
  assign new_n806_ = ~new_n820_ | ~rxr_9;
  assign rxr_9_Q = ~new_n807_ | ~new_n806_;
  assign new_n809_ = ~new_n820_ | ~rxr_8;
  assign new_n808_ = ~new_n821_ | ~rxr_9;
  assign rxr_8_Q = ~new_n809_ | ~new_n808_;
  assign new_n811_ = ~new_n820_ | ~rxr_7;
  assign new_n810_ = ~new_n821_ | ~rxr_8;
  assign rxr_7_Q = ~new_n811_ | ~new_n810_;
  assign new_n813_ = ~new_n820_ | ~rxr_6;
  assign new_n812_ = ~new_n821_ | ~rxr_7;
  assign rxr_6_Q = ~new_n813_ | ~new_n812_;
  assign new_n815_ = ~new_n820_ | ~rxr_5;
  assign new_n814_ = ~new_n821_ | ~rxr_6;
  assign rxr_5_Q = ~new_n815_ | ~new_n814_;
  assign new_n817_ = ~new_n820_ | ~rxr_4;
  assign new_n816_ = ~new_n821_ | ~rxr_5;
  assign rxr_4_Q = ~new_n817_ | ~new_n816_;
  assign new_n819_ = ~new_n820_ | ~rxr_3;
  assign new_n818_ = ~new_n821_ | ~rxr_4;
  assign rxr_3_Q = ~new_n819_ | ~new_n818_;
  assign new_n823_ = ~new_n820_ | ~rxr_2;
  assign new_n822_ = ~new_n821_ | ~rxr_3;
  assign rxr_2_Q = ~new_n823_ | ~new_n822_;
  assign new_n826_ = ~new_n583_ | ~rx_fifo_mem_0;
  assign new_n825_ = ~new_n824_ | ~rxr_2;
  assign rx_fifo_mem_0_Q = ~new_n826_ | ~new_n825_;
  assign new_n915_ = ~new_n828_ | ~new_n827_;
  assign new_n829_ = ~rx_fifo_mem_24;
  assign new_n832_ = ~new_n915_ & ~new_n829_;
  assign new_n830_ = ~rx_fifo_mem_8;
  assign new_n831_ = ~new_n917_ & ~new_n830_;
  assign new_n838_ = ~new_n832_ & ~new_n831_;
  assign new_n836_ = ~new_n921_ & ~new_n587_;
  assign new_n923_ = ~rx_fifo_rp_0 | ~rx_fifo_rp_1;
  assign new_n834_ = ~rx_fifo_mem_0;
  assign new_n835_ = ~new_n923_ & ~new_n834_;
  assign new_n837_ = ~new_n836_ & ~new_n835_;
  assign dout_o_0_ = ~new_n838_ | ~new_n837_;
  assign new_n840_ = ~new_n582_ | ~rx_fifo_mem_17;
  assign new_n839_ = ~new_n911_ | ~rxr_3;
  assign rx_fifo_mem_17_Q = ~new_n840_ | ~new_n839_;
  assign new_n841_ = ~rx_fifo_mem_25;
  assign new_n844_ = ~new_n915_ & ~new_n841_;
  assign new_n842_ = ~rx_fifo_mem_9;
  assign new_n843_ = ~new_n917_ & ~new_n842_;
  assign new_n850_ = ~new_n844_ & ~new_n843_;
  assign new_n845_ = ~rx_fifo_mem_17;
  assign new_n848_ = ~new_n921_ & ~new_n845_;
  assign new_n846_ = ~rx_fifo_mem_1;
  assign new_n847_ = ~new_n923_ & ~new_n846_;
  assign new_n849_ = ~new_n848_ & ~new_n847_;
  assign dout_o_1_ = ~new_n850_ | ~new_n849_;
  assign new_n852_ = ~new_n582_ | ~rx_fifo_mem_18;
  assign new_n851_ = ~new_n911_ | ~rxr_4;
  assign rx_fifo_mem_18_Q = ~new_n852_ | ~new_n851_;
  assign new_n853_ = ~rx_fifo_mem_26;
  assign new_n856_ = ~new_n915_ & ~new_n853_;
  assign new_n854_ = ~rx_fifo_mem_10;
  assign new_n855_ = ~new_n917_ & ~new_n854_;
  assign new_n862_ = ~new_n856_ & ~new_n855_;
  assign new_n857_ = ~rx_fifo_mem_18;
  assign new_n860_ = ~new_n921_ & ~new_n857_;
  assign new_n858_ = ~rx_fifo_mem_2;
  assign new_n859_ = ~new_n923_ & ~new_n858_;
  assign new_n861_ = ~new_n860_ & ~new_n859_;
  assign dout_o_2_ = ~new_n862_ | ~new_n861_;
  assign new_n864_ = ~new_n581_ | ~rx_fifo_mem_19;
  assign new_n863_ = ~new_n911_ | ~rxr_5;
  assign rx_fifo_mem_19_Q = ~new_n864_ | ~new_n863_;
  assign new_n865_ = ~rx_fifo_mem_27;
  assign new_n868_ = ~new_n915_ & ~new_n865_;
  assign new_n866_ = ~rx_fifo_mem_11;
  assign new_n867_ = ~new_n917_ & ~new_n866_;
  assign new_n874_ = ~new_n868_ & ~new_n867_;
  assign new_n869_ = ~rx_fifo_mem_19;
  assign new_n872_ = ~new_n921_ & ~new_n869_;
  assign new_n870_ = ~rx_fifo_mem_3;
  assign new_n871_ = ~new_n923_ & ~new_n870_;
  assign new_n873_ = ~new_n872_ & ~new_n871_;
  assign dout_o_3_ = ~new_n874_ | ~new_n873_;
  assign new_n876_ = ~new_n582_ | ~rx_fifo_mem_20;
  assign new_n875_ = ~new_n911_ | ~rxr_6;
  assign rx_fifo_mem_20_Q = ~new_n876_ | ~new_n875_;
  assign new_n877_ = ~rx_fifo_mem_28;
  assign new_n880_ = ~new_n915_ & ~new_n877_;
  assign new_n878_ = ~rx_fifo_mem_12;
  assign new_n879_ = ~new_n917_ & ~new_n878_;
  assign new_n886_ = ~new_n880_ & ~new_n879_;
  assign new_n881_ = ~rx_fifo_mem_20;
  assign new_n884_ = ~new_n921_ & ~new_n881_;
  assign new_n882_ = ~rx_fifo_mem_4;
  assign new_n883_ = ~new_n923_ & ~new_n882_;
  assign new_n885_ = ~new_n884_ & ~new_n883_;
  assign dout_o_4_ = ~new_n886_ | ~new_n885_;
  assign new_n888_ = ~new_n581_ | ~rx_fifo_mem_21;
  assign new_n887_ = ~new_n911_ | ~rxr_7;
  assign rx_fifo_mem_21_Q = ~new_n888_ | ~new_n887_;
  assign new_n889_ = ~rx_fifo_mem_29;
  assign new_n892_ = ~new_n915_ & ~new_n889_;
  assign new_n890_ = ~rx_fifo_mem_13;
  assign new_n891_ = ~new_n917_ & ~new_n890_;
  assign new_n898_ = ~new_n892_ & ~new_n891_;
  assign new_n893_ = ~rx_fifo_mem_21;
  assign new_n896_ = ~new_n921_ & ~new_n893_;
  assign new_n894_ = ~rx_fifo_mem_5;
  assign new_n895_ = ~new_n923_ & ~new_n894_;
  assign new_n897_ = ~new_n896_ & ~new_n895_;
  assign dout_o_5_ = ~new_n898_ | ~new_n897_;
  assign new_n900_ = ~new_n589_ | ~rx_fifo_mem_22;
  assign new_n899_ = ~new_n911_ | ~rxr_8;
  assign rx_fifo_mem_22_Q = ~new_n900_ | ~new_n899_;
  assign new_n901_ = ~rx_fifo_mem_30;
  assign new_n904_ = ~new_n915_ & ~new_n901_;
  assign new_n902_ = ~rx_fifo_mem_14;
  assign new_n903_ = ~new_n917_ & ~new_n902_;
  assign new_n910_ = ~new_n904_ & ~new_n903_;
  assign new_n905_ = ~rx_fifo_mem_22;
  assign new_n908_ = ~new_n921_ & ~new_n905_;
  assign new_n906_ = ~rx_fifo_mem_6;
  assign new_n907_ = ~new_n923_ & ~new_n906_;
  assign new_n909_ = ~new_n908_ & ~new_n907_;
  assign dout_o_6_ = ~new_n910_ | ~new_n909_;
  assign new_n913_ = ~new_n589_ | ~rx_fifo_mem_23;
  assign new_n912_ = ~new_n911_ | ~rxr_9;
  assign rx_fifo_mem_23_Q = ~new_n913_ | ~new_n912_;
  assign new_n914_ = ~rx_fifo_mem_31;
  assign new_n919_ = ~new_n915_ & ~new_n914_;
  assign new_n916_ = ~rx_fifo_mem_15;
  assign new_n918_ = ~new_n917_ & ~new_n916_;
  assign new_n927_ = ~new_n919_ & ~new_n918_;
  assign new_n920_ = ~rx_fifo_mem_23;
  assign new_n925_ = ~new_n921_ & ~new_n920_;
  assign new_n922_ = ~rx_fifo_mem_7;
  assign new_n924_ = ~new_n923_ & ~new_n922_;
  assign new_n926_ = ~new_n925_ & ~new_n924_;
  assign dout_o_7_ = ~new_n927_ | ~new_n926_;
  assign new_n928_ = ~shift_en_r | ~new_n1113_;
  assign shift_en_r_Q = ~new_n931_ & ~new_n1166_;
  assign new_n936_ = ~new_n934_ | ~tx_fifo_mem_0;
  assign new_n935_ = ~new_n997_ | ~din_i_0_;
  assign tx_fifo_mem_0_Q = ~new_n936_ | ~new_n935_;
  assign new_n946_ = ~tx_fifo_wp_0 & ~new_n937_;
  assign new_n1001_ = ~new_n939_;
  assign new_n941_ = ~new_n1001_ | ~din_i_0_;
  assign new_n940_ = ~new_n939_ | ~tx_fifo_mem_8;
  assign tx_fifo_mem_8_Q = ~new_n941_ | ~new_n940_;
  assign new_n944_ = ~new_n942_ | ~tx_fifo_mem_16;
  assign new_n1005_ = ~new_n942_;
  assign new_n943_ = ~new_n1005_ | ~din_i_0_;
  assign tx_fifo_mem_16_Q = ~new_n944_ | ~new_n943_;
  assign new_n1009_ = new_n946_ & new_n945_;
  assign new_n948_ = ~new_n1009_ | ~din_i_0_;
  assign new_n1010_ = ~new_n946_ | ~new_n945_;
  assign new_n947_ = ~new_n1010_ | ~tx_fifo_mem_24;
  assign tx_fifo_mem_24_Q = ~new_n948_ | ~new_n947_;
  assign new_n950_ = ~new_n997_ | ~din_i_1_;
  assign new_n949_ = ~new_n934_ | ~tx_fifo_mem_1;
  assign tx_fifo_mem_1_Q = ~new_n949_ | ~new_n950_;
  assign new_n952_ = ~new_n1001_ | ~din_i_1_;
  assign new_n951_ = ~new_n939_ | ~tx_fifo_mem_9;
  assign tx_fifo_mem_9_Q = ~new_n951_ | ~new_n952_;
  assign new_n954_ = ~new_n1005_ | ~din_i_1_;
  assign new_n953_ = ~new_n942_ | ~tx_fifo_mem_17;
  assign tx_fifo_mem_17_Q = ~new_n953_ | ~new_n954_;
  assign new_n956_ = ~new_n1009_ | ~din_i_1_;
  assign new_n955_ = ~new_n1010_ | ~tx_fifo_mem_25;
  assign tx_fifo_mem_25_Q = ~new_n956_ | ~new_n955_;
  assign new_n958_ = ~new_n997_ | ~din_i_2_;
  assign new_n957_ = ~new_n934_ | ~tx_fifo_mem_2;
  assign tx_fifo_mem_2_Q = ~new_n957_ | ~new_n958_;
  assign new_n960_ = ~new_n1001_ | ~din_i_2_;
  assign new_n959_ = ~new_n939_ | ~tx_fifo_mem_10;
  assign tx_fifo_mem_10_Q = ~new_n959_ | ~new_n960_;
  assign new_n962_ = ~new_n1005_ | ~din_i_2_;
  assign new_n961_ = ~new_n942_ | ~tx_fifo_mem_18;
  assign tx_fifo_mem_18_Q = ~new_n961_ | ~new_n962_;
  assign new_n964_ = ~new_n1009_ | ~din_i_2_;
  assign new_n963_ = ~new_n1010_ | ~tx_fifo_mem_26;
  assign tx_fifo_mem_26_Q = ~new_n964_ | ~new_n963_;
  assign new_n966_ = ~new_n997_ | ~din_i_3_;
  assign new_n965_ = ~new_n934_ | ~tx_fifo_mem_3;
  assign tx_fifo_mem_3_Q = ~new_n965_ | ~new_n966_;
  assign new_n968_ = ~new_n1001_ | ~din_i_3_;
  assign new_n967_ = ~new_n939_ | ~tx_fifo_mem_11;
  assign tx_fifo_mem_11_Q = ~new_n967_ | ~new_n968_;
  assign new_n970_ = ~new_n1005_ | ~din_i_3_;
  assign new_n969_ = ~new_n942_ | ~tx_fifo_mem_19;
  assign tx_fifo_mem_19_Q = ~new_n969_ | ~new_n970_;
  assign new_n972_ = ~new_n1009_ | ~din_i_3_;
  assign new_n971_ = ~new_n1010_ | ~tx_fifo_mem_27;
  assign tx_fifo_mem_27_Q = ~new_n972_ | ~new_n971_;
  assign new_n974_ = ~new_n997_ | ~din_i_4_;
  assign new_n973_ = ~new_n934_ | ~tx_fifo_mem_4;
  assign tx_fifo_mem_4_Q = ~new_n973_ | ~new_n974_;
  assign new_n976_ = ~new_n1001_ | ~din_i_4_;
  assign new_n975_ = ~new_n939_ | ~tx_fifo_mem_12;
  assign tx_fifo_mem_12_Q = ~new_n975_ | ~new_n976_;
  assign new_n978_ = ~new_n1005_ | ~din_i_4_;
  assign new_n977_ = ~new_n942_ | ~tx_fifo_mem_20;
  assign tx_fifo_mem_20_Q = ~new_n977_ | ~new_n978_;
  assign new_n980_ = ~new_n1009_ | ~din_i_4_;
  assign new_n979_ = ~new_n1010_ | ~tx_fifo_mem_28;
  assign tx_fifo_mem_28_Q = ~new_n980_ | ~new_n979_;
  assign new_n982_ = ~new_n997_ | ~din_i_5_;
  assign new_n981_ = ~new_n934_ | ~tx_fifo_mem_5;
  assign tx_fifo_mem_5_Q = ~new_n981_ | ~new_n982_;
  assign new_n984_ = ~new_n1001_ | ~din_i_5_;
  assign new_n983_ = ~new_n939_ | ~tx_fifo_mem_13;
  assign tx_fifo_mem_13_Q = ~new_n983_ | ~new_n984_;
  assign new_n986_ = ~new_n1005_ | ~din_i_5_;
  assign new_n985_ = ~new_n942_ | ~tx_fifo_mem_21;
  assign tx_fifo_mem_21_Q = ~new_n985_ | ~new_n986_;
  assign new_n988_ = ~new_n1009_ | ~din_i_5_;
  assign new_n987_ = ~new_n1010_ | ~tx_fifo_mem_29;
  assign tx_fifo_mem_29_Q = ~new_n988_ | ~new_n987_;
  assign new_n990_ = ~new_n997_ | ~din_i_6_;
  assign new_n989_ = ~new_n934_ | ~tx_fifo_mem_6;
  assign tx_fifo_mem_6_Q = ~new_n989_ | ~new_n990_;
  assign new_n992_ = ~new_n1001_ | ~din_i_6_;
  assign new_n991_ = ~new_n939_ | ~tx_fifo_mem_14;
  assign tx_fifo_mem_14_Q = ~new_n991_ | ~new_n992_;
  assign new_n994_ = ~new_n1005_ | ~din_i_6_;
  assign new_n993_ = ~new_n942_ | ~tx_fifo_mem_22;
  assign tx_fifo_mem_22_Q = ~new_n993_ | ~new_n994_;
  assign new_n996_ = ~new_n1009_ | ~din_i_6_;
  assign new_n995_ = ~new_n1010_ | ~tx_fifo_mem_30;
  assign tx_fifo_mem_30_Q = ~new_n996_ | ~new_n995_;
  assign new_n1000_ = ~new_n997_ | ~din_i_7_;
  assign new_n999_ = ~new_n934_ | ~tx_fifo_mem_7;
  assign tx_fifo_mem_7_Q = ~new_n1000_ | ~new_n999_;
  assign new_n1004_ = ~new_n1001_ | ~din_i_7_;
  assign new_n1003_ = ~new_n939_ | ~tx_fifo_mem_15;
  assign tx_fifo_mem_15_Q = ~new_n1003_ | ~new_n1004_;
  assign new_n1008_ = ~new_n1005_ | ~din_i_7_;
  assign new_n1007_ = ~new_n942_ | ~tx_fifo_mem_23;
  assign tx_fifo_mem_23_Q = ~new_n1008_ | ~new_n1007_;
  assign new_n1012_ = ~new_n1009_ | ~din_i_7_;
  assign new_n1011_ = ~new_n1010_ | ~tx_fifo_mem_31;
  assign tx_fifo_mem_31_Q = ~new_n1012_ | ~new_n1011_;
  assign new_n1013_ = ~hold_reg_9;
  assign hold_reg_9_Q = ~new_n584_ | ~new_n1013_;
  assign new_n1016_ = ~new_n1160_ | ~tx_fifo_mem_15;
  assign new_n1015_ = ~new_n1184_ | ~tx_fifo_mem_7;
  assign new_n1021_ = ~new_n1016_ | ~new_n1015_;
  assign new_n1019_ = ~new_n786_ | ~tx_fifo_mem_23;
  assign new_n1097_ = ~tx_fifo_rp_1 & ~tx_fifo_rp_0;
  assign new_n1018_ = ~new_n1097_ | ~tx_fifo_mem_31;
  assign new_n1020_ = ~new_n1019_ | ~new_n1018_;
  assign new_n1022_ = ~new_n1020_ & ~new_n1021_;
  assign new_n1026_ = ~new_n1022_ & ~new_n586_;
  assign new_n1024_ = ~new_n1108_ | ~hold_reg_8;
  assign new_n1023_ = ~new_n756_ | ~hold_reg_9;
  assign new_n1025_ = ~new_n1024_ | ~new_n1023_;
  assign new_n1028_ = ~new_n1160_ | ~tx_fifo_mem_14;
  assign new_n1027_ = ~new_n609_ | ~tx_fifo_mem_6;
  assign new_n1032_ = ~new_n1028_ | ~new_n1027_;
  assign new_n1030_ = ~new_n786_ | ~tx_fifo_mem_22;
  assign new_n1029_ = ~new_n1097_ | ~tx_fifo_mem_30;
  assign new_n1031_ = ~new_n1030_ | ~new_n1029_;
  assign new_n1033_ = ~new_n1031_ & ~new_n1032_;
  assign new_n1037_ = ~new_n1033_ & ~new_n586_;
  assign new_n1035_ = ~new_n584_ | ~hold_reg_7;
  assign new_n1034_ = ~new_n756_ | ~hold_reg_8;
  assign new_n1036_ = ~new_n1035_ | ~new_n1034_;
  assign new_n1039_ = ~new_n1160_ | ~tx_fifo_mem_13;
  assign new_n1038_ = ~new_n1184_ | ~tx_fifo_mem_5;
  assign new_n1043_ = ~new_n1039_ | ~new_n1038_;
  assign new_n1041_ = ~new_n786_ | ~tx_fifo_mem_21;
  assign new_n1040_ = ~new_n1097_ | ~tx_fifo_mem_29;
  assign new_n1042_ = ~new_n1041_ | ~new_n1040_;
  assign new_n1044_ = ~new_n1042_ & ~new_n1043_;
  assign new_n1048_ = ~new_n1044_ & ~new_n586_;
  assign new_n1046_ = ~new_n585_ | ~hold_reg_6;
  assign new_n1045_ = ~new_n756_ | ~hold_reg_7;
  assign new_n1047_ = ~new_n1046_ | ~new_n1045_;
  assign new_n1050_ = ~new_n1160_ | ~tx_fifo_mem_12;
  assign new_n1049_ = ~new_n609_ | ~tx_fifo_mem_4;
  assign new_n1054_ = ~new_n1050_ | ~new_n1049_;
  assign new_n1052_ = ~new_n786_ | ~tx_fifo_mem_20;
  assign new_n1051_ = ~new_n1097_ | ~tx_fifo_mem_28;
  assign new_n1053_ = ~new_n1052_ | ~new_n1051_;
  assign new_n1055_ = ~new_n1053_ & ~new_n1054_;
  assign new_n1059_ = ~new_n1055_ & ~new_n586_;
  assign new_n1057_ = ~new_n1108_ | ~hold_reg_5;
  assign new_n1056_ = ~new_n756_ | ~hold_reg_6;
  assign new_n1058_ = ~new_n1057_ | ~new_n1056_;
  assign new_n1061_ = ~new_n1160_ | ~tx_fifo_mem_11;
  assign new_n1060_ = ~new_n1184_ | ~tx_fifo_mem_3;
  assign new_n1065_ = ~new_n1061_ | ~new_n1060_;
  assign new_n1063_ = ~new_n786_ | ~tx_fifo_mem_19;
  assign new_n1062_ = ~new_n1097_ | ~tx_fifo_mem_27;
  assign new_n1064_ = ~new_n1063_ | ~new_n1062_;
  assign new_n1066_ = ~new_n1064_ & ~new_n1065_;
  assign new_n1068_ = ~new_n584_ | ~hold_reg_4;
  assign new_n1067_ = ~new_n756_ | ~hold_reg_5;
  assign new_n1072_ = ~new_n1160_ | ~tx_fifo_mem_10;
  assign new_n1071_ = ~new_n609_ | ~tx_fifo_mem_2;
  assign new_n1076_ = ~new_n1072_ | ~new_n1071_;
  assign new_n1074_ = ~new_n786_ | ~tx_fifo_mem_18;
  assign new_n1073_ = ~new_n1097_ | ~tx_fifo_mem_26;
  assign new_n1075_ = ~new_n1074_ | ~new_n1073_;
  assign new_n1077_ = ~new_n1075_ & ~new_n1076_;
  assign new_n1079_ = ~new_n585_ | ~hold_reg_3;
  assign new_n1078_ = ~new_n756_ | ~hold_reg_4;
  assign new_n1083_ = ~new_n1160_ | ~tx_fifo_mem_9;
  assign new_n1082_ = ~new_n1184_ | ~tx_fifo_mem_1;
  assign new_n1087_ = ~new_n1083_ | ~new_n1082_;
  assign new_n1085_ = ~new_n786_ | ~tx_fifo_mem_17;
  assign new_n1084_ = ~new_n1097_ | ~tx_fifo_mem_25;
  assign new_n1086_ = ~new_n1085_ | ~new_n1084_;
  assign new_n1088_ = ~new_n1086_ & ~new_n1087_;
  assign new_n1090_ = ~new_n1108_ | ~hold_reg_2;
  assign new_n1089_ = ~new_n756_ | ~hold_reg_3;
  assign new_n1095_ = ~new_n1160_ | ~tx_fifo_mem_8;
  assign new_n1094_ = ~new_n609_ | ~tx_fifo_mem_0;
  assign new_n1101_ = ~new_n1095_ | ~new_n1094_;
  assign new_n1099_ = ~new_n786_ | ~tx_fifo_mem_16;
  assign new_n1098_ = ~new_n1097_ | ~tx_fifo_mem_24;
  assign new_n1100_ = ~new_n1099_ | ~new_n1098_;
  assign new_n1105_ = ~new_n584_ | ~hold_reg_1;
  assign new_n1104_ = ~new_n756_ | ~hold_reg_2;
  assign new_n1111_ = ~new_n1108_ | ~hold_reg_0;
  assign new_n1110_ = ~new_n756_ | ~hold_reg_1;
  assign hold_reg_0_Q = ~new_n1111_ | ~new_n1110_;
  assign new_n1115_ = shift_en_r | new_n1112_;
  assign new_n1114_ = ~hold_reg_0 & ~new_n1113_;
  assign new_n1117_ = ~new_n1115_ | ~new_n1114_;
  assign new_n1116_ = txd_o | sio_ce;
  assign new_n1118_ = ~new_n1117_ | ~new_n1116_;
  assign txd_o_D = ~new_n1118_ | ~rst;
  assign new_n697_ = ~sio_ce_x4;
  assign new_n643_ = ~new_n744_ & ~new_n642_;
  assign new_n756_ = ~new_n929_ & ~load;
  assign new_n727_ = ~new_n709_;
  assign new_n937_ = ~we_i;
  assign new_n929_ = ~shift_en | ~sio_ce;
  assign new_n1160_ = ~new_n1014_;
  assign new_n1177_ = new_n1105_ & new_n1104_;
  assign new_n1183_ = new_n1090_ & new_n1089_;
  assign new_n1175_ = new_n1079_ & new_n1078_;
  assign new_n1181_ = new_n1068_ & new_n1067_;
  assign new_n709_ = ~new_n707_ & ~new_n706_;
  assign new_n707_ = ~new_n723_ | ~rst;
  assign new_n706_ = ~new_n705_ & ~rxd_r_Q;
  assign new_n945_ = ~new_n938_;
  assign new_n1179_ = ~we_i | ~rst;
  assign new_n1166_ = ~rst;
  assign new_n603_ = ~new_n600_ & ~new_n604_;
  assign new_n1113_ = ~sio_ce;
  assign tx_bit_cnt_1_Q = new_n1161_ | new_n1162_;
  assign new_n1161_ = ~new_n769_ & ~new_n761_;
  assign new_n1162_ = new_n773_ & tx_bit_cnt_1;
  assign new_n1163_ = ~new_n585_ & ~new_n1165_;
  assign tx_bit_cnt_0_Q = ~new_n1163_ & ~new_n1164_;
  assign new_n1164_ = rst & new_n757_;
  assign new_n1165_ = new_n782_ | new_n1166_;
  assign new_n1167_ = new_n1187_ | new_n796_;
  assign txf_empty_r_Q = ~new_n1167_ | ~new_n1168_;
  assign new_n1168_ = ~new_n1166_ & ~new_n1185_;
  assign new_n1169_ = ~new_n717_ | ~new_n1171_;
  assign rx_bit_cnt_1_Q = new_n1169_ & new_n1170_;
  assign new_n1170_ = new_n1166_ | new_n713_;
  assign new_n1171_ = rx_bit_cnt_1 & rst;
  assign new_n931_ = new_n929_ & new_n928_;
  assign new_n934_ = new_n611_ | tx_fifo_wp_1;
  assign new_n932_ = ~new_n611_;
  assign new_n1176_ = ~new_n1173_ | ~new_n787_;
  assign new_n1173_ = new_n1100_ | new_n1101_;
  assign new_n787_ = ~new_n1102_;
  assign hold_reg_3_Q = ~new_n1174_ | ~new_n1175_;
  assign new_n1174_ = new_n1077_ | new_n586_;
  assign hold_reg_1_Q = ~new_n1176_ | ~new_n1177_;
  assign new_n1178_ = ~new_n1160_;
  assign new_n1190_ = ~new_n794_ & ~new_n1179_;
  assign hold_reg_4_Q = ~new_n1180_ | ~new_n1181_;
  assign new_n1180_ = new_n1066_ | new_n586_;
  assign hold_reg_2_Q = ~new_n1182_ | ~new_n1183_;
  assign new_n1182_ = new_n1088_ | new_n586_;
  assign new_n1184_ = tx_fifo_rp_1 & tx_fifo_rp_0;
  assign new_n1185_ = new_n1186_ & new_n1113_;
  assign new_n1186_ = ~new_n798_;
  assign new_n1187_ = new_n795_ | new_n798_;
  assign new_n997_ = ~new_n934_;
  assign new_n1191_ = new_n580_ & new_n748_;
  assign new_n1188_ = ~new_n632_ | ~new_n1190_;
  assign tx_fifo_gb_Q = ~new_n1188_ | ~new_n1189_;
  assign new_n1189_ = new_n1166_ | new_n633_;
  assign new_n748_ = ~new_n751_;
  assign new_n824_ = ~new_n616_;
endmodule


