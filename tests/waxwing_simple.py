#!/usr/bin/env python3
# Support for the Numato Saturn (http://numato.com/product/saturn-spartan-6-fpga-development-board-with-ddr-sdram)
# Original code from : https://github.com/timvideos/litex-buildenv/blob/master/targets/waxwing/base.py
# By Rohit Singh

import argparse
from fractions import Fraction

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

import waxwing_platform

from litex.soc.cores.clock import *
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *

from litedram.phy import s6ddrphy
from litedram.core import ControllerSettings

# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform, clk_freq):
        self.clock_domains.cd_sys    = ClockDomain()

        # # #

        self.submodules.pll = pll = S6PLL(speedgrade=-2)
        pll.register_clkin(platform.request("clk100"), 100e6)
        pll.create_clkout(self.cd_sys,    clk_freq)


# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self, sys_clk_freq=int(10e6), integrated_rom_size=0x8000, **kwargs):
        assert sys_clk_freq == int(10e6)
        platform = waxwing_platform.Platform()

        # SoCCore ----------------------------------------------------------------------------------
        SoCCore.__init__(self, platform, clk_freq=sys_clk_freq,
            integrated_rom_size=integrated_rom_size,
            integrated_main_ram_size=16*1024,
            **kwargs)
        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq)



# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on WaxWing")
    builder_args(parser)
    soc_core_args(parser)
    args = parser.parse_args()
    cls =  BaseSoC
    soc = cls(**soc_core_argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    builder.build(mode="yosys")


if __name__ == "__main__":
    main()
