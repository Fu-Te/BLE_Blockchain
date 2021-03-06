import hashlib

class Block:
    
    def __init__(self, index, timestamp, transactions, previous_hash, public_key):
        self.publick_key = public_key
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.gen_hashed_block()
        
    def gen_hashed_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.index)+str(self.timestamp)+str(self.transactions)+str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
    
    def validate_private_key(self, private_key):
        pub_key = self.publick_key
        sha = hashlib.sha256()
        sha.update(str(private_key).encode('utf-8'))
        hash_key = sha.hexdigest()
        return hash_key == pub_key
    
    def disp_block_info(self):
        print(f'Index: {self.index}')
        print(f'Timestanp: {self.timestamp}')
        print(f'Public Key: {self.publick_key}')
        
        print('Transcations:')
        
        for transaction in self.transactions:
            transaction.display_details()
            
    def get_block_transactions(self):
        return self.transactions