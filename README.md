# VISAInstrument

Programming control Parent class for Instruments that support VISA(Virtual Instrument Software Architecture) protocol.


## Usage

1. Install Pyvisa

```bash
pip install PyVISA
```

If the code cannot run correctly, you can install PyVISA==1.12.0 by `pip install PyVISA==1.12.0`.

2. Write your own instrument controlling code like `VisaExample.py` in directory `example`.

This file is based on Thorlabs ITC4001, and its mannual and programmer reference can be found in `example` folder.