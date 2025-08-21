import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # vote data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Data (Vote): {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")


# ========== Voting System ==========
def main():
    blockchain = Blockchain()
    votes = {}

    while True:
        print("\n--- Blockchain Voting System ---")
        print("1. Cast a vote")
        print("2. Show Blockchain")
        print("3. Count votes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            voter = input("Enter voter name: ")
            candidate = input("Enter candidate name: ")

            vote_data = f"{voter} voted for {candidate}"
            new_block = Block(len(blockchain.chain), time.time(), vote_data, blockchain.get_latest_block().hash)
            blockchain.add_block(new_block)

            # count votes
            if candidate not in votes:
                votes[candidate] = 0
            votes[candidate] += 1

            print(f"✅ Vote added: {vote_data}")

        elif choice == "2":
            blockchain.display_chain()

        elif choice == "3":
            print("\n--- Voting Results ---")
            for candidate, count in votes.items():
                print(f"{candidate}: {count} votes")

        elif choice == "4":
            print("Exiting... Thank you for using the system!")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()