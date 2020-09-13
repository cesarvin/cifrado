from Crypto.Cipher import AES
import binascii, os

secretKey = b'N\xc1\xdd\xa5\xf0\xc1\xdd\xfe\x08:\x17\x94I\xbb{\xdd\x0f\x80\xbc\x17\x8fJ\xdf7kz\xee\xd1z\x88\xc1\x87' # 256-bit random encryption key

def encrypt_AES_GCM(msg, secretKey):
  aesCipher = AES.new(secretKey, AES.MODE_GCM)
  ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
  return (ciphertext, aesCipher.nonce, authTag)
  #return ciphertext

def decrypt_AES_GCM(encryptedMsg, secretKey):
  (ciphertext, nonce, authTag) = encryptedMsg
  aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
  plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
  return plaintext

def encryptMainPass(password):
    ecn_pass = encrypt_AES_GCM(password.encode("utf8"), secretKey)
    return ecn_pass

def decryptMainPass(password):
    dec_pass = decrypt_AES_GCM(password, secretKey)
    return dec_pass
