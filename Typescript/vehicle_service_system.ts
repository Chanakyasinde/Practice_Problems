interface Vehicle {
  serviceDetails(): void;
}

class Car {
    model: string;
    constructor(model: string) {
        this.model = model
    }
    serviceDetails(): void {
        console.log(`Car model ${this.model} requires regular servicing`)
    }
}

class Bike {
    engineCC: number
    constructor(engineCC: number) {
        this.engineCC = engineCC
    }
    serviceDetails(): void {
        console.log(`Bike with ${this.engineCC}cc engine requires oil change`)
    }
}

class Truck {
    capacity: number
    constructor(capacity: number){
        this.capacity = capacity
    }
    serviceDetails(): void {
        console.log(`Truck with capacity ${this.capacity} tons requires heavy maintenance`)
    }
}
