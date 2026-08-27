let bedrooms = 3;

if (bedrooms > 2) {
    console.log("Large house");
    console.warn("Price: $500,000");
    console.error("Error: Price not available");
} else {
    console.log("Small house");
}

let arr = [{ name: "Maths", score: 3 }, { name: "Programming", score: 9 }, { name: "English", score: 5 }, { name: "Politics", score: 10 }];
let sum = 0;
let max = 0;

for (let i = 0; i < arr.length; i++) {
    sum += arr[i].score;
    if (arr[i].score > 8) {
        console.log("Subject with score > 8: " + arr[i].name);
    }
    if (arr[i].score > max) {
        max = arr[i].score;
    }
}

console.log("Sum of scores: " + sum);
console.log("Maximum score: " + max);
