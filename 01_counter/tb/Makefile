SIM ?= verilator
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../rtl/counter.sv
COCOTB_TOPLEVEL = counter
COCOTB_TEST_MODULES = test_counter

ifeq ($(SIM),verilator)
EXTRA_ARGS += --trace --trace-fst --trace-structs
endif

include $(shell cocotb-config --makefiles)/Makefile.sim