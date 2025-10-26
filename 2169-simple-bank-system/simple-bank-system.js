/**
 * @param {number[]} balance
 */
var Bank = function(balance) {
    this.balances = [null, ...balance];
    this.size = balance.length;
};

/** 
 * @param {number} account
 * @return {boolean}
 */
Bank.prototype.isValidAccount = function(account) {
    return 0 <= account && account <= this.size;
};

/** 
 * @param {number} account
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.hasEnoughBalance = function(account, money) {
    return this.balances[account] >= money;
};


/** 
 * @param {number} account1 
 * @param {number} account2 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.transfer = function(account1, account2, money) {
    if (!(this.isValidAccount(account1) && this.isValidAccount(account2))) return false;
    if (!this.hasEnoughBalance(account1, money)) return false;

    this.balances[account1] -= money;
    this.balances[account2] += money;

    return true;
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.deposit = function(account, money) {
    if (!this.isValidAccount(account)) return false;
    this.balances[account] += money;
    return true;
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.withdraw = function(account, money) {
    if (!this.isValidAccount(account)) return false;
    if (!this.hasEnoughBalance(account, money)) return false;
    this.balances[account] -= money;
    return true;
};

/** 
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */