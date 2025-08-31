/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    let numbers = x.toString().split("");
    let total = 0;
    for(i=0; i<numbers.length;i++){
        total += parseInt(numbers[i]);
    };
    if( x%total === 0 ){
        return total;
    } else {
        return -1;
    }
};