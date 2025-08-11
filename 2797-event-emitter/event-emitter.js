class EventEmitter {
    constructor(){
        this.cache = new Map()
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.cache.has(eventName)) {
            this.cache.set(eventName, new Set());
        }
        const callbacks = this.cache.get(eventName);
        callbacks.add(callback)
        return {
            unsubscribe: () => {
                callbacks.delete(callback)
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const callbacks = this.cache.get(eventName) || new Set();
        return [...callbacks].map(callback => callback(...args))
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */