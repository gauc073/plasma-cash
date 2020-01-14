import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""

authority_address = "0xd7b02e3bdf2eddbb5793d4728eafa83ec8c07d0b"
authority_key = "0x740b220f156da692ead7d9e7a1b281534cb90f6821f36628485f1d5a05056be9"
"""
plasma_config = dict(
    ROOT_CHAIN_CONTRACT_ADDRESS='0xF273BD6B87138C610aAB70FaD7DEc71F73F10ed7',
    AUTHORITY=b'\xd7\xb0.;\xdf.\xdd\xbbW\x93\xd4r\x8e\xaf\xa8>\xc8\xc0}\x0b',
    AUTHORITY_KEY=b't\x0b"\x0f\x15m\xa6\x92\xea\xd7\xd9\xe7\xa1\xb2\x81SL\xb9\x0fh!\xf3f(H_\x1dZ\x05\x05k\xe9',
)


db_config = {
    'type': 'leveldb' # | 'memory' # (required)
    # 'path': '' (optional, if nor specific set, would have default path)
}
"""
db_config = {
    'type': 'memory'
}
"""