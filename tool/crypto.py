import bcrypt
import base64

PASSWORD = 'password'
SECRET_KEY = 'mySecret'
ENCODE_TYPE = 'utf-8'
# ALGORITHM = 'HS256'

# hash encoding (type: bytes)
def encodeHash(password):
    hashed_password = bcrypt.hashpw(password.encode(ENCODE_TYPE), bcrypt.gensalt())

    return hashed_password

# hash decoding (type: str)
def decodeHash(hashed_password):
    decoded_password = hashed_password.decode(ENCODE_TYPE)

    return decoded_password

# validate hash password (type: bytes)
def validateHash(password, hashed_password):
    result = bcrypt.checkpw(password.encode(ENCODE_TYPE), hashed_password)

    return result

# encrypt base64
def encryptBase(password, salt):
    password = password + salt
    encode_password = password.encode(ENCODE_TYPE)
    encoded = base64.b64encode(encode_password)

    return encoded

# decrypt
def decryptBase(encoded, salt):
    decoded = base64.b64decode(encoded)
    decode_password = decoded.decode(ENCODE_TYPE)
    decode_password = decode_password.replace(salt, "")
    
    return decode_password

# validate
def validateBase(password, decode_password):
    return password == decode_password