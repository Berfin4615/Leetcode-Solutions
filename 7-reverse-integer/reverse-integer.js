/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const limit = 2 ** 31;
    const reversed = parseInt(Math.abs(x).toString().split('').reverse().join(''));
    const result = x < 0 ? -reversed : reversed;
    if (result < -limit || result > limit - 1) {
        return 0;
    }
    return result;
};