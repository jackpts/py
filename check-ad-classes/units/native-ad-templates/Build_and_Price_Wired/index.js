import styles from './style.scss'; // eslint-disable-line no-unused-vars
import vars from './merge-vars.json'; // eslint-disable-line no-unused-vars
import { checkDisclaimerContent } from '../../../assets/js/common/helpers';
import {loadPhotoDetails, initColorPicker, defaultImgSrc} from '../../../assets/js/color-picker/color-picker';

const disclaimerElements = {
    content: '.disclaimer-content',
    button: '.disclaimer-button',
    closeButton: '.disclaimer-close',
    copy: '.disclaimer-copy'
};
const adContainer = document.querySelector('.ad-container');

function setDefaultJellybean(photo) {
    const jellybean = document.querySelector('.jelly-bean');
    jellybean.src = photo || defaultImgSrc;
}
function hideColorPicker() {
    adContainer.classList.add('no-custom-data');
    setDefaultJellybean();
}
function checkJellybeansReceiving(photoDetail) {
    let jellybeansCount = 0;
    if (photoDetail.colorInfo && photoDetail.colorInfo.length) {
        jellybeansCount = (photoDetail.colorInfo.filter((ci) => ci.path.length > 0)).length;
    }
    if (jellybeansCount === 0 && photoDetail.photo) {
        setDefaultJellybean(photoDetail.photo);
    }
}
function checkConquest(hasConquest) {
    const conquestRibbon = document.querySelector('.conquest-ribbon');
    if (hasConquest) {
        conquestRibbon.classList.remove('hidden');
        adContainer.classList.add('conquest');
    }
}

window.onload = function() {
    const photoDetail = loadPhotoDetails(document.querySelector('.custom-data').innerHTML);
    (photoDetail.colorInfo && photoDetail.colorInfo.length) ? initColorPicker(photoDetail.colorInfo) : hideColorPicker();

    checkJellybeansReceiving(photoDetail);
    checkConquest(photoDetail.isConquest);
    checkDisclaimerContent(disclaimerElements);
};
