/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let romanArray = s.split('');
    let total = 0;
    for(i=0; i<romanArray.length; i++){
        if(romanArray[i] === 'I'){
            if (romanArray[i+1] === 'V') {
                total += 4;
                i++;
            } else if(romanArray[i+1] === 'X') {
                total += 9;
                i++;
            }else {
                total += 1;
            }
        } else if (romanArray[i] === 'X'){
            if (romanArray[i+1] === 'L') {
                total += 40;
                i++;
            } else if(romanArray[i+1] === 'C') {
                total += 90;
                i++;
            }else {
                total += 10;
            }
        } else if (romanArray[i] === 'C') {
            if (romanArray[i+1] === 'D') {
                total += 400;
                i++;
            } else if(romanArray[i+1] === 'M') {
                total += 900;
                i++;
            }else {
                total += 100;
            }
        } else if (romanArray[i] === 'V'){
            total += 5;
        } else if (romanArray[i] === 'L'){
            total += 50;
        } else if (romanArray[i] === 'D'){
            total += 500;
        } else if (romanArray[i] === 'M'){
            total += 1000;
        }
    }
    return parseInt(total);
};