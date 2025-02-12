let condition1= (typeof input1 === "number" && input1>20);
let condition2= (typeof input2 === "boolean" && input2===true);
if (condition1 && condition2) {
    console.log("All conditions are met.")
} else if (condition1 || condition2) {
    console.log("At least one condition is met.")
} else {
    console.log("No conditions are met.")
}
