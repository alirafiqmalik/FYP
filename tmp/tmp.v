module sample (a,b,c,S,Cout);
  input a,b,c;
  output S,Cout;


always @({a,b,c}) begin
	case ({a,b,c})
  3'b000:{Cout,S}=2'b00;
	3'b001:{Cout,S}=2'b01;
	3'b010:{Cout,S}=2'b01;
	3'b011:{Cout,S}=2'b10;
	3'b100:{Cout,S}=2'b01;
	3'b101:{Cout,S}=2'b10;
	3'b110:{Cout,S}=2'b10;
	3'b111:{Cout,S}=2'b11;
  endcase
end

endmodule
