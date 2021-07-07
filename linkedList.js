class LinkedList {
    constructor(value){
        this.head= {
            value: value,
            next: null
        }
        this.tail= this.head
        this.length= 1  
    }
    append(value){
        const newNode = {
            value: value,
            next: null
        }
        this.tail.next = newNode
        this.tail = newNode
        this.length += 1
    }
    prepend(value){
        const newNode = {
            value: value,
            next: this.head
        }
        this.head = newNode
        this.length += 1
    }
}
const myList = new LinkedList(10)
myList.append(5)
myList.append(16)
myList.prepend(1)
console.log(myList)