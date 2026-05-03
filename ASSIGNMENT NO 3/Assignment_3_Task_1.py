import hashlib
import datetime
# Create a Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                  # Block number
        self.timestamp = timestamp          # Time of creation
        self.data = data                    # Data stored in block
        self.previous_hash = previous_hash  # Hash of previous block
        self.hash = self.calculate_hash()   # Current block hash
    # Function to calculate hash using SHA256
    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()
# Create Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize with first block
    # Create the first block (Genesis Block)
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")
    # Get last block in chain
    def get_last_block(self):
        return self.chain[-1]
    # Add new block
    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=datetime.datetime.now(),
            data=data,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)
# Function to display blockchain
def print_chain(blockchain):
    for block in blockchain.chain:
        print("Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Previous Hash:", block.previous_hash)
        print("Hash:", block.hash)
        print("-" * 50)
# ---------------- MAIN PROGRAM ----------------
# Create blockchain
my_blockchain = Blockchain()
# Add 4–5 blocks
my_blockchain.add_block("Block 1 Data")
my_blockchain.add_block("Block 2 Data")
my_blockchain.add_block("Block 3 Data")
my_blockchain.add_block("Block 4 Data")
print("🔗 Original Blockchain:\n")
print_chain(my_blockchain)
# ---------------- MODIFY A BLOCK ----------------
print("\n Modifying Block 2 Data...\n")
# Change data of block 2
my_blockchain.chain[2].data = "Hacked Data"
my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()
print(" Blockchain After Modification:\n")
print_chain(my_blockchain)