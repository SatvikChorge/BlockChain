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
        return hashlib.sha256(
            (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
        ).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), new_data, latest_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 40)

# ----------- Interactive Part -------------
if __name__ == "__main__":
    blockchain = Blockchain()
    while True:
        print("\n1. Add a block")
        print("2. Print blockchain")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter data to store in block: ")
            blockchain.add_block(data)
            print("✅ Block added successfully!")
        elif choice == "2":
            blockchain.print_chain()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")