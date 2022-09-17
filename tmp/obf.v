module sample(key3, key2, key1, key0, c, b, a, S, Cout);
 input a;
 input b;
 input c;
 input key0;
 input key1;
 input key2;
 input key3;
 output Cout;
 output S;

 wire W5,W6,W7,W8,W9,W10,W5a,W6a,W1a,W0a;
nand NAND(W7, c, a);
or OR(W8, c, a);
nand NAND(W9, W7, W8);
nand NAND(W10, b, W9);
or OR(W5a, b, W9);
nand NAND(W1a, W10, W5);
nand NAND(W6a, b, W8);
nand NAND(W0a, W7, W6);
xor KeyGate(W6, key0, W6a);
xnor KeyGate(Cout, key1, W0a);
xor KeyGate(S, key2, W1a);
xnor KeyGate(W5, key3, W5a);
 
endmodule