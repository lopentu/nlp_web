/* Revised from Flanagan, David. JavaScript: The Definitive Guide. O'Reilly Media. 7th Edition.
 */

//--------------------
// A variable is a symbolic name for a value. The value can be changed.
// e.g, variables declared with the let keyword:
let x; // Declare a variable named x.

// Values can be assigned to variables with an = sign
x = 0; // Now the variable x has the value 0
x; // => 0: A variable evaluates to its value.

// JavaScript supports several types of values
x = 1; // Numbers.
x = 0.01; // Numbers can be integers or reals.
x = "hello world"; // Strings of text in quotation marks.
x = "JavaScript"; // Single quote marks also delimit strings.
x = true; // A Boolean value.
x = false; // The other Boolean value.
x = null; // Null is a special value that means "no value."
x = undefined; // Undefined is another special value like null. It means a variable has been declared but has no value.

//----------------
// JavaScript's most important datatype is the object.
// An object is a collection of name/value pairs
let book = {
  // Objects are enclosed in curly braces.
  topic: "JavaScript", // The property "topic" has value "JavaScript."
  edition: 7, // The property "edition" has value 7
}; // The curly brace marks the end of the object.

// Access the properties of an object with . or []:
book.topic; // => "JavaScript"
book["edition"]; // => 7: another way to access property values.
book.author = "Flanagan"; // Create new properties by assignment.
book.contents = {}; // {} is an empty object with no properties.

// Conditionally access properties with ?. (ES2020):
book.contents?.ch01?.sect1; // => undefined: book.contents has no ch01 property.

// JavaScript also supports arrays (numerically indexed lists) of values:
let primes = [2, 3, 5, 7]; // An array of 4 values, delimited with [ and ].
primes[0]; // => 2: the first element (index 0) of the array.
primes.length; // => 4: how many elements in the array.
primes[primes.length - 1]; // => 7: the last element of the array.
primes[4] = 9; // Add a new element by assignment.
primes[4] = 11; // Or alter an existing element by assignment.
let empty = []; // [] is an empty array with no elements.
empty.length; // => 0

// Arrays and objects can hold other arrays and objects:

let points = [
  // An array with 2 elements.
  { x: 0, y: 0 }, // Each element is an object.
  { x: 1, y: 1 },
];

let data = {
  // An object with 2 properties: trial1 and trial2
  trial1: [
    [1, 2],
    [3, 4],
  ], // The value of each property is an array.
  trial2: [
    [2, 3],
    [4, 5],
  ], // The elements of the arrays are arrays.
};

// Expression and Statement
// expressions are evaluated to produce a value; statements are executed for their side effects (such as control flow, variable declarations, iterations, etc).
// e.g., 1 + 2 is an expression that evaluates to 3; the assignment statement x = 3 is a statement that assigns the value 3 to the variable x.

// One of the most common ways to form expressions is to use operators.
// Operators act on values (the operands) to produce a new value.
// Arithmetic operators are some of the simplest:

3 + 2; // => 5: addition
3 - 2; // => 1: subtraction
3 * 2; // => 6: multiplication
3 / 2; // => 1.5: division

// JavaScript defines some shorthand arithmetic operators
let count = 0; // Define a variable
count++; // Increment the variable
count--; // Decrement the variable
count += 2; // Add 2: same as count = count + 2;
count *= 3; // Multiply by 3: same as count = count * 3;
count; // => 6: variable names are expressions, too.

// Equality and relational operators test whether two values are equal,
// unequal, less than, greater than, and so on. They evaluate to true or false.
// type coercion: JavaScript converts values from one type to another as needed. e.g, 1 == "1" is true because JavaScript converts the string "1" to the number 1 before comparing them.
// ===: strict equality operator, which does not perform type coercion.

