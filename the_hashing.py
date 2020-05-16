import hashlib

# takes password turns to hash and store in the database
def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# used to verify password when client logs in, takes hash value and compares
def check_pw_hash(password, hash):
    # takes string password typed by user
    # hashes that string compares to string in database
    if make_pw_hash(password) == hash:
        return True
    
    return False
