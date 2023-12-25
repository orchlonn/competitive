// designing stack using array

class Stack {
  constructor() {
    this.arr = [];
  }

  peek = () => this.arr[this.arr.length - 1];

  push(value) {
    this.arr.push(value);
    return this;
  }

  pop() {
    this.arr.length != 0 ? this.arr.pop() : null;
    return this;
  }
}
