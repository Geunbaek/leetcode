/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const n = functions.length;
        let successCount = 0;
        const successes = new Array(n).fill(null)

        for (let i = 0; i < n; i ++) {
            functions[i]()
                .then((result) => {
                    successes[i] = result;
                    successCount += 1;

                    if (successCount === n) {
                        resolve(successes)
                    }
                }).catch(e => {
                    reject(e)
                });
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */