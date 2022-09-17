module sample(a,b,c,key0,key1,key2,key3,Cout,S);
 input a;
 input b;
 input c;
 input key0;
 input key1;
 input key2;
 input key3;
 output Cout;
 output S;

 wire _00_;
 wire _01_;
 wire _02_;
 wire _03_;
 wire _04_;
 wire _05_;
 wire _06_;
 wire _07_;
 wire _08_;
 wire _09_;
 wire _10_;
 wire [1:0] _11_;
 wire [1:0] _12_;
 wire [1:0] _13_;

 NAND_g _14_ ( .A(c), .B(a), .Y(_07_) );
 OR_g _15_ ( .A(c), .B(a), .Y(_08_) );
 NAND_g _16_ ( .A(_07_), .B(_08_), .Y(_09_) );
 NAND_g _17_ ( .A(b), .B(_09_), .Y(_10_) );
 OR_g _18_ ( .A(b), .B(_09_), .Y(_05a_) );
 NAND_g _19_ ( .A(_10_), .B(_05_), .Y(_01a_) );
 NAND_g _20_ ( .A(b), .B(_08_), .Y(_06a_) );
 NAND_g _21_ ( .A(_07_), .B(_06_), .Y(_00a_) );

 XOR_g _433_ ( .A(key0), .B(_06a_), .Y(_06_) );
 XNOR_g _434_ ( .A(key1), .B(_00a_), .Y(Cout) );
 XOR_g _435_ ( .A(key2), .B(_01a_), .Y(S) );
 XNOR_g _436_ ( .A(key3), .B(_05a_), .Y(_05_) );

endmodule
