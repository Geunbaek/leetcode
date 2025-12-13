const isValidCode = (str) => {
    return /^[a-zA-Z0-9_]+$/g.test(str)
}

const isValidBusiness = (str) => {
    return ["electronics", "grocery", "pharmacy", "restaurant"].includes(str)
}

const businessPriorityMap = {"electronics": 1, "grocery": 2, "pharmacy": 3, "restaurant": 4}

/**
 * @param {string[]} code
 * @param {string[]} businessLine
 * @param {boolean[]} isActive
 * @return {string[]}
 */
var validateCoupons = function(code, businessLine, isActive) {
    const n = code.length;
    return Array
            .from({length: n}, (_, i) => ({
                code: code[i], 
                businessLine: businessLine[i], 
                isActive: isActive[i]
            }))
            .filter((coupon) => 
                isValidCode(coupon.code) && 
                isValidBusiness(coupon.businessLine) && 
                coupon.isActive
            )
            .sort((a, b) => 
                businessPriorityMap[a.businessLine] - businessPriorityMap[b.businessLine] || 
                (a.code < b.code ? -1 : (a.code > b.code ? 1 : 0))
            )
            .map(coupon => coupon.code)
};