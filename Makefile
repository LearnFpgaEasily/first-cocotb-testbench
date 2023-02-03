export PYTHONPATH := $(PWD)/testbench:$(PYTHONPATH)

TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/src/dff.sv
TOPLEVEL = dff
MODULE = test_dff

include $(shell cocotb-config --makefiles)/Makefile.sim
