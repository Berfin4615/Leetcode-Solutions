/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    function isNoZero(x) {
        return !x.toString().includes('0');
    }

    for (let a = 1; a < n; a++) {
        let b = n - a;
        if (isNoZero(a) && isNoZero(b)) {
            return [a, b];
        }
    }
};