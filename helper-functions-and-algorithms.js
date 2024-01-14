/* Convert Kilometers to miles */
const kmToMiles = (kilo) => {
  /* Conversion */
  let conversion_factor = 0.6211371;
  let miles = kilo * conversion_factor;
  return (
    kilo + " kilometers is equal to " + miles + " miles"
  )
}

// console.log(kmToMiles(2));

/* Convert Celsius to fahrenheit */
const celToFahr = (celsius) => {
  return celsius + " degrees Celsius is equal to " + ((celsius * 9/5) + 32) + " degree Fahrenheit" 
}

// console.log(celToFahr(100))

// Solve quadratic equation
const quadratic = (a, b, c) => {
  let discriminant = b**2 - 4*a*c;
  if (discriminant > 0) {
    return "root 1: " + ((-b + Math.pow(discriminant)) / (2*a)) + " root 2: " + ((-b - Math.pow(discriminant)) / (2*a));
  } else if (discriminant == 0) {
    return "Root: " + (-b / (2*a));
  } else {
    return "Root 1: " + (-b / (2*a)) + " + " + (Math.pow(Math.abs(discriminant), 2) / (2*a), 2) + "i Root2: " + (-b / (2*a)) + " - " + (Math.pow(Math.abs(discriminant)) / (2*a), 2) + "i"; 
  }
}

// console.log(quadratic(1, 4, 8))

// Check if leap year
const leapYearCheck = (year) => {
  if (year % 400 === 0 && year % 100 === 0){
    return year + " is a leap year"
  } else if (year % 4 === 0 && year % 100 != 0) {
    return year + " is a leap year"
  } else {
    return year + " is not a leap year"
  }
}

// console.log(leapYearCheck(2024))

// Check prime number
const primeCheck = (num) => {
  let is_prime;
    if (num===1){is_prime = false}
    else if (num===2||num===3){is_prime = true}
    else if (num%2===0){is_prime = false}
    else{
        let x = Math.floor(num/2);
        while (x>1){
            if (num%x===0){
                is_prime = false;
                break;
            }
            x = x-1;
            is_prime = true;
        }
    }
    
    return is_prime
}

// console.log(primeCheck(5))

// Print the fibonacci sequence
const fibonacciSeq = (num) => {
  let fib = [0, 1];

  if (num <= 0){
    return " must be a positive integer"
  } else {
    for (i = 1; i < num; i++) {
      fib.push(fib[i] + fib[i - 1]);
    }
  }

  return fib;
}

// console.log(fibonacciSeq(10))

//Check for Armstrong number
const armstrongCheck = (num) => {
  let num_str = toString(num);
  let num_digits = num_str.length;

  let sum_of_powers = 0;
  let temp_num = num;

  while(temp_num > 0){
    digit = temp_num % 10;
    sum_of_powers += digit ** num_digits
    temp_num /= 10
  }

  if (sum_of_powers == num ){
    return num + " is a Armstrong number"
  } else {
    return num + " is not a Armstrong number"
  }
}

// console.log(armstrongCheck(153))
