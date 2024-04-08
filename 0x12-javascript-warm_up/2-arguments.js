#!/usr/bin/node

// Get command line arguments and remove the first two elements (node and script path)
const args = process.argv.slice(2);

const message = args.length === 0 ? "No argument" : // If no arguments, assign "No argument"
                args.length === 1 ? "Argument found" : // If one argument, assign "Argument found"
                "Arguments found"; // If more than one argument, assign "Arguments found"
                
// Print the message to the console
console.log(message);
