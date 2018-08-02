**My Python scripts repo**

## 1. check-ad-classes
- Intended to check if the redundant classes found in native Ad templates and styles and reveal them out.

## 2. technodocbox-download
- Retrieving the direct link to PDF from technodocbox.com for non logined users

Examples:

    https://technodocbox.com/Unix/66519152-Learn-bash-the-hard-way.html
    --> http://pdftoword-converter.online/storage/documents/be9ba10b52cf0dede47251fb89cf0ae1.pdf

    https://technodocbox.com/Unix/74202510-Answers-to-awk-problems-shell-programming-future-using-loops-to-automate-tasks-download-and-install-python-windows-only-r.html
    ---> http://pdftoword-converter.online/storage/documents/b42aeddfc959a36065e5c32db52569b5.pdf
    
    https://technodocbox.com/Unix/71105609-Useful-unix-commands-cheat-sheet.html
    ---> http://pdftoword-converter.online/storage/documents/ab48878c0d462ea65d98fa275fad7e68.pdf

## 3. XML to CSV converter
Remake of the upwork task [https://github.com/jackpts/upwork/tree/master/002] from bash scripting to python version 
(using modules: xmltodict, csv).

## 4. epson-check-free
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

    > python epson-check-free.py --scan-range:1335-1499
    Please specify Epson serial numbers as a parameters
    OR download and put the SN_list_with_country.xlsx file close to this script.
    Examples:
             python epson-check-free.py S9VY082652 X2MX039192
             python epson-check-free.py --scan-range:200-250
             python epson-check-free.py --count-records
    ---------
    Excel file exists - start scanning with Range: (1335 - 1499)
    SEGY269813      SUCCESSFUL
    R2LY017735      SERIAL_NUMBER_NOT_ELIGIBLE
    X2U2002955      PRINTER_MODEL_NOT_FOUND_IN_NEON
    X2U2003000      PRINTER_MODEL_NOT_FOUND_IN_NEON
    S9JY117651      ALREADY_USED
    
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

## 5. 