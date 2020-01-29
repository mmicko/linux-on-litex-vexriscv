# Support for the Numato Waxwing Spartan 6 Development Module
# https://numato.com/product/waxwing-spartan-6-fpga-development-board
# Original code from https://github.com/timvideos/litex-buildenv/blob/master/platforms/waxwing.py
# By Rohit Singh

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform
from litex.build.xilinx.programmer import iMPACT



_io = [
    ("clk100", 0, Pins("D11"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx",  Pins("T20")),
        Subsignal("rx",  Pins("T19")),
        IOStandard("LVCMOS33")
    ),    
    ("ddram_clock", 0,
        Subsignal("p", Pins("F2")),
        Subsignal("n", Pins("F1")),
        IOStandard("DIFF_SSTL18_II"), Misc("IN_TERM=NONE")
    ),
    ("ddram", 0,
        Subsignal("a", Pins(
            "M5 L4 K3 M4 K5 G3 G1 K4",
            "C3 C1 K6 B1 J4")),
        Subsignal("ba", Pins("E3 E1 D1")),
        Subsignal("ras_n", Pins("N4")),
        Subsignal("cas_n", Pins("P3")),
        Subsignal("we_n", Pins("D2")),
        Subsignal("dm", Pins("H2 H1")),
        Subsignal("dq", Pins(
            "N3 N1 M2 M1 J3 J1 K2 K1",
            "P2 P1 R3 R1 U3 U1 V2 V1")),
        Subsignal("dqs", Pins("T2 L3"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("T1 L1"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke", Pins("J6")),
        Subsignal("odt", Pins("M3")),
        #Subsignal("cs_n", Pins("K6")),
        IOStandard("SSTL18_II"),
    ),
    ("user_btn", 0, Pins("E6"), IOStandard("LVCMOS33"), Misc("PULLUP")),
    ("user_btn", 1, Pins("D5"), IOStandard("LVCMOS33"), Misc("PULLUP")),
    ("user_btn", 2, Pins("A3"), IOStandard("LVCMOS33"), Misc("PULLUP")),
    ("user_btn", 3, Pins("AB9"), IOStandard("LVCMOS33"), Misc("PULLUP")),

    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("C12")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        #Subsignal("rst_n", Pins("D5")), #button 1
        Subsignal("rx_data", Pins("C13 C14")),
        Subsignal("crs_dv", Pins("B14")),
        Subsignal("tx_en", Pins("D15")),
        Subsignal("tx_data", Pins("E10 F10")),
        Subsignal("mdc", Pins("C15")),
        Subsignal("mdio", Pins("A14")),
        Subsignal("rx_er", Pins("A13")),
        IOStandard("LVCMOS33")
     ),
]

## Ethernet
	#NET	"ETH_REFCLK"		LOC=C12	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L37N_GCLK12_0,	Sch name = ETH-REFCLK
	#NET	"ETH_PHY_MDC"	LOC=C15	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L62P_0,					Sch name = ETH-MDC
	#NET	"ETH_PHY_MDIO"	LOC=A14	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L50N_0,					Sch name = ETH-MDIO
	#NET	"ETH_TX_EN"			LOC=D15	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L46P_0,					Sch name = ETH-TXEN
	#NET	"ETH_TXD[0]"			LOC=E10	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L38N_VREF_0,		Sch name = ETH-TXD0
	#NET	"ETH_TXD[1]"			LOC=F10	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L38P_0,					Sch name = ETH-TXD1
	#NET	"ETH_CRSDV"		LOC=B14	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L50P_0,					Sch name = ETH-CRSDV
	#NET	"ETH_RXERR"		LOC=A13	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L48N_0,					Sch name = ETH-RXERR
	#NET	"ETH_RXD[0]"		LOC=C13	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L48P_0,					Sch name = ETH-RXD0
	#NET	"ETH_RXD[1]"		LOC=C14	|	IOSTANDARD=LVCMOS33;			#Bank = 0, pin name = IO_L46N_0,					Sch name = ETH-RXD1


_connectors = [
]

class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.00

    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx45-3csg484", _io, _connectors)

    def create_programmer(self):
        return iMPACT()