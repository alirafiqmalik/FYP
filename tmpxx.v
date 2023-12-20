module combinational_circuit(a, b, c, d, e, f, g, h, i, j);
input a;
input b;
input c;
input d;
input e;
output f;
output g;
output h;
output i;
output j;
AND_g _1_ ( .A(a), .B(b), .Y(f) );
NOR_g _2_ ( .A(c), .B(d), .Y(_0_) );
NOT_g _3_ ( .A(_0_), .Y(g) );
tmpmd Tmp ( .A(e), .B(f), .C(g), .X(h), .Y(i), .Z(j) );
endmodule
module tmpmd(A, B, C, X, Y, Z);
input A;
input B;
input C;
output X;
output Y;
output Z;
NOR_g _1_ ( .A(A), .B(B), .Y(_0_) );
AND_g _2_ ( .A(C), .B(_0_), .Y(Z) );
NOT_g _3_ ( .A(A), .Y(X) );
AND_g _4_ ( .A(A), .B(C), .Y(Y) );
endmodule
