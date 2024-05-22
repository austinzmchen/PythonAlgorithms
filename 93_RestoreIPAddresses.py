class Solution_93 {
    fun restoreIpAddresses(s: String): List<String> {
        var res = mutableListOf<String>()
        
        var i = 1
        while (i < 4 && i < s.size - 2) {
            var j = i + 1
            while (j < i + 3 && j < s.size - 1) {
                var k = j + 1
                while (k < j + 3 && k < s.size) {
                    var s1 = s.substring(0, i)
                    var s2 = s.substring(i, j)
                    var s3 = s.substring(j, k)
                    var s4 = s.substring(k, s.size)
                    if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)) {
                        res.add("$s1.$s2.$s3.$s4")
                    }
                    
                    k += 1    
                }
                
                j += 1    
            }
            
            i += 1
        }
        
        return res
    }
 
    fun isValid(str: String) {
        if (str.size > 3 || str.size == 0 || str[0] == '0' || Integer.of(str) > 255) {
            return false
        }
        
        return true
    }
}