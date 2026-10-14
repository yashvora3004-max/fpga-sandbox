import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


@cocotb.test()
async def counts_up_and_wraps(dut):
    """Reset clears the count; with en high it adds 1 per clock and wraps at 255."""
    Clock(dut.clk, 10, unit="ns").start(start_high=False)  # 100 MHz clock

    dut.rst.value = 1
    dut.en.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    assert dut.count.value == 0, f"count should be 0 in reset, got {dut.count.value}"

    dut.rst.value = 0
    dut.en.value = 1
    for cycle in range(1, 301):  # 300 clocks crosses the 255 -> 0 wrap
        await FallingEdge(dut.clk)
        expected = cycle % 256
        assert dut.count.value == expected, f"cycle {cycle}: expected {expected}, got {dut.count.value}"