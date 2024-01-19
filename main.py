from Blockchain import Blockchain
from Block import Block

#Initialize blockchain
block = Blockchain()

#Mine 10 blocks
for cont in range(10):
    block.mine(Block("Block " + str(cont+1)))

#Print out each block in the blockchain
while block.head != None:
    print(block.head)
    block.head = block.head.next