const gcd = (a, b) => {
    while (b > 0) {
        [a, b] = [b, a % b]; 
    }
    return a
}
const lcm = (a, b) => a * b / gcd(a, b)

const isCoprimes = (a, b) => gcd(a, b) <= 1

class Node {
    constructor(value, prev=null, next=null){
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}

class LL {
    constructor(){
        this.head = new Node(null);
        this.tail = this.head;
    }

    push(value) {
        this.tail.next = new Node(value, this.tail)
        this.tail = this.tail.next;
    }

    remove(node) {
        if (node.next !== null) {
            node.next.prev = node.prev;
        }
        node.prev.next = node.next;
        node.next = null;
        node.prev = null;
    }
}

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var replaceNonCoprimes = function(nums) {
    const list = new LL();
    for (const num of nums) {
        list.push(num);
    }

    let node = list.head.next;
    console.log("NODE", node.value)
    console.log(gcd(899, 23))

    while (node.next) {
        if (node.prev.value !== null && !isCoprimes(node.value, node.prev.value)) {
            node = node.prev;
            node.value = lcm(node.value, node.next.value);
            list.remove(node.next)
            continue;
        }
        
        if (isCoprimes(node.value, node.next.value)) {
            node = node.next;
        } else {
            node.value = lcm(node.value, node.next.value);
            list.remove(node.next);
        }
    }

    node = list.head.next;
    const answer = []
    while (node) {
        answer.push(node.value);
        node = node.next;
    }

    return answer;
};