CC=gcc ${DBG} -Ofast ${TRACE} -Wall -Wpedantic

all: extract run

extract: extract.o

run: | extract
	./extract fpga-data.txt data-0.txt 0
	./extract fpga-data.txt data-1.txt 1
	./extract fpga-data.txt data-2.txt 2
	./extract fpga-data.txt data-3.txt 3
	./extract fpga-data.txt data-4.txt 4
	./extract fpga-data.txt data-5.txt 5
	./extract fpga-data.txt data-6.txt 6
	./extract fpga-data.txt data-7.txt 7
	./extract fpga-data.txt data-8.txt 8
	./extract fpga-data.txt data-9.txt 9
	./extract fpga-data.txt data-10.txt 10
	./extract fpga-data.txt data-11.txt 11
	./extract fpga-data.txt data-12.txt 12
	./extract fpga-data.txt data-13.txt 13
	./extract fpga-data.txt data-14.txt 14
	./extract fpga-data.txt data-15.txt 15

.PHONY: all run
