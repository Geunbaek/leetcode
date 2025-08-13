/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (typeof object === 'string') return `"${object}"`
    if (typeof object !== "object" || object === null) return `${object}`;


    if (Array.isArray(object)) {
        const values = object.map(value => {
            if (typeof value === "string") return `"${value}"`
            if (typeof value !== "object" || value === null) return `${value}`;
            return jsonStringify(value)
        })
        return `[${values.join(",")}]`
    }

    const keys = Reflect.ownKeys(object);

    const values = keys.map(key => {
        const value = object[key];
        if (typeof value === "string") return `"${key}":"${value}"`;
        if (typeof value !== "object" || value === null) return `"${key}":${value}`;
        return `"${key}":${jsonStringify(object[key])}`;
    })

    return `{${values.join(",")}}`
};