let x = 2, y = 3; // These = signs are assignment, not equality tests
x === y; // => false: equality. Note:  === is strict equality, which checks both value and type.
x !== y; // => true: inequality
x < y; // => true: less-than
x <= y; // => true: less-than or equal
x > y; // => false: greater-than
x >= y; // => false: greater-than or equal
"two" === "three"; // => false: the two strings are different
"two" > "three"; // => true: "tw" is alphabetically greater than "th"
(false ===  (x > y)    // => true: false is equal to false

// Logical operators combine or invert boolean values
(x === 2 ) && (y === 3) // => true: both comparisons are true. && is AND
(x  > 3 ) || (y < 3);   // => false: neither comparison is true. || is OR
!(x === y); // => true: ! inverts a boolean value



// Functions are parameterized blocks of JavaScript code that we can invoke.

function plus1(x) {
                // Define a function named "plus1" with parameter "x"
  return x + 1; // Return a value one larger than the value passed in
}               // Functions are enclosed in curly braces

plus1(y); // => 4: y is 3, so this invocation returns 3+1


// Functions are values and can be assigned to vars
let square = function (x) {
  return x * x; // Compute the function's value
}; // Semicolon marks the end of the assignment.

square(plus1(y)); // => 16: invoke two functions in one expression


// In ES6 and later, we can use the concise syntax for defining functions
// it uses => instead of the function keyword, to separate the argument list from the function body.(arrow function)
// If the function has a single argument, we can omit the parentheses around the argument list.


const plus1 = (x) => x + 1; // The input x maps to the output x + 1
const square = x => x * x; // The input x maps to the output x * x
plus1(y); // => 4: function invocation is the same
square(plus1(y)); // => 16


// When functions are assigned to the properties of an object, we call
// them "methods."  All JavaScript objects (including arrays) have methods:
let a = []; // Create an empty array
a.push(1, 2, 3); // The push() method adds elements to an array
a.reverse(); // Another method: reverse the order of elements

// We can define our own methods, too. The "this" keyword refers to the object
// on which the method is defined: in this case, the points array from earlier.
points.dist = function () {
  // Define a method to compute distance between points
  let p1 = this[0]; // First element of array we're invoked on
  let p2 = this[1]; // Second element of the "this" object
  let a = p2.x - p1.x; // Difference in x coordinates
  let b = p2.y - p1.y; // Difference in y coordinates
  return Math.sqrt(
    a * a + // The Pythagorean theorem
      b * b
  ); // Math.sqrt() computes the square root
};
points.dist(); // => Math.sqrt(2): distance between our 2 points

// JavaScript statements include conditionals and loops using the syntax
// of C, C++, Java, and other languages.
function abs(x) {
  // A function to compute the absolute value.
  if (x >= 0) {
    // The if statement...
    return x; // executes this code if the comparison is true.
  } // This is the end of the if clause.
  else {
    // The optional else clause executes its code if
    return -x; // the comparison is false.
  } // Curly braces optional when 1 statement per clause.
} 
// Note return statements nested inside if/else.
abs(-10) === abs(10); // => true


function sum(array) {
  // Compute the sum of the elements of an array
  let sum = 0; // Start with an initial sum of 0.
  for (let x of array) {
    // Loop over array, assigning each element to x.
    sum += x; // Add the element value to the sum.
  } // This is the end of the loop.
  return sum; // Return the sum.
}
sum(primes); // => 28: sum of the first 5 primes 2+3+5+7+11

function factorial(n) {
  // A function to compute factorials
  let product = 1; // Start with a product of 1
  while (n > 1) {
    // Repeat statements in {} while expr in () is true
    product *= n; // Shortcut for product = product * n;
    n--; // Shortcut for n = n - 1
  } // End of loop
  return product; // Return the product
}
factorial(4); // => 24: 1*4*3*2


function factorial2(n) {
  // Another version using a different loop
  let i,
    product = 1; // Start with 1
  for (
    i = 2;
    i <= n;
    i++ // Automatically increment i from 2 up to n
  )
    product *= i; // Do this each time. {} not needed for 1-line loops
  return product; // Return the factorial
}
factorial2(5); // => 120: 1*2*3*4*5

// Class is a new feature in ES6. They are syntactic sugar over the prototype-based OO pattern.
// They support prototype-based inheritance, super calls, instance and static methods and constructors.

class Point {
  // By convention, class names are capitalized.
  constructor(x, y) {
    // Constructor function to initialize new instances.
    this.x = x; // This keyword is the new object being initialized.
    this.y = y; // Store function arguments as object properties.
  } // No return is necessary in constructor functions.

  distance() {
    // Method to compute distance from origin to point.
    return Math.sqrt(
      // Return the square root of x² + y².
      this.x * this.x + // this refers to the Point object on which
        this.y * this.y // the distance method is invoked.
    );
  }
}

// Use the Point() constructor function with "new" to create Point objects
let p = new Point(1, 1); // The geometric point (1,1).

// Now use a method of the Point object p
p.distance(); // => Math.SQRT2
