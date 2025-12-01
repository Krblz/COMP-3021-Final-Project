# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Keith Robles

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning  
Assignment 2: Abstraction, Inheritance, and Polymorphism  
Assignment 3: Design Patterns  
Assignment 4: Programming Paradigms

## Encapsulation
Encapsulation is achieved in BankAccount Class by inputting values into an instance
of the BankAccount Class. The BankAccount Class also correctly checks for Errors and 
messages appropriate statements regarding the Errors.  
BankAccount Class also has methods like Withdraw, Deposit, and Balance that provides
access to the values from inside the Instance.

## Polymorphism
Polymorphism is achieved in ChequingAccount, InvestmentAccount, and SavingsAccount by  
using the BankAccount Class as their Superclass. This allows them to inherit the attributes  
and methods of the Superclass. As a Subclass, they also override the method get_service_charges  
with their own respective changes. Dynamic Binding is observed working through the Tests and  
the AO2_Main where each account made from the Subclasses used the Deposit and Withdraw Method  
from BankAccount Superclass. Each instance is the method invoked depends on the runtime of each  
respective instances created during the program's runtime. 

## Strategy Pattern
Strategy Pattern is used by changing the functionality within of the Child Classes of the BankAccount Classes  
and making it run in the ServiceChargeStrategy Child Classes. This allows for easier implementation of new BankAccount   
Classes while also allowing BankAccount Class to change between Strategies without changing much of the Code.  
The Variables required also being contained in the Strategies allow for easy modification of the Code without drastic changes  
to the BankAccount Classes.

## Observer Pattern
Observer Pattern is used in BankAccount and Client, BankAccount to Allow itself to be Observed and Client to be  
notified when the BankAccount triggers the Observer. But first, the Client Instance must first be attached to   
the BankAccount, this allows the Client to be notified when the balance is updated that triggers the Observer. 
When Triggered, a txt file in the Output Folder shows the Message that would've been sent to the Email of the Client  
that is attached to a BankAccount.  
  
## Event-Driven Programming Paradigm  
The Event-Driven Programming Paradigm is used here to add a functioning User Interface for Clients. There are  
multiple events used ranging from interface buttons to update signals. Event Handlers are connected to events.  
In this application, an example is the Look Up Client Button that sends a Signal to look up the inputted client  
and depending on the user's input, will trigger methods and their functions. Some Events are also based on internal  
updates like the balance update that only triggers when the balance is updated via a transaction done in the interface.  
