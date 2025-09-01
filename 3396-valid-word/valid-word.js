/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    let letters = word.split("");
    const consonants = word.split('').filter(
        char => 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'.includes(char));
    if(letters.length < 3){
        return false;
    } else if(letters.includes('@') || letters.includes('#') || letters.includes('$')){
        return false;
    } else if(!letters.includes('a') && !letters.includes('e') && !letters.includes('i') && !letters.includes('o') && !letters.includes('u') && !letters.includes('A') && !letters.includes('E') && !letters.includes('I') && !letters.includes('O') && !letters.includes('U')){
        return false;
    } else if(consonants.length === 0){
        return false;
    } else {
        return true;
    }
};