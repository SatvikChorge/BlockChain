import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, previous_block.hash)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash() or curr.previous_hash != prev.hash:
                return False
        return True

# --- Usage ---
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction 1: Alice pays Bob 10 BTC")
my_blockchain.add_block("Transaction 2: Bob pays Charlie 5 BTC")

for block in my_blockchain.chain:
    print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, Previous: {block.previous_hash}")

print("Blockchain valid?", my_blockchain.is_chain_valid())
