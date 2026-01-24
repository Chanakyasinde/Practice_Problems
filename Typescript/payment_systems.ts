interface PaymentGateway {
  pay(amount: number): boolean;
}

class PaytmGateway implements PaymentGateway {
    pay(amount: number): boolean {
        console.log(`[PayTM] Paying Rs${amount}`)
        return true
    }
}

class UPIGateway implements PaymentGateway {
    pay(amount: number): boolean {
        console.log(`[UPI] Paying Rs${amount}`);
        return true
    }
}

class CreditCardGateway implements PaymentGateway {
    pay(amount: number): boolean {
        console.log(`[CreditCard] Paying Rs${amount}`);
        return true
    }
}

class PaymentService implements PaymentGateway {
    gateway: PaymentGateway;

    constructor(gateway: PaymentGateway) {
        this.gateway = gateway
    }

    setGateway(g: PaymentGateway): void {
        this.gateway = g
    }

    makePayment(amount: number): void {
        this.gateway.pay(amount)
    }
    pay(amount: number): boolean {
        return true
    }
}
