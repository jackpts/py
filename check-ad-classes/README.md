Scripts for edmunds.com site, repo: libraries-adcreative-templates

1. check-ad-classes
- Intended to check if the redundant classes found in native Ad templates and styles and reveal them out.

2. scan-native-dir

### Working with scan-classes.py script

1. Pre-installation:

a) Need to install Python v.3 at least (mostly for regex logic functionality). 
Instruction: https://realpython.com/installing-python/

How to check:

    $ python3 --version
    Python 3.6.5

b) Recommended (but not obliged) to install python's `tabulate` module (https://pypi.org/project/tabulate/) for better output in table format:
    
    pip3 install tabulate
    
How to check:

    python -c "import tabulate"
If no errors during output (like `ModuleNotFoundError: No module named`) then all Ok.

Note: if this module isn't installed the output will be in simple format.
Note2: you can also customize the table output by changing the param inside the script: `tablefmt="psql"`

2. Run:

a) as a script in package.json:

    npm run scan-classes

b) directly via python:

    python3 scan-classes.py
    
3. Command line parameters:

a) input directory by default set inside the py script in var:

    scanDir = './units/native-ad-templates/'
You can customize this var or use a command line parameter to set another directory like this:

    python3 scan-classes.py --custom-path ./units/leaderboard/

b) Flag `--scan-imports` - add the possibility to scan for @import-ed styles inside the `style.scss` files.

    python3 scan-classes.py --scan-imports

**c) Flag `--scan-js` - add the possibility to scan for classes inside the `index.js` files (like `.hidden`, etc.).

    python3 scan-classes.py --scan-js
    
**d) Flag `--chunk-size` - add the possibility to format the output by number of classes per row
Because when the table is too wide and your terminal window is don't and too many classes found - it can be the issue.

    python3 scan-classes.py --chunk-size 7
Also you can set this variable inside the script - find `chunkSize = 4` line.

** - still in TODO.

4. Output example:
a) with tabulate module installed + custom path: 

>python3 scan-classes.py --custom-path ./units/leaderboard

Check if tabulate module is installed... Ok.
Checking if file with styles exists [./BMW_728x90/style.scss]... Ok.
Checking if file with template exists [./BMW_728x90/template.html]... Ok.
Checking if file with styles exists [./Cadillac_728x90/style.scss]... Ok.
Checking if file with template exists [./Cadillac_728x90/template.html]... Ok.

+--------------------------+--------------------------------------------------------------+
| adName/file              | Differences                                                  |
|--------------------------+--------------------------------------------------------------|
| BMW_728x90/template      | --- no differences ---                                       |
| BMW_728x90/styles        | --- no differences ---                                       |
| Cadillac_728x90/template | vehicle-info, vehicle-slider, vehicle-slide, vehicle-content |
|                          | slider-text, slide-info                                      |
| Cadillac_728x90/styles   | --- no differences ---                                       |
+--------------------------+--------------------------------------------------------------+

b) with no tabulate module installed and by default:

>npm run scan-classes

Check if tabulate module is installed... Not! 
Please install tabulate module for better output (as a table) via: pip3 install tabulate --user

Checking if file with styles exists [./SRP/style.scss]... Ok.
Checking if file with template exists [./SRP/template.html]... Ok.
Checking if file with styles exists [./SRP_Amp/style.scss]... Error! 
	 Please check the path:  /home/jacky/git/libraries-adcreative-templates/units/native-ad-templates/SRP_Amp/style.scss
Checking if file with template exists [./SRP_Amp/template.html]... Ok.
...
Checking if file with template exists [./VDP_Wired/template.html]... Ok.

['SRP/template']

		 ['oem-url, text-gray-dark, disclaimer-copy, mb-0_25']
		 ['mr-0_25, w-100, ad-label']
['SRP/styles']

		 ['flex-column, flex-wrap, mx-0_75, my-1']
		 ['display-3, col-8, mb-0_5, mt-1_75']
		 ['py-0_75, pr-0_5, flex-row, display-6']
		 ['col-4, display-4, btn-sm, ml-0_5']
		 ['h-100, text-gray-darker, info-title-break, xsmall']
		 ['px-0_5']
['SRP_Amp/styles']

		 ['--- nothing to compare, file not exists ---']
['Button/template']

		 ['--- no differences ---']
