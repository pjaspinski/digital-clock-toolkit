# Digital Clock Toolkit

This is a Python script that can communicate over Bluetooth with clocks made using (3D-7-Segment-Digital-Clock)[https://github.com/leonvandenbeukel/3D-7-Segment-Digital-Clock] repository. It can be used instead of the Android app that is not available on Play Store anymore.

## Supported functions

-   setting current time to the clock

If you need other functions then create an issue or make a PR.

## How to use

-   Make sure that you have Python installed
-   Install the only required dependency: `pip install pybluez2`
-   Run `python digital-clock-toolkit.py`

If you run into `A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond` error, make sure that you are close to clock so that Bluetooth connection can be made.
