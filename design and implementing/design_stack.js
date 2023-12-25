// designing stack using linked list

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.bottom = null;
    this.top = null;
    this.length = 0;
  }

  peek() {
    return this.top;
  }

  push(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.top = newNode;
      this.bottom = newNode;
    } else {
      const holdingPointers = this.top;
      this.top = newNode;
      this.top.next = holdingPointers;
    }

    this.length += 1;
  }

  pop() {
    if (this.lenght === 0) {
      return null;
    }

    if (this.top === this.bottom) {
      this.bottom = none;
    }

    this.top = this.top.next;

    this.length -= 1;
  }
}
