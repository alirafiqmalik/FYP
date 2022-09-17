module sample(a,b,c,key0,key1,key2,key3,Cout,S);
 input a;
 input b;
 input c;
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
 OR_g _18_ ( .A(b), .B(_09_), .Y(_05_) );
 NAND_g _19_ ( .A(_10_), .B(_05_), .Y(S) );
 NAND_g _20_ ( .A(b), .B(_08_), .Y(_06_) );
 NAND_g _21_ ( .A(_07_), .B(_06_), .Y(Cout) );

endmodule
