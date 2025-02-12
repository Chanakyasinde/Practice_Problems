switch (sign) {
    case "+":
    result = a+b
    break;
    case "-":
    result = a-b
    break;
    case "*":
    result = a*b
    break;
    case "/":
    if (b===0){
        result = "Invalid operation"
    } else{
        result = a/b
    }
    break;
    case "%":
    if (b===0){
        result = "Invalid operation"
    } else{
        result=a%b
    }
    break;
    default:
    result = "Invalid operation"
}
console.log(result)
