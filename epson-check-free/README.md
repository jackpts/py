# epson-check-free
## Written by Yauheni Pauliukanets 01 Aug 2018

Check free serial numbers available for Epson printers.
You can specify the numbers to check as an input parameters or put the download excel file with these numbers close to the script.

Examples:

    > python epson-check-free.py S9VY082652 X2MX039192
    Please specify Epson serial numbers as a parameters
    OR download and put the SN_list_with_country.xlsx file close to this script.
    Examples:
             python epson-check-free.py S9VY082652 X2MX039192
             python epson-check-free.py --scan-range:200-250
             python epson-check-free.py --count-records
    ---------
    S9VY082652      ALREADY_USED
    X2MX039192      SUCCESSFUL
    
    > python epson-check-free.py --count-records
    Please specify Epson serial numbers as a parameters
    OR download and put the SN_list_with_country.xlsx file close to this script.
    Examples:
             python epson-check-free.py S9VY082652 X2MX039192
             python epson-check-free.py --scan-range:200-250
             python epson-check-free.py --count-records
    ---------
    Excel file exists - start scanning with Range: (1 - 9999)
    Total number of serials in Excel-file: 1340

    > python epson-check-free.py
    Please specify Epson serial numbers as a parameters
    OR download and put the SN_list_with_country.xlsx file close to this script.
    Examples:
             python epson-check-free.py S9VY082652 X2MX039192
             python epson-check-free.py --scan-range:200-250
             python epson-check-free.py --count-records
    ---------
    Excel file exists - start scanning with Range: (1 - 20)
    S9VY082652	ALREADY_USED
    X2MX039192	SUCCESSFUL
    NASY203682	SERIAL_NUMBER_NOT_ELIGIBLE
    ...

    > python epson-check-free.py --log --scan-range:1-2
    Please specify Epson serial numbers as a parameters
    OR download and put the SN_list_with_country.xlsx file close to this script.
    Examples:
             python epson-check-free.py S9VY082652 X2MX039192
             python epson-check-free.py --scan-range:200-250
             python epson-check-free.py --count-records
             python epson-check-free.py --log
    ---------
    Excel file exists - start scanning with Range: (1 - 2)
    X2MX039192      SUCCESSFUL
    NASY203682      SERIAL_NUMBER_NOT_ELIGIBLE

    LOG file epson_serials.log has been updated with 2 records
