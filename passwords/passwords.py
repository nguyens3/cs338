import hashlib
import binascii


def cracked1():
  hashWords = {}
  hash_count = 0
  words = [line.strip().lower() for line in open('words.txt')]
  passwords1 = [line.strip().lower() for line in open('passwords1.txt')]
 
  for word in words:
    encoded_word = word.encode('utf-8')
    hasher = hashlib.sha256(encoded_word)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    hashWords[digest_as_hex_string] = word
    hash_count += 1

  f = open("cracked1.txt" , "w")
  for password in passwords1:
    hash = password.split(":") 
    if hash[1] in hashWords:
        f.write(hash[0]+":"+hashWords[hash[1]]+"\n")
  f.close()
  print(f"Hash: {hash_count}")


def hash(password): 
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8') 
    return digest_as_hex_string

#Credit to Lily and Ashok for telling me to use a dictionary!
def cracked2():
  hash_count = 0
  words = [line.strip().lower() for line in open('words.txt')] 
  f = open("cracked2.txt", "w")
  accounts = [line.strip().split(":") for line in open('passwords2.txt')]
  dict_account = {}
  for user in accounts:
    dict_account[user[1]] = user[0]

    for word in words:
        for word2 in words:
            combination = word + word2
            hashed = hash(combination)
            hash_count += 1
            if(hashed in dict_account):
                f.write(dict_account[hashed] + ":" + combination + "\n")
  print(hash_count)
  f.close()

            
 
def cracked3():
  words = [line.strip().lower() for line in open('words.txt')] 
  hash= {}
  f = open("cracked3.txt", "w")
  passwords = [line.strip() for line in open('passwords3.txt')]
  hash_count = 0
  for account in passwords:
    hash = account.split(':')
    hashed= hash[1].split('$')
    salt = hashed[2]
    password = hashed[3]
    for word in words:
      salted_word = salt + word
      hasher = hashlib.sha256(salted_word.encode('utf-8'))
      digest = binascii.hexlify(hasher.digest())
      digest_string = digest.decode('utf-8')
      hash_count += 1
      if(password == digest_string):
         f.write(hash[0]+":"+word +"\n")
  f.close()
  print("Hash:", hash_count)



def main():
    cracked1()
    cracked2()
    cracked3()

      
if __name__=="__main__":
  main()
