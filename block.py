import functools
import hashlib
import collections 

import hash_util

MINING_REWARD = 10

genesis_block = {'previous_hash': '', 'index': 0, "transactions": [], 'proof': 100}
blockchain = [genesis_block]
open_transactions = []
owner = "Jack"
participants = {"Jack"}


def valid_proof(transactions, last_hash, proof):
  guess = (str(transactions) + str(last_hash) + str(proof)).encode()
  guess_hash = hash_util.hash_string_256(guess)
  print(guess_hash)
  return guess_hash[0:2] == '00'

def proof_of_work():
  last_block = blockchain[-1]
  last_hash = hash_util.hash_block(last_block)
  proof = 0
  while not valid_proof(open_transactions, last_hash, proof):
    proof +=1
  return proof


def get_last_blockchain_value():
  if len(blockchain) < 1:
    return None
  return blockchain[-1]

def get_balance(participant):
  tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
  open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
  tx_sender.append(open_tx_sender)
  amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

  tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
  amount_recieved = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

  return amount_recieved - amount_sent

def verify_transaction(transaction):
  sender_balance = get_balance(transaction['sender'])
  return sender_balance >= transaction['amount']


def add_transaction(recipient, amount=1.0, sender=owner):
  # transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
  transaction = collections.OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])
  if verify_transaction(transaction):
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
    return True
  return False
  

def mine_block():
  last_block = blockchain[-1]
  hashed_block = hash_util.hash_block(last_block)
  proof = proof_of_work()
  # reward_transaction = {'sender': 'MINING', 'recipient': owner, 'amount': MINING_REWARD}
  reward_transaction = collections.OrderedDict([('sender', 'Mining'), ('recipient', owner), ('amount', MINING_REWARD)])
  # coppied_transactions = 
  open_transactions.append(reward_transaction)
  block = {'previous_hash': hashed_block, 'index': len(blockchain), "transactions": open_transactions, 'proof': proof}
  blockchain.append(block)
  return True

def get_transaction_value():
  tx_recipient = input('enter the recipient of the transaction')
  tx_amount = float(input("your transaction here: "))
  return (tx_recipient, tx_amount)

def get_user_choice():
  user_input= input()
  return user_input

def verify_chain():
  for (index, block) in enumerate(blockchain):
    if index == 0:
      continue
    if block['previous_hash'] != hash_util.hash_block(blockchain[index-1]):
      return False
    if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
      print('proof of work was invalid')
      return False
  return True

def verify_transactions():
  is_valid = True
  for tx in open_transactions:
    if verify_transaction(tx):
      is_valid = True
    else:
      is_valid = False
  return is_valid


# def hash_block(block):
#   return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


def print_blockchain_elements():
    for block in blockchain:
      print('Outputting block: ')
      print(block)
    else:
      print("-" * 30)

waiting_for_input = True

while waiting_for_input:
  print("Please choose")
  print("1: add a new Transaction value")
  print("2: Mine Bocks")
  print("3: Output the blockchain blocks")
  print("4: oputput Participants")
  print("5: check transaction validity")
  print("h: manipulate the chain")
  print("q: quit")
  user_choice = get_user_choice()
  if user_choice == '1':
    tx_data = get_transaction_value()
    recipient, amount = tx_data
    if add_transaction(recipient, amount):
      print('Added to Transaction')
    else:
      print('transaction failed')
    print(open_transactions)

  elif user_choice =='2':
    if mine_block():
      open_transactions = []

  elif user_choice =='3':
    print_blockchain_elements()

  elif user_choice =="4":
    print(participants)
  
  elif user_choice == '5':
    if verify_transactions:
      print ('All Transactions valid')
    else:
      print('invalid transactions')

  elif user_choice =='h':
    if len(blockchain)>0:
      blockchain[0]={'previous_hash': '', 'index': 0, "transactions": [{'sender': 'chris', "recipient": 'Jack', 'amount': 100}]}

  elif user_choice == 'q':
    waiting_for_input = False

  else:
    print('input was invalid')

  if not verify_chain():
    print_blockchain_elements()
    print('invalid block')
    break
  print('Balance of {}: {:6.2f}'.format('Jack', get_balance('Jack')))
else:
  print('user left')

print('done')