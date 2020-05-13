import hashlib, binascii, os

# encodes a provided password in a way that is safe to store in a database
# encode
def hash_password(password):
    """Hash a password for storing."""
    # generates some random salt that should be added to the password, usually hexidecimal
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # pbkdf2_hmac is provided together with the hashed password in a randomized way
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
# When given an encoded password and a plain text one is provided by the user it
# verifies the password is correct
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    # extracts the salt from the hashed password
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    # the extracted salt is then provided to the pbkdf2_hmac to compute their hash
    
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    # and convert to string using binascii.hexlify
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

stored_password = hash_password('ThisIsAPassword')
print(stored_password)
verify_password(stored_password, 'ThisIsAPassWord')
verify_password(stored_password, 'WrongPassword')
                                
