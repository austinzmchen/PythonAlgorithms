var fullname = 'John Doe';
var obj = {
   fullname: 'Colin Ihrig',
   prop: {
      fullname: 'Aurelio De Rosa',
      getFullname: function() {
         return this.fullname;
      }
   }
};
console.log(obj.prop.getFullname()); 
 
var test = obj.prop.getFullname; 
console.log(`test: ${test()}`); 

// use call or apply
console.log(test.call(obj.prop));

// use bind
var test0 = obj.prop.getFullname.bind(obj.prop); 
console.log(`test0: ${test0()}`);

var obj2 = {
   fullname: 'Colin Ihrig',
   prop: {
      fullname: 'Aurelio De Rosa',
      // Arrow functions don't have their own this - they inherit this from the surrounding scope where they're defined.
      getFullname: () => {
         return this.fullname;
      }
   }
};

var test2 = obj2.prop.getFullname; 

// Arrow functions capture this from their enclosing scope (lexical scope)
// The object literal obj2 is NOT a scope - it's just an object
// The enclosing scope is the global scope
// In the global scope, this.fullname is undefined (unless you have a global fullname variable)
// Therefore, this.fullname returns undefined
console.log(`test2: ${test2()}`); 