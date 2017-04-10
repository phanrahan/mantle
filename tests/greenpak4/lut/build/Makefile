NAME = lut2

DEVICE = SLG46620V
#PCF = $(NAME).pcf

QUIET = -q

all: $(NAME).txt

%.txt: %.json
	gp4pnr $(QUIET) -p $(DEVICE) $*.json -o $*.txt --unused-pull down --unused-drive 10k

%.json: %.v
	yosys $(QUIET) -p 'synth_greenpak4 -top main -part SLG46620V -json $*.json' $<

upload: $(NAME).txt
	gp4prog $<

clean:
	rm -f *.txt *.json 


.PRECIOUS: %.bin %.txt %.blif 

.PHONY: all explain install clean
