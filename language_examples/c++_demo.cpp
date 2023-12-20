#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <algorithm>
#include <stdexcept>

// Define a simple class
class Animal {
public:
    Animal(const std::string& name) : name(name) {}
    void speak() const {
        std::cout << name << " says hello!" << std::endl;
    }
private:
    std::string name;
};

// Function demonstrating templates
template <typename T>
T max(T x, T y) {
    return (x > y) ? x : y;
}

// Inheritance and Polymorphism
class Shape {
public:
    virtual void draw() const = 0; // Pure virtual function
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a Circle." << std::endl;
    }
};

class Square : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a Square." << std::endl;
    }
};

// Exception Handling
void mightGoWrong() {
    bool errorOccurred = true; // Simulate an error
    if (errorOccurred) {
        throw std::runtime_error("Something went wrong!");
    }
}

// Smart Pointers
void useSmartPointer() {
    std::unique_ptr<int> p(new int);
    *p = 7;
    std::cout << "Smart Pointer value: " << *p << std::endl;
}

int main() {
    // Basic input/output
    std::cout << "C++ Demo File" << std::endl;

    // Variables and data types
    int number = 10;
    double pi = 3.14159;
    std::string message = "Hello, C++!";

    // Control structures
    if (number > 5) {
        std::cout << "Number is greater than 5" << std::endl;
    }

    // Loops
    for (int i = 0; i < number; ++i) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // Using STL containers
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    for (auto num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Working with custom classes
    Animal cat("Whiskers");
    cat.speak();

    // Using templates
    std::cout << "Max of 4 and 7 is " << max(4, 7) << std::endl;
    std::cout << "Max of 3.5 and 2.5 is " << max(3.5, 2.5) << std::endl;

    // Polymorphism
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>());
    shapes.push_back(std::make_unique<Square>());

    for (const auto& shape : shapes) {
        shape->draw();
    }

    // Exception Handling
    try {
        mightGoWrong();
    } catch (const std::exception& e) {
        std::cerr << "Caught Exception: " << e.what() << std::endl;
    }

    // Lambda Expressions and STL Algorithms
    std::for_each(numbers.begin(), numbers.end(), [](int val) {
        std::cout << val << " ";
    });
    std::cout << std::endl;

    // Smart Pointers
    useSmartPointer();

    return 0;
}
