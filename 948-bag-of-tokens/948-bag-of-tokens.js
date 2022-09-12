/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */

class Node{
    constructor(prev, data, next){
        this.prev = prev;
        this.data = data;
        this.next = next;
    }
}
class Deque{
    constructor(){
        this.head = null;
        this.tail = null;
    }
    
    isEmpty(){
        return this.head === null;
    }
    
    enqueue(data){
        if(this.isEmpty()){
            this.head = new Node(null, data, null);
            this.tail = this.head;
        } else {
            const node = new Node(this.tail, data, null);
            this.tail.next = node;
            this.tail = node;
        }
    }
    
    pop(){
        if(this.isEmpty()){
            return;
        } else if (this.head === this.tail){
            const lastNode = this.tail;
            this.head = null;
            this.tail = null;
            return lastNode.data;
        } else {
            const lastNode = this.tail;
            this.tail = this.tail.prev;
            this.tail.next = null;
            return lastNode.data;
        }
    }
    
    popleft(){
        if(this.isEmpty()){
            return;
        } else if (this.head === this.tail){
            const firstNode = this.head;
            this.head = null;
            this.tail = null;
            return firstNode.data;
        } else {
            const firstNode = this.head;
            this.head = this.head.next;
            this.head.prev = null;
            return firstNode.data;
        }
    }
    
    print(){
        let node = this.head;
        while (node){
            console.log(node.data);
            node = node.next
        }
    }
}

var bagOfTokensScore = function(tokens, power) {
    tokens.sort((a, b) => a - b);
    
    const q = new Deque();
    tokens.forEach(token => q.enqueue(token));
    
    const ret = {
        answer: 0,
        score: 0,
        power,
    }
    q.print()
    while(!q.isEmpty()){
        console.log(q.head.data)
        if(ret.power >= q.head.data){
            ret.power -= q.popleft();
            ret.score += 1;
            ret.answer = Math.max(ret.answer, ret.score);
        } else if (ret.score >= 1){
            ret.power += q.pop();
            ret.score -= 1;
        } else {
            return ret.answer;
        }
    }
    
    return ret.answer;
};