import styles from './style.scss'; // eslint-disable-line no-unused-vars
import vars from './merge-vars.json'; // eslint-disable-line no-unused-vars
import start from '../../../assets/js/leaderboard-start';

const tpls = {
    img: '#tplImg',
    info: '#tplInfo'
};

if (document.readyState === 'complete') {
    start(tpls);
} else {
    window.onload = () => {
        start(tpls);
    };
}
