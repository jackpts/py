**My Python scripts repo**

1. check-ad-classes
- Intended to check if the redundant classes found in native Ad templates and styles and reveal them out.

2. technodocbox-download
- Retrieving the direct link to PDF from technodocbox.com for non logined users

Examples:

    https://technodocbox.com/Unix/66519152-Learn-bash-the-hard-way.html
    --> http://pdftoword-converter.online/storage/documents/be9ba10b52cf0dede47251fb89cf0ae1.pdf

    https://technodocbox.com/Unix/74202510-Answers-to-awk-problems-shell-programming-future-using-loops-to-automate-tasks-download-and-install-python-windows-only-r.html
    ---> http://pdftoword-converter.online/storage/documents/b42aeddfc959a36065e5c32db52569b5.pdf
    
    https://technodocbox.com/Unix/71105609-Useful-unix-commands-cheat-sheet.html
    ---> http://pdftoword-converter.online/storage/documents/ab48878c0d462ea65d98fa275fad7e68.pdf

3. XML to CSV converter
Remake of the upwork task [https://github.com/jackpts/upwork/tree/master/002] from bash scripting to python version 
(using modules: xmltodict, csv).

4. epson-check-free
Check free serial numbers available for Epson printers.
You can specify the numbers to check as an input parameters or put the download excel file with these numbers close to the script.
Examples:
a) 
```
    python epson-check-free.py S9VY082652 X2MX039192
    Please specify Epson serial numbers as a parameters
        Example: python epson-check-free.py S9VY082652 X2MX039192
    OR download and put the /SN_list_with_country.xlsx file near this script!
    S9VY082652	ALREADY_USED
    X2MX039192	SUCCESSFUL
```

b)
```
    epson-check-free.py
    Please specify Epson serial numbers as a parameters
        Example: python epson-check-free.py S9VY082652 X2MX039192
    OR download and put the SN_list_with_country.xlsx file near this script!
    -------------------------
    xls File exists - start scanning...
    X2MX039192	SUCCESSFUL
    NASY203682	SERIAL_NUMBER_NOT_ELIGIBLE
```

5. 