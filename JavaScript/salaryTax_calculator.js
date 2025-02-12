function findTax(salary) {
    switch(true){
        case(salary<=0):
        return "Salary not valid"
        case(salary>0 && salary<=500000):
        return 0
        case(salary>500000 && salary<=1000000):
        return 0.1*salary
        case(salary>1000000 && salary<=1500000):
        return 0.2*salary
        case(salary>1500000):
        return 0.3*salary
    }
}
