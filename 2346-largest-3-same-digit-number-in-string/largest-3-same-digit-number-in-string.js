/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    const liste = num.split("");
    let biggest = "";

    for (let i = 0; i < liste.length - 2; i++) {
        if (liste[i] === liste[i + 1] && liste[i + 1] === liste[i + 2]) {
            let goodNumber = liste[i] + liste[i] + liste[i];
            if (goodNumber > biggest) {
                biggest = goodNumber;
            }
        }
    }

    return biggest;
};
