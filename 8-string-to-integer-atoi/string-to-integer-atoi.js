/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    s = s.trimStart();

    if (s.length === 0) return 0;

    let sign = 1;
    let i = 0;
    let result = 0;

    if (s[i] === '-') {
        sign = -1;
        i++;
    } else if (s[i] === '+') {
        i++;
    }

    while (i < s.length && s[i] >= '0' && s[i] <= '9') {
        let digit = s[i].charCodeAt(0) - '0'.charCodeAt(0);

        result = result * 10 + digit;
        
        if (sign === 1 && result >= 2147483647) return 2147483647;
        if (sign === -1 && result >= 2147483648) return -2147483648;

        i++;
    }

    return result * sign;
};