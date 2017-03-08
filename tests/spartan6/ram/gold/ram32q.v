module main (output [7:0] LED, input [7:0] SWITCH, input  CLKIN);
wire [1:0] inst0_DOA;
wire [1:0] inst0_DOB;
wire [1:0] inst0_DOC;
wire [1:0] inst0_DOD;
RAM32M #(.INIT_A(32'h55555555),
.INIT_C(32'hAAAAAAAA),
.INIT_B(32'hFFFFFFFF),
.INIT_D(32'h00000000)) inst0 (.ADDRA({SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .ADDRB({SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .ADDRC({SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .ADDRD({SWITCH[4],SWITCH[3],SWITCH[2],SWITCH[1],SWITCH[0]}), .DIA({1'b0,1'b0}), .DIB({1'b0,1'b0}), .DIC({1'b0,1'b0}), .DID({1'b0,1'b0}), .DOA(inst0_DOA), .DOB(inst0_DOB), .DOC(inst0_DOC), .DOD(inst0_DOD), .WE(1'b0), .WCLK(CLKIN));
assign LED = {inst0_DOD[1],inst0_DOD[0],inst0_DOC[1],inst0_DOC[0],inst0_DOB[1],inst0_DOB[0],inst0_DOA[1],inst0_DOA[0]};
endmodule

