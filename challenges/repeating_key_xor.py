import base64
import binascii
from utilities import util

# Challenge 5

if __name__ == '__main__':
  c = util.repeating_key_xor(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", b'ICE')
  print(binascii.hexlify(c))

