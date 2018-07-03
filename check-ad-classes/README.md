Scripts for edmunds.com site, repo: libraries-adcreative-templates

1. check-ad-classes
- Intended to check if the redundant classes found in native Ad templates and styles and reveal them out.

2. scan-native-dir
- scans native ad dir for sub-directories with templates/styles and checks them for redundant/missed classes


***Example output***:

python scan-native-dir.py 
Check if tabulate module installed... Ok.
Checking if file with styles exists [./Build_and_Price_Wired/style.scss]... Ok.
Checking if file with template exists [./Build_and_Price_Wired/template.html]... Ok.
Checking if file with styles exists [./SRP/style.scss]... Ok.
Checking if file with template exists [./SRP/template.html]... Ok.
Checking if file with styles exists [./Article_Wired/style.scss]... Ok.
Checking if file with template exists [./Article_Wired/template.html]... Ok.
Checking if file with styles exists [./Map_Mobile/style.scss]... Ok.
Checking if file with template exists [./Map_Mobile/template.html]... Ok.
Checking if file with styles exists [./Medium_Rectangle_Amp/style.scss]... Ok.
Checking if file with template exists [./Medium_Rectangle_Amp/template.html]... Ok.
Checking if file with styles exists [./Pricing_Module/style.scss]... Ok.
Checking if file with template exists [./Pricing_Module/template.html]... Ok.
Checking if file with styles exists [./Pricing_Fresh_Core_Mobile/style.scss]... Ok.
Checking if file with template exists [./Pricing_Fresh_Core_Mobile/template.html]... Ok.
Checking if file with styles exists [./Conquest_YSC_Wired/style.scss]... Ok.
Checking if file with template exists [./Conquest_YSC_Wired/template.html]... Ok.
Checking if file with styles exists [./Pricing_Fresh_Core_Wired/style.scss]... Ok.
Checking if file with template exists [./Pricing_Fresh_Core_Wired/template.html]... Ok.
Checking if file with styles exists [./Build_and_Price_Mobile/style.scss]... Ok.
Checking if file with template exists [./Build_and_Price_Mobile/template.html]... Ok.
Checking if file with styles exists [./MPG_Wired/style.scss]... Ok.
Checking if file with template exists [./MPG_Wired/template.html]... Ok.
Checking if file with styles exists [./Map_Wired/style.scss]... Ok.
Checking if file with template exists [./Map_Wired/template.html]... Ok.
Checking if file with styles exists [./Enhanced_Spotlight/style.scss]... Ok.
Checking if file with template exists [./Enhanced_Spotlight/template.html]... Ok.
Checking if file with styles exists [./Leaderboard/style.scss]... Ok.
Checking if file with template exists [./Leaderboard/template.html]... Ok.
Checking if file with styles exists [./Button/style.scss]... Ok.
Checking if file with template exists [./Button/template.html]... Ok.
Checking if file with styles exists [./Incentives_Fresh_Core_Mobile/style.scss]... Ok.
Checking if file with template exists [./Incentives_Fresh_Core_Mobile/template.html]... Ok.
Checking if file with styles exists [./Conquest_Filmstrip/style.scss]... Ok.
Checking if file with template exists [./Conquest_Filmstrip/template.html]... Ok.
Checking if file with styles exists [./SRP_Amp/style.scss]... Ok.
Checking if file with template exists [./SRP_Amp/template.html]... Ok.
Checking if file with styles exists [./Incentives_Fresh_Core_Wired/style.scss]... Ok.
Checking if file with template exists [./Incentives_Fresh_Core_Wired/template.html]... Ok.
Checking if file with styles exists [./Medium_Rectangle/style.scss]... Ok.
Checking if file with template exists [./Medium_Rectangle/template.html]... Ok.
Checking if file with styles exists [./Photoflipper_Mobile/style.scss]... Ok.
Checking if file with template exists [./Photoflipper_Mobile/template.html]... Ok.
Checking if file with styles exists [./Article_Mobile/style.scss]... Ok.
Checking if file with template exists [./Article_Mobile/template.html]... Ok.
Checking if file with styles exists [./Photoflipper_Wired/style.scss]... Ok.
Checking if file with template exists [./Photoflipper_Wired/template.html]... Ok.
Checking if file with styles exists [./Conquest_YSC_Mobile/style.scss]... Ok.
Checking if file with template exists [./Conquest_YSC_Mobile/template.html]... Ok.
Checking if file with styles exists [./MPG_Mobile/style.scss]... Ok.
Checking if file with template exists [./MPG_Mobile/template.html]... Ok.
Checking if file with styles exists [./VDP_Mobile/style.scss]... Ok.
Checking if file with template exists [./VDP_Mobile/template.html]... Ok.
Checking if file with styles exists [./VDP_Wired/style.scss]... Ok.
Checking if file with template exists [./VDP_Wired/template.html]... Ok.

