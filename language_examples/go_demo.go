// Go Demo
package main

import (
	"fmt"
	"time"
)

// Variables and Types
var message string = "Hello, Go!"
var count int = 42
var isTrue bool = true

// Arrays/Slices
var fruits = []string{"apple", "banana", "cherry"}

// Functions
func greet(name string) string {
	return "Hello, " + name + "!"
}

// Structs
type Person struct {
	Name string
	Age  int
}

var person = Person{
	Name: "John",
	Age:  30,
}

type Animal struct {
	Name string
}

func (a Animal) Speak() {
	fmt.Printf("%s makes a sound.\n", a.Name)
}

var cat = Animal{"Cat"}

// cat.Speak() // Uncomment this line to make the cat speak

// Template Strings
var templateString = fmt.Sprintf("The count is %d, and the message is: %s", count, message)

// Loops
func printFruits() {
	for _, fruit := range fruits {
		fmt.Println(fruit)
	}
}

// Anonymous Functions (Closures)
func add(a, b int) int {
	return a + b
}

// Type Assertion (Type Conversion)
func typeAssertion(value interface{}) int {
	if val, ok := value.(int); ok {
		return val
	}
	return 0
}

// Generics (No direct support for generics, use interfaces)
type Identity interface {
	identity() string
}

type StringIdentity string

func (s StringIdentity) identity() string {
	return string(s)
}

// Goroutines and Channels (Concurrency)
func printNumbers() {
	for i := 1; i <= 5; i++ {
		fmt.Printf("%d ", i)
	}
}

func printLetters() {
	for letter := 'a'; letter <= 'e'; letter++ {
		fmt.Printf("%c ", letter)
	}
}

// Error Handling
func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("cannot divide by zero")
	}
	return a / b, nil
}

// Pointers
func increment(x *int) {
	*x++
}

// Maps
var fruitColors = map[string]string{
	"apple":  "green",
	"banana": "yellow",
	"cherry": "red",
}

// Switch Statement
func evaluateNumber(num int) string {
	switch {
	case num < 0:
		return "negative"
	case num > 0:
		return "positive"
	default:
		return "zero"
	}
}

// Defer, Panic, and Recover
func safeDivide(a, b int) (result int) {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("Recovered from panic:", err)
			result = 0
		}
	}()

	if b == 0 {
		panic("cannot divide by zero")
	}
	return a / b
}

func main() {
	// Conditional Statements
	if isTrue {
		fmt.Println("It's true!")
	} else {
		fmt.Println("It's false!")
	}

	// Call identity function
	result := StringIdentity("Hello, Generics!").identity()
	fmt.Println(result)

	// Start goroutines
	go printNumbers()
	go printLetters()

	// Sleep to allow goroutines to finish
	time.Sleep(time.Second)

	// Error Handling
	_, err := divide(10, 0)
	if err != nil {
		fmt.Println(err)
	}

	// Pointers
	num := 10
	increment(&num)
	fmt.Println(num) // Should print 11

	const test = "test"

	// Maps
	fmt.Println(fruitColors)

	// Switch Statement
	fmt.Println(evaluateNumber(10)) // Should print "positive"

	// Defer, Panic, and Recover
	fmt.Println(safeDivide(10, 0)) // Should print "Recovered from panic: cannot divide by zero" and 0
}
