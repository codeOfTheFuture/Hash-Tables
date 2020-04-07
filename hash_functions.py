# What is a hash function and how does it work?

# Deterministic: For a given input, the output will always be the same.j

# Defined output range: For a hash table of size 16, all keys must hash to a value 0-15.

# Predictable Speed: Hash functions for hash tables should be lighting fast while cryptographic hashes (like bcrypt) should be very slow.

# Non-invertible: You should not be able to reconstruct the input value from the output. This trait is important in cryptographic hashes but not necessary for general hash tables.