+---------------------------------------+----------------------------------------------------------------+
| adName/file                           | Differences                                                    |
|---------------------------------------+----------------------------------------------------------------|
| Build_and_Price_Wired/template        | btn-link, ad-label, btn-outline-primary, disclaimer-copy       |
|                                       | custom-data, text-gray-dark                                    |
| Build_and_Price_Wired/styles          | color-swatch, d-block, no-custom-data, mb-0_75                 |
|                                       | border-2, font-weight-normal, ml-1, border-radius              |
|                                       | mx-auto, pt-2, border-gray, text-primary                       |
|                                       | mr-0_5, p-0, border-1, xsmall                                  |
|                                       | d-inline-block, mt-0_5                                         |
| SRP/template                          | ad-label, disclaimer-copy, w-100, mb-0_25                      |
|                                       | oem-url, mr-0_25, text-gray-dark                               |
| SRP/styles                            | btn-sm, col-8, my-1, ml-0_5                                    |
|                                       | mt-1_75, display-6, pr-0_5, mx-0_75                            |
|                                       | mb-0_5, px-0_5, display-3, flex-wrap                           |
|                                       | info-title-break, text-gray-darker, col-4, flex-column         |
|                                       | flex-row, display-4, xsmall, py-0_75                           |
|                                       | h-100                                                          |
| Article_Wired/template                | px-1_5, jelly-bean, cta-body-text, body-container              |
|                                       | disclaimer-copy, flex-row, pr-1_5                              |
| Article_Wired/styles                  | font-weight-bold, mr-0_75, text-center, pt-0_5                 |
|                                       | font-weight-normal, w-100, pb-1_5, mr-0_5                      |
|                                       | mt-1_25, pr-2_75, ml-0_25, justify-content-around              |
|                                       | pt-3_5, ml-3                                                   |
| Map_Mobile/template                   | py-1, px-1, cta2, map-image                                    |
|                                       | rounded, disclaimer-copy                                       |
| Map_Mobile/styles                     | text-gray-dark, justify-content-center                         |
| Medium_Rectangle_Amp/template         | carousel-container, root-container, carousel, carousel-img     |
|                                       | stretch, button-secondary, button, footer                      |
|                                       | carousel-item, logo-img                                        |
| Medium_Rectangle_Amp/styles           | font-weight-bold, d-none, d-block, disclaimer                  |
|                                       | py-1_5, text-gray, mx-0_25, card                               |
|                                       | px-1_5, cta, text-center, jelly-bean                           |
|                                       | disclaimer-button, mt-0_25, justify-content-between, display-5 |
|                                       | d-flex, cta-container, my-0_5, disclaimer-close                |
|                                       | text-primary, disclaimer-content, mr-0_25, text-uppercase      |
|                                       | text-gray-darker, ml-0_25, vehicle-block, pt-1_75              |
|                                       | xsmall, text-gray-dark, hidden, persistent-disclaimer          |
|                                       | oem-logo                                                       |
| Pricing_Module/template               | jelly-bean, mx-md-0, align-items-center, label                 |
|                                       | ad-label, native-ad-disclaimer-pricing, label2, label3         |
|                                       | disclaimer-copy, headline2, d-flex, justify-content-center     |
| Pricing_Module/styles                 | large, small), invisible, display-5                            |
| Pricing_Fresh_Core_Mobile/template    | msrp, disclaimer-img, ad-label, local                          |
|                                       | cta-text, disclaimer-text                                      |
| Pricing_Fresh_Core_Mobile/styles      | d-none, display-5                                              |
| Conquest_YSC_Wired/template           | disclaimer-img, logo, ad-label, disclaimer-label               |
|                                       | disclaimer-text                                                |
| Conquest_YSC_Wired/styles             | align-items-center, mt-1, mr-0_25, mb-0_75                     |
|                                       | display-5, ml-0_5                                              |
| Pricing_Fresh_Core_Wired/template     | msrp, ad-label, disclaimer-text, local                         |
|                                       | cta-text, oem-logo                                             |
| Pricing_Fresh_Core_Wired/styles       | logo, d-none, logo-wrapper, display-5                          |
| Build_and_Price_Mobile/template       | btn-link, ad-label, btn-outline-primary, disclaimer-copy       |
|                                       | custom-data, pt-1_75, text-gray-dark                           |
| Build_and_Price_Mobile/styles         | text-left, color-swatch, d-block, no-custom-data               |
|                                       | border-2, border-radius, mx-auto, conquest                     |
|                                       | border-gray, mb-1_5, mt-1_5, text-primary                      |
|                                       | mr-0_5, mt-1_25, border-1, mt-1                                |
|                                       | xsmall, d-inline-block                                         |
| MPG_Wired/template                    | min-range, city, max-range, cta2                               |
|                                       | mpg-calculator, weighted-average, hwy, cta                     |
|                                       | disclaimer-copy, custom-data, slider-wrapper                   |
| MPG_Wired/styles                      | d-none                                                         |
| Map_Wired/template                    | map, py-1, px-1, cta2                                          |
|                                       | map-image, rounded, disclaimer-copy                            |
| Map_Wired/styles                      | justify-content-center                                         |
| Enhanced_Spotlight/template           | vehicle-block, ad-label, photo-disclaimer, disclaimer-text     |
| Enhanced_Spotlight/styles             | display-5                                                      |
| Leaderboard/template                  | cta4, cta3, cta2, ad-container                                 |
|                                       | cta1, disclaimer-copy, headline2                               |
| Leaderboard/styles                    | ml-0_75, mx-0_75, my-1_5, display-5                            |
|                                       | my-1                                                           |
| Button/template                       | ---== no differences ==---                                     |
| Button/styles                         | hidden                                                         |
| Incentives_Fresh_Core_Mobile/template | text-left, label-text, ad-label, headline                      |
|                                       | body-text, cta-text, disclaimer-text, cta                      |
|                                       | w-100, headline2, text-right, oem-logo                         |
| Incentives_Fresh_Core_Mobile/styles   | px-2_25, mt-0_25, display-5, pos-a                             |
|                                       | mr-0_25, persistent-disclaimer                                 |
| Conquest_Filmstrip/template           | jelly-bean, ad-label, label2, persistent-disclaimer            |
|                                       | disclaimer-button, cta-text, disclaimer-copy, img-block        |
| Conquest_Filmstrip/styles             | display-5, mb-0_5                                              |
| SRP_Amp/template                      | ad-label, disclaimer-copy, w-100, mb-0_25                      |
|                                       | oem-url, mr-0_25, icon-cancel-circle2, text-gray-dark          |
| SRP_Amp/styles                        | btn-sm, col-8, my-1, ml-0_5                                    |
|                                       | mt-1_75, display-6, pr-0_5, mx-0_75                            |
|                                       | mb-0_5, px-0_5, display-3, flex-wrap                           |
|                                       | info-title-break, text-gray-darker, col-4, flex-column         |
|                                       | flex-row, display-4, xsmall, py-0_75                           |
|                                       | h-100                                                          |
| Incentives_Fresh_Core_Wired/template  | text-left, label-text, jelly-bean, ad-label                    |
|                                       | headline, cta-text, disclaimer-text, cta                       |
|                                       | w-100, headline2, text-right, oem-logo                         |
| Incentives_Fresh_Core_Wired/styles    | px-2_25, display-5, d-block, mr-0_5                            |
| Medium_Rectangle/template             | main-block, cta4, cta3, headline                               |
|                                       | cta2, ad-container, px-1_5, cta1                               |
|                                       | disclaimer-copy, headline2                                     |
| Medium_Rectangle/styles               | display-5                                                      |
| Photoflipper_Mobile/template          | flex-row, oem-url, cta, disclaimer-copy                        |
| Photoflipper_Mobile/styles            | px-0_75, mr-0_75, py-1_5, align-self-end                       |
|                                       | display-5                                                      |
| Article_Mobile/template               | main-container, flex-row, jelly-bean, cta-body-text            |
|                                       | disclaimer-button, body-container, disclaimer-copy             |
| Article_Mobile/styles                 | px-2_25, disclaimer-label, px-2_5, display-5                   |
|                                       | mt-0_5                                                         |
| Photoflipper_Wired/template           | headline2, oem-url, headline, cta                              |
|                                       | disclaimer-copy                                                |
| Photoflipper_Wired/styles             | px-1_5, display-5                                              |
| Conquest_YSC_Mobile/template          | disclaimer-img, logo, ad-label, vehicle-img                    |
|                                       | disclaimer-text, disclaimer-label                              |
| Conquest_YSC_Mobile/styles            | mt-1_25, mr-0_25, my-0_25, mt-1                                |
|                                       | vehicle-content, display-5                                     |
| MPG_Mobile/template                   | pl-3, min-range, city, hwy                                     |
|                                       | max-range, info-wrapper, cta2, mpg-calculator                  |
|                                       | weighted-average, cta, disclaimer-copy, custom-data            |
|                                       | slider-wrapper                                                 |
| MPG_Mobile/styles                     | d-none, pr-3_5, mb-0_25                                        |
| VDP_Mobile/template                   | py-1_5, px-1_5, cta, headline2                                 |
|                                       | ad-label, disclaimer-copy, oem-url, headline                   |
|                                       | ad-container, oem-logo                                         |
| VDP_Mobile/styles                     | mt-2_25, mt-1_75, mt-2_5, display-5                            |
|                                       | mt-2, mt-1_5, mr-0_25, mt-2_75                                 |
|                                       | mt-0, mt-1_25, mt-0_5                                          |
| VDP_Wired/template                    | cta, headline2, ad-label, view-offer                           |
|                                       | medium, disclaimer-copy, mb-0_5, oem-url                       |
|                                       | headline, row, flex-row                                        |
| VDP_Wired/styles                      | mt-2_25, mt-1_75, mt-3, mt-2_5                                 |
|                                       | display-5, mt-2, mt-1_5, mr-0_25                               |
|                                       | mt-2_75, mt-1_25                                               |
+---------------------------------------+----------------------------------------------------------------+
