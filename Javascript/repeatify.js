
String.prototype.repeatify = function repeatify(i) {
	_str = ""
	for (j = 0; j < i; j++) {
		_str += this
	}
	return _str
}

console.log('hello'.repeatify(3));
//Should print hellohellohello.