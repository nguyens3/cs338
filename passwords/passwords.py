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

    




def main():
    cracked1()

      
if __name__=="__main__":
  main()
