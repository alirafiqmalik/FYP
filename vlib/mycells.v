module  BUF_g(A, Y);
input A;
output Y;
assign Y=A;
endmodule

 
module  NOT_g(A, Y);
input A;
output Y;
assign Y=~A;
endmodule

module AND_g(A, B, Y);
input A, B;
output Y;
assign Y=(A & B);
endmodule

module OR_g(A, B, Y);
input A, B;
output Y;
assign Y= (A | B);
endmodule

module NAND_g(A, B, Y);
input A, B;
output Y;
assign Y= ~(A & B);

endmodule

module NOR_g(A, B, Y);
input A, B;
output Y;
assign Y = ~(A | B);
endmodule


module DFFcell(C, D, Q);
input C, D;
output reg Q;
always @(posedge C)
	Q <= D;
endmodule


// library(demo) {
//   cell(BUF_g) {
//     area: 6;
//     pin(A) { direction: input; }
//     pin(Y) { direction: output;
//               function: "A"; }
//   }
//   cell(NOT_g) {
//     area: 3;
//     pin(A) { direction: input; }
//     pin(Y) { direction: output;
//               function: "A'"; }
//   }
//   cell(AND_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A*B)"; }
//   }

//   cell(OR_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A+B)"; }
//   }

//   cell(NAND_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A*B)'"; }
//   }
//   cell(NOR_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A+B)'"; }
//   }



//   cell(DFFcell) {
//     area: 18;
//     ff(IQ, IQN) { clocked_on: C;
//                   next_state: D; }
//     pin(C) { direction: input;
//                  clock: true; }
//     pin(D) { direction: input; }
//     pin(Q) { direction: output;
//               function: "IQ"; }
//   }
// }



//   cell(XOR_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A*B'+A'*B)"; }
//   }

//   cell(XNOR_g) {
//     area: 4;
//     pin(A) { direction: input; }
//     pin(B) { direction: input; }
//     pin(Y) { direction: output;
//              function: "(A*B'+A'*B)"; }
//   }