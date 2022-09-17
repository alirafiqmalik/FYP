module sample (c,b,a,S,Cout);
 input a;
 input b;
 input c;
 output Cout;
 output S;
 wire _05_,_06_,_07_,_08_,_09_,_10_;
nand NAND(_07_ ,c,a);
or OR(_08_,c,a);
nand NAND(_09_,_07_,_08_);
nand NAND(_10_,b,_09_);
or OR(_05_,b,_09_);
nand NAND(S,_10_,_05_);
nand NAND(_06_,b,_08_);
nand NAND(Cout,_07_,_06_);
endmodule