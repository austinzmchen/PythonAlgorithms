import hashlib

class Base62Hash:
    """Base62 encoding for hash-based URL shortening"""
    
    CHARSET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    @staticmethod
    def encode_number(num):
        """Convert integer to base62 string"""
        if num == 0:
            return Base62Hash.CHARSET[0]
        
        result = ''
        while num:
            result = Base62Hash.CHARSET[num % 62] + result
            num //= 62
        return result
    
    @staticmethod
    def decode_number(encoded):
        """Convert base62 string back to integer"""
        num = 0
        for char in encoded:
            num = num * 62 + Base62Hash.CHARSET.index(char)
        return num
    
    # hashing is lossy, result is truncated, 
    # the collision rate is high for the `text` input that can be anything
    @staticmethod
    def hash_to_base62(text, length=6, algorithm='md5'):
        """
        Convert text to short base62 hash
        
        Args:
            text: Input string to hash
            length: Desired output length (default 6)
            algorithm: Hash algorithm ('md5', 'sha256', etc.)
        
        Returns:
            Base62 encoded hash string
        """
        # Create hash
        if algorithm == 'md5':
            hash_obj = hashlib.md5(text.encode('utf-8'))
        elif algorithm == 'sha256':
            hash_obj = hashlib.sha256(text.encode('utf-8'))
        else:
            hash_obj = hashlib.new(algorithm, text.encode('utf-8'))
        
        # Convert hash bytes to integer
        hash_int = int.from_bytes(hash_obj.digest(), byteorder='big')
        
        # Encode to base62
        encoded = Base62Hash.encode_number(hash_int)
        
        # Truncate to desired length
        return encoded[:length]
    
    @staticmethod
    def hash_bytes_to_base62(hash_bytes, length=6):
        """
        Convert raw hash bytes to base62
        Useful when you already have the hash
        """
        hash_int = int.from_bytes(hash_bytes, byteorder='big')
        encoded = Base62Hash.encode_number(hash_int)
        return encoded[:length]


# Example usage
def shorten_url(url, length=6):
    """Generate short code for URL"""
    return Base62Hash.hash_to_base62(url, length)


# Demo
if __name__ == "__main__":
    # Test URLs
    urls = [
        "https://example.com/very/long/path/to/resource",
        "https://github.com/user/repository/issues/12345",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        "https://www.google.ca/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.linguaframe.com%2Fes%2Fhow-to-say-hello.html&ved=0CBkQjhxqFwoTCNCP1OnrwpEDFQAAAAAdAAAAABAe&opi=89978449"
    ]
    
    print("URL Shortening Examples:\n")
    for url in urls:
        short_code = shorten_url(url, length=6)
        print(f"Original: {url}")
        print(f"Short code: {short_code}")
        print(f"Short URL: https://short.link/{short_code}\n")
    
    print("\n" + "="*50)
    print("Base62 Number Encoding Examples:\n")
    
    # Test number encoding/decoding
    numbers = [123, 12345, 999999]
    for num in numbers:
        encoded = Base62Hash.encode_number(num)
        decoded = Base62Hash.decode_number(encoded)
        print(f"Number: {num} -> Base62: {encoded} -> Decoded: {decoded}")
    
    print("\n" + "="*50)
    print("Collision Testing (same URL):\n")
    
    # Same URL should always produce same hash
    url = "https://example.com/page"
    for i in range(3):
        print(f"Attempt {i+1}: {shorten_url(url)}")
    
    print("\n" + "="*50)