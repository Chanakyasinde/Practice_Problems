//Write your code here
let Total_monthly_income = parseInt(a);
let Rent = parseInt(b);
let Food_expenses = parseInt(c);
let Transport_expenses = parseInt(d);
let Other_expenses = parseInt(e);

Total_expenses = Rent + Food_expenses + Transport_expenses + Other_expenses
Remaining_Balance = Total_monthly_income - Total_expenses
let result = 20/100*Total_monthly_income

console.log("Total Income:",Total_monthly_income);
console.log("Total Expenses:",Total_expenses);
console.log("Remaining Balance:",Remaining_Balance);
if (result<=Remaining_Balance){
    console.log("You saved well this month!")
} else if (result>=Remaining_Balance && Remaining_Balance>0){
    console.log("Try to save more next month.")
} else {
    console.log("You have overspent!")
}
