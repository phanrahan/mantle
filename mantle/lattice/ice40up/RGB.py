#    SB_RGBA_DRV RGB_DRIVER ( 
#      .RGBLEDEN (1'b1),
#      .RGB0PWM  (frequency_counter_i[25]&frequency_counter_i[24]),
#      .RGB1PWM  (frequency_counter_i[25]&~frequency_counter_i[24]),
#      .RGB2PWM  (~frequency_counter_i[25]&frequency_counter_i[24]),
#      .CURREN   (1'b1), 
#      .RGB0     (REDn),		//Actual Hardware connection
#      .RGB1     (GRNn),
#      .RGB2     (BLUn)
#    );
#    defparam RGB_DRIVER.RGB0_CURRENT = "0b000001";
#    defparam RGB_DRIVER.RGB1_CURRENT = "0b000001";
#    defparam RGB_DRIVER.RGB2_CURRENT = "0b000001";
