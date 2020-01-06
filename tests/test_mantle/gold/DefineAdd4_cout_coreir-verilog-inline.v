module Add4_cout (output COUT, input [3:0] I0, input [3:0] I1, output [3:0] O);
wire [4:0] coreir_add5_inst0_out;
assign coreir_add5_inst0_out = ({1'b0,I0[3],I0[2],I0[1],I0[0]}) + ({1'b0,I1[3],I1[2],I1[1],I1[0]});
assign COUT = coreir_add5_inst0_out[4];
assign O = {coreir_add5_inst0_out[3],coreir_add5_inst0_out[2],coreir_add5_inst0_out[1],coreir_add5_inst0_out[0]};
endmodule

