# epson-check-free
## Written by Yauheni Pauliukanets 01 Aug 2018

Check free serial numbers available for Epson printers.
You can specify the numbers to check as an input parameters or put the download excel file with these numbers close to the script.

Examples:

```
    > python epson-check-free.py S9VY082652 X2MX039192
    Please specify Epson serial numbers as a parameters
        Example: python epson-check-free.py S9VY082652 X2MX039192
    OR download and put the /SN_list_with_country.xlsx file near this script!
    S9VY082652	ALREADY_USED
    X2MX039192	SUCCESSFUL

    >epson-check-free.py
    Please specify Epson serial numbers as a parameters
        Example: python epson-check-free.py S9VY082652 X2MX039192
    OR download and put the SN_list_with_country.xlsx file close to this script!
    -------------------------
    xls File exists - start scanning...
    S9VY082652	ALREADY_USED
    X2MX039192	SUCCESSFUL
    NASY203682	SERIAL_NUMBER_NOT_ELIGIBLE
    ...
```