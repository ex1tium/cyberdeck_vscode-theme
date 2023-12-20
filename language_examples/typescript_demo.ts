// TypeScript Demo

// Variables and Types
let message: string = "Hello, TypeScript!";
const count: number = 42;
const isTrue: boolean = true;

// Arrays
const fruits: string[] = ["apple", "banana", "cherry"];

// Functions
function greet(name: string): string {
  return `Hello, ${name}!`;
}

// Objects
interface Person {
  name: string;
  age: number;
}

const person: Person = {
  name: "John",
  age: 30,
};

// Classes
class Animal {
  constructor(public name: string) {}

  speak(): void {
    console.log(`${this.name} makes a sound.`);
  }
}

const cat = new Animal("Cat");
cat.speak();

// Template Literals
const templateString = `The count is ${count}, and the message is: ${message}`;

// Conditional Statements
if (isTrue) {
  console.log("It's true!");
} else {
  console.log("It's false!");
}

// Loops
for (const fruit of fruits) {
  console.log(fruit);
}

// Arrow Functions
const add = (a: number, b: number): number => a + b;

// Type Assertions
const value: any = "123";
const numericValue: number = Number(value);

// Generics
function identity<T>(arg: T): T {
  return arg;
}

const map = new Map<number, Map<string, number>>();

const result = identity<string>("Hello, Generics!");

// Promises
async function fetchData(): Promise<string> {
  const response = await fetch("https://example.com/data");
  const data = await response.text();
  return data;
}

fetchData().then((data) => console.log(data));

// Nullish Coalescing
const defaultValue = "Default Value";
const userInput = null;
const finalValue = userInput ?? defaultValue;

console.log(finalValue);
// Private Class Fields (TypeScript 3.8)
class Example {
  #privateField: string;

  constructor() {
    this.#privateField = "Hello, Private!";
  }

  getPrivateField() {
    return this.#privateField;
  }
}
const example = new Example();
console.log(example.getPrivateField());
// Optional Chaining (TypeScript 3.7)
const user = {
  id: 123,
  info: {
    name: "John",
    address: {
      street: "123 Main St",
      city: "Anytown",
    },
  },
};

console.log(user.info?.address?.city);

// Nullish Coalescing (TypeScript 3.7)
const input = undefined;
const output = input ?? "default";
console.log(output);
