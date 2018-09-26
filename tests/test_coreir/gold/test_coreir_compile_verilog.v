

module corebit_and (
  input in0,
  input in1,
  output out
);
  assign out = in0 & in1;

endmodule //corebit_and

module main (
  input [1:0] I,
  output  O
);
  //Wire declarations for instance 'inst0' (Module corebit_and)
  wire  inst0__in0;
  wire  inst0__in1;
  wire  inst0__out;
  corebit_and inst0(
    .in0(inst0__in0),
    .in1(inst0__in1),
    .out(inst0__out)
  );

  //All the connections
  assign inst0__in0 = I[0];
  assign inst0__in1 = I[1];
  assign O = inst0__out;

endmodule //main
