// how many measurements are larger than the previous one

var array = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
var indexLess = array[i] - 1
counter = 0;
for (let i = 1; i < array.length; i++) {
    if (indexLess > array[i]) {
        counter++;
        return "The number you are looking for is: " + counter; 
    }
}