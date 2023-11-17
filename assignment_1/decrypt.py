# %%
import os
from pathlib import Path

print(os.path.abspath(__file__))

# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__)
# PRIVATE_KEY_FILE = PROJECT_FOLDER / "ceu_key"
# PUBLIC_KEY_FILE = PROJECT_FOLDER / "ceu_key.pub"

# assert Path.exists(PRIVATE_KEY_FILE)
# assert Path.exists(PUBLIC_KEY_FILE)
print(__file__)
print(PROJECT_FOLDER)
# %%
