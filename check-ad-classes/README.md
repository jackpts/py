Scripts for edmunds.com site, repo: libraries-adcreative-templates

1. check-ad-classes
- Intended to check if the redundant classes found in native Ad templates and styles and reveal them out.

2. scan-native-dir
- scans native ad dir for sub-directories with templates/styles and checks them for redundant/missed classes

a) Need to install `Python v.3` to operate with RE(gex) module
b) Need to install `tabulate` module to be able to output in table format:

    pip3 install tabulate --user

***Example output*** (with no table mode):

python3 scan-native-dir.py 

Check if tabulate module installed... Ok.

Checking if file with styles exists [./Build_and_Price_Wired/style.scss]... Ok.

Checking if file with template exists [./Build_and_Price_Wired/template.html]... Ok.

Checking if file with styles exists [./SRP/style.scss]... Ok.

Checking if file with template exists [./SRP/template.html]... Ok.

Checking if file with styles exists [./Article_Wired/style.scss]... Ok.

Checking if file with template exists [./Article_Wired/template.html]... Ok.

Checking if file with styles exists [./Map_Mobile/style.scss]... Ok.

Checking if file with template exists [./Map_Mobile/template.html]... Ok.

.....

Checking if file with template exists [./VDP_Wired/template.html]... Ok.

['Build_and_Price_Wired/template']

		 ['disclaimer-copy, ad-label, btn-link, custom-data']
		 ['btn-outline-primary, text-gray-dark']
		 
['Build_and_Price_Wired/styles']

		 ['border-radius, ml-1, text-primary, d-block']
		 ['font-weight-normal, mt-0_5, border-2, p-0']
		 ['d-inline-block, mr-0_5, pt-2, mb-0_75']
		 ['no-custom-data, border-gray, color-swatch, xsmall']
		 ['mx-auto, border-1']
		 
['SRP/template']

		 ['w-100, disclaimer-copy, mb-0_25, mr-0_25']
		 ['ad-label, oem-url, text-gray-dark']
		 
['SRP/styles']

		 ['display-4, flex-column, my-1, mt-1_75']
		 ['col-8, col-4, btn-sm, info-title-break']
		 ['flex-row, mb-0_5, pr-0_5, ml-0_5']
		 ['flex-wrap, display-3, display-6, py-0_75']
		 ['h-100, mx-0_75, px-0_5, xsmall']
		 ['text-gray-darker']
		 
['Article_Wired/template']

		 ['disclaimer-copy, jelly-bean, cta-body-text, flex-row']
		 ['pr-1_5, body-container, px-1_5']
		 
['Article_Wired/styles']

		 ['justify-content-around, w-100, mr-0_75, pr-2_75']
		 ['pt-3_5, font-weight-normal, font-weight-bold, ml-3']
		 ['mr-0_5, pb-1_5, mt-1_25, ml-0_25']
		 ['pt-0_5, text-center']
		 
['Map_Mobile/template']

		 ['px-1, disclaimer-copy, map-image, rounded']
		 ['py-1, cta2']
		 
['Map_Mobile/styles']

		 ['justify-content-center, text-gray-dark']
['Medium_Rectangle_Amp/template']

		 ['button-secondary, stretch, root-container, carousel-container']
		 ['button, carousel, logo-img, carousel-item']
		 ['footer, carousel-img']
		 
['Medium_Rectangle_Amp/styles']

		 ['cta-container, hidden, persistent-disclaimer, mt-0_25']
		 ['text-primary, d-block, mx-0_25, pt-1_75']
		 ['disclaimer-button, d-none, oem-logo, font-weight-bold']
		 ['d-flex, text-uppercase, jelly-bean, disclaimer-content']
		 ['mr-0_25, justify-content-between, text-gray, my-0_5']
		 ['disclaimer-close, card, disclaimer, display-5']
		 ['py-1_5, cta, ml-0_25, px-1_5']
		 ['text-center, xsmall, text-gray-darker, text-gray-dark']
		 ['vehicle-block']
		 
['Pricing_Module/template']

		 ['justify-content-center, label2, disclaimer-copy, headline2']
		 ['align-items-center, jelly-bean, d-flex, native-ad-disclaimer-pricing']
		 ['ad-label, label3, label, mx-md-0']
		 
['Pricing_Module/styles']

		 ['display-5, large, small), invisible']
['Pricing_Fresh_Core_Mobile/template']

		 ['msrp, disclaimer-text, ad-label, local']
		 ['cta-text, disclaimer-img']
['Pricing_Fresh_Core_Mobile/styles']

		 ['d-none, display-5']
['Conquest_YSC_Wired/template']

		 ['disclaimer-text, logo, disclaimer-label, disclaimer-img']
		 ['ad-label']
['Conquest_YSC_Wired/styles']

		 ['display-5, ml-0_5, align-items-center, mr-0_25']
		 ['mt-1, mb-0_75']
['Pricing_Fresh_Core_Wired/template']

		 ['msrp, disclaimer-text, oem-logo, local']
		 ['cta-text, ad-label']
['Pricing_Fresh_Core_Wired/styles']

		 ['logo-wrapper, display-5, d-none, logo']
['Build_and_Price_Mobile/template']

		 ['disclaimer-copy, pt-1_75, ad-label, btn-link']
		 ['custom-data, btn-outline-primary, text-gray-dark']
['Build_and_Price_Mobile/styles']

		 ['conquest, border-radius, mt-1, text-primary']
		 ['d-block, border-2, d-inline-block, text-left']
		 ['mr-0_5, mt-1_5, mb-1_5, no-custom-data']
		 ['border-gray, color-swatch, mt-1_25, xsmall']
		 ['mx-auto, border-1']
['MPG_Wired/template']

		 ['city, slider-wrapper, max-range, disclaimer-copy']
		 ['cta, hwy, custom-data, cta2']
		 ['mpg-calculator, weighted-average, min-range']
['MPG_Wired/styles']

		 ['d-none']
['Map_Wired/template']

		 ['px-1, disclaimer-copy, map-image, rounded']
		 ['py-1, cta2, map']
['Map_Wired/styles']

		 ['justify-content-center']
['Enhanced_Spotlight/template']

		 ['disclaimer-text, photo-disclaimer, ad-label, vehicle-block']
['Enhanced_Spotlight/styles']

		 ['display-5']
['Leaderboard/template']

		 ['disclaimer-copy, headline2, cta4, cta2']
		 ['cta1, cta3, ad-container']
['Leaderboard/styles']

		 ['my-1, display-5, ml
		 -0_75, mx-0_75']
		 ['my-1_5']
['Button/template']

		 ['---== no differences ==---']
['Button/styles']

		 ['hidden']
['Incentives_Fresh_Core_Mobile/template']

		 ['label-text, disclaimer-text, w-100, oem-logo']
		 ['text-left, headline2, cta, headline']
		 ['cta-text, ad-label, body-text, text-right']

['VDP_Wired/template']

		 ['disclaimer-copy, row, medium, ad-label']
		 ['flex-row, oem-url, mb-0_5, headline2']
		 ['cta, headline, view-offer']
['VDP_Wired/styles']

		 ['mt-1_75, mt-2_25, mt-2, mr-0_25']
		 ['mt-3, mt-1_5, mt-2_75, display-5']
		 ['mt-1_25, mt-2_5']
