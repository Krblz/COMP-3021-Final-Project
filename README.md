# Assignment #5

## Description

In this assignment. I implemented functions to the chatbot.
And created Unit Tests Functions for each individual error that the chatbot
may come across.

## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions.

- Not knowing that putting an Exception would make Unit Test not be able to raise the Error.
  Because the error doesn't exist anymore. Since it has been excepted in the process.

- That all Errors should only be Raise, and Exception is used to convert one Error into another.

- The Functions are done with an assumption of chaining them together like get_account_number() and
  get_balance() are chained together, so Errors with returns and inputs are fitted together.

- Act and Assert, they can be together. I assumed they didn't but the testFunctions in the Module
  prove it to be false, they can be together if it both Acts and Asserts. Or Asserts then Acts.

### 2. Discuss the benefits and challenges of developing and using unit tests.

- Unit Testing is good practice to make Error Handling be at the end of the overall program. Instead
  of handling them they as appear.

- Unit Testing allows Error handling to be more efficient for the future developer that comes across
  the program. 

- Unit Testing is good for spotting and making sure the Program works correctly.

- Unit Testing is better at documenting and troubleshooting Functions in a program than manually
  changing the function and testing it as it goes. With Unit Testing, the troubleshooting is
  documented and handled better. So in the future, the developer will understand the testing done
  easier.

## Author

Keith Robles