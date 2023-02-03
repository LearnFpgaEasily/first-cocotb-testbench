# "random" is a standard package it is installed with python
import random
# "cocotb" is not a standard package, we installed it with "pip install cocotb" in our virtual environnement
import cocotb
# just an egornomic import. If you don't import Clock and FallingEdge you will have to call it in your code by writing "cocotb.clock.Clock" or "cocotb.triggers.FallingEdge" everytime.
# Not doing it will lead to a less readable and longer code. Doing it is a good practice.
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge

# @cocotb.test() is a python decorator, telling cocotb framework that the function directly under is a cocotb test.
@cocotb.test()
# async is a reserved word in python to indicate that the function "test_ddd_simple" is asynchrone. To over simplify, it can wait for other function before continuing.
async def test_dff_simple(dut):
    # a comment between three quote under a function defintition is docstring. in cocotb the docstring of a test is show when you launch the test.
    """ Test that d propagates to q """

    # Delaration of the clock object first parameter is our clock signal, second the period, third the unit of the period.
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # the clock start is also a async function, meaning it start and the fonction test_dff_simple continue without waiting clock.start() to finish.
    # the clock will continue ticking until the end of the smulation.
    cocotb.start_soon(clock.start())  # Start the clock

    # a really simple python for loop of 10 iteration. Our test will test 10 random value then stop
    for i in range(10):
        # generate a random value that equal 0 or 1
        val = random.randint(0, 1)
        # set the prevously genreated random value in the input q. Don't forget the .value "dut.d = val" is invalid
        dut.d.value = val  # Assign the random value val to the input port d
        # await is a reserved word in python that wait for a fonction to return something. here we wait that Falling edge on our clock occur.
        await FallingEdge(dut.clk)
        # translation :  "check that the output q is equal to val, otherwise raise in error with the message under quote"
        assert dut.q.value == val, f"output q was incorrect on the {i}th cycle. Got {dut.q.value} expected {val}".format(i, dut.q.value, val)