class BankAccount {
  private balance: number;

  constructor(initialBalance: number) {
    if (typeof initialBalance !== "number" || isNaN(initialBalance) || initialBalance < 0) {
      throw new Error("Invalid initial balance");
    }
    this.balance = initialBalance;
  }

  deposit(amount: number): void {
    if (typeof amount !== "number" || isNaN(amount) || amount < 0) {
      console.log("Invalid deposit amount");
      return;
    }
    this.balance += amount;
  }

  withdraw(amount: number): void {
    if (typeof amount !== "number" || isNaN(amount) || amount < 0) {
      console.log("Invalid withdraw amount");
      return;
    }

    if (amount > this.balance) {
      return; // skip silently
    }

    this.balance -= amount;
  }

  getBalance(): number {
    return this.balance;
  }
}
