# Modified Proof of Immune with Conscious Consensus mechanism
This repo is dedicated to creating a public blockchain network with Modified Proof of Immune  algorithm to create conscious consensus among the partiicpating nodes in the network.
This work has been simulated in the lab environment setting up test network of ethereum public blockchain with hyperledger besu client.

In order to run this code,  you can set up a test network with the code mentioned in the network folder.

Once the network is set up, you can run the code inside the poi folder. first install all the requirements mentioned under the requirements file.

pip install -r requirements.txt

To run each node you can use the following command. Including the command for 3 nodes being set up. You can test with more number of nodes. Add keys as per the requirements of new node.

Node1: sudo python3 Main.py localhost 10001 5000 keys/genesisPrivateKey.pem
Node2: sudo python3 Main.py localhost 10003 5003 keys/karmaPrivateKey.pem
Node3: sudo python3 Main.py localhost 10002 5001

once the node is up and running, we can start testing the transaction.
Each transaction execution can be made using

 python Interaction.py
