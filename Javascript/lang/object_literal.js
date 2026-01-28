// Method shorthand (ES6+, modern)
const personProto = {
  greet() {
    return `Hi, I'm ${this.name}`;
  }
};

// Traditional way (with function keyword)
const personProto = {
  greet: function() {
    return `Hi, I'm ${this.name}`;
  }
};

// Arrow function (different `this` binding)
const personProto = {
  greet: () => {
    return `Hi, I'm ${this.name}`;
  }
};