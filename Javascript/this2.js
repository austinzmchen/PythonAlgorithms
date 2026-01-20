// The following code will output "my name is rex, Woof!" and then "my name is, Woof!" one second later, fix it so prints correctly the second time

var Dog = function (name) {
  this.name = name;
};

Dog.prototype.bark = function () {
  console.log('my name is '+ this.name + ', Woof!');
}

var rex = new Dog('rex');
rex.bark();

setTimeout(rex.bark, 1000);
// fix
setTimeout(rex.bark.bind(rex), 1000);