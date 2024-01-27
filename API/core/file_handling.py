import json
import os

def load_chain_from_disk(chain, current_transactions):
    if os.path.exists('blockchain.json'):
        with open('blockchain.json', 'r') as f:
            data = json.load(f)
            chain = data['chain']
            current_transactions = data['current_transactions']
    else:
        # Create the blockchain.json file if it doesn't exist
        save_chain_to_disk(chain, current_transactions)

def save_chain_to_disk(chain, current_transactions):
    data = {
        'chain': chain,
        'current_transactions': current_transactions,
    }
    with open('blockchain.json', 'w') as f:
        json.dump(data, f, indent=4)

def load_nodes_from_disk(nodes):
    if os.path.exists('nodes.json'):
        with open('nodes.json', 'r') as f:
            nodes = json.load(f)
    else:
        # Create the nodes.json file if it doesn't exist
        save_nodes_to_disk(nodes)
        
def save_nodes_to_disk(nodes):
    with open('nodes.json', 'w') as f:
        json.dump(nodes, f, indent=4)