// Your code here
let discount_Amount=(originalPrice*discountPercentage) / 100;
let finalPrice = originalPrice - discount_Amount;

console.log("Original Price:",originalPrice);
console.log("Discount Amount:",discount_Amount);
console.log("Final Price:",finalPrice);
if (discountPercentage > 50){
    console.log("Great Deal!")
}
