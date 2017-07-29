NAME ?= dff

PCF = $(NAME).pcf

DEVICE = 1k
QUIET = -q

$(NAME).bin: $(NAME).v $(PCF)
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	arachne-pnr $(QUIET) -d $(DEVICE) -o $(NAME).txt -p $(PCF) $(NAME).blif
	icepack $(NAME).txt $(NAME).bin

upload: $(NAME).bin
	iceprog $(NAME).bin

upload_mac: $(NAME).bin
	sudo kextunload -b com.apple.driver.AppleUSBFTDI
	iceprog $(NAME).bin
	sudo kextload -b com.apple.driver.AppleUSBFTDI

clean:
	rm -f *.bin *.txt *.blif *.rpt

.PHONY: all explain install clean
