/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const limit = 2 ** 31;
    const reversed = parseInt(Math.abs(x).toString().split('').reverse().join(''));
    if (reversed < -limit || reversed > limit - 1) {
        return 0;
    } else {
        const result = x < 0 ? -reversed : reversed;
        return result;
    }
};