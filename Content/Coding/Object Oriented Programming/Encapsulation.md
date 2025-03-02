# Encapsulation in OOP

![oopPillars.png](Resources/oopPillars.png)

Encapsulation is a fundamental principle in object-oriented programming (OOP) that protects an object's internal state from unauthorized access and modification. By bundling data and methods together, encapsulation ensures that an object’s internal representation is hidden from the outside, exposing only a controlled interface for interaction.

## What is Encapsulation?

Encapsulation involves hiding the internal details of a class while exposing only what is necessary through a public interface. This helps safeguard the data by ensuring that any changes to an object’s state occur only through well-defined methods. In essence, encapsulation separates the “how” (the internal workings) from the “what” (the external behavior).

[Wikipedia](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))

## Benefits of Encapsulation

- **Data Protection:** Prevents direct access to an object’s internal variables, reducing the risk of accidental or malicious changes.
- **Modularity:** Creates a clear separation between an object’s interface and its implementation, making the code easier to maintain.
- **Flexibility:** Allows the internal implementation to change without affecting external code that relies on the public interface.
- **Maintainability:** Encourages controlled interaction with object data through getter and setter methods, ensuring consistency and integrity.

## Example

Imagine you are developing a banking application. A `BankAccount` class manages sensitive data like the account balance. Encapsulation ensures that the balance can only be modified through dedicated methods, thus preventing improper access.

```java
public class BankAccount {
    // Private variable: cannot be accessed directly from outside the class
    private double balance;

    // Constructor to initialize the account with an initial balance
    public BankAccount(double initialBalance) {
        balance = initialBalance;
    }

    // Public method to deposit money: modifies the balance in a controlled way
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    // Public method to withdraw money: ensures balance remains valid
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }

    // Public method to retrieve the current balance
    public double getBalance() {
        return balance;
    }
}
```
In this example, the balance variable is declared as private, so it cannot be accessed or modified directly from outside the class. Instead, external code must use the public methods deposit(), withdraw(), and getBalance(). This controlled access ensures that the balance is updated only under appropriate conditions, preserving the integrity of the account data.

## More
Encapsulation not only enhances security by preventing unauthorized data access but also promotes a cleaner design by separating the internal workings of a class from its public interface. This approach aligns with the Single Responsibility Principle, ensuring that each class has a clear and focused role. As a result, encapsulated code is generally easier to debug, test, and maintain.

By using encapsulation, developers can create robust and scalable applications where internal implementation details can change without impacting the overall system, provided the public interface remains consistent.
