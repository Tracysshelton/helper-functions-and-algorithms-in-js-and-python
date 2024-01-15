// This is a function that will check for Armstrong numbers
function isArmstrong($num) {
    // Convert the number to a string to find the number of digits
    $numStr = (string)$num;
    $numDigits = strlen($numStr);
    
    // Initialize sum
    $sum = 0;
    
    // Iterate over each digit and add its power to the sum
    for ($i = 0; $i < $numDigits; $i++) {
        $digit = (int)$numStr[$i];
        $sum += pow($digit, $numDigits);
    }
    
    // Check if the sum is equal to the original number
    return $sum === $num;
}

$num = 76;
if (isArmstrong(num)) {
      echo "$num is a Armstrong number.";
} else {
      echo "$num is not a Armstrong number.";
}
