# Python 3 code to demonstrate the working of hmac module.
# Running - python3 HMAC.py

import hmac
import hashlib

# creating new hmac object using sha1 hash algorithm
digest_maker = hmac.new(b'secret-key', b'msg', hashlib.sha1)

# print the Hexdigest of the bytes passed to update
print ("Hexdigest: " + digest_maker.hexdigest())

# call update to update msg
digest_maker.update(b'another msg')

# print the Hexdigest of the bytes passed to update
print ("Hexdigest after update: " + digest_maker.hexdigest())

print ("Digest size: " + str(digest_maker.digest_size) + " bytes")
print ("Block size: " + str(digest_maker.block_size) + " bytes")
print ("Canonical name: " + digest_maker.name)

# print the digest of the bytes passed to update
print ("Digest: ", end =" ")
print (digest_maker.digest())

# create a copy of the hmac object
digest_clone = digest_maker.copy()
print ("Hexdigest of clone: " + digest_clone.hexdigest())
