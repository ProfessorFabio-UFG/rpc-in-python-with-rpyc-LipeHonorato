import rpyc
from constRPYC import * #-
import random

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  print (conn.root.exposed_value())   # Print the result
  print(f"Soma dos valores da lista: {conn.root.exposed_accumulator()}") # Print the sum of the values in the list value

  a = random.randint(0,100)
  b = random.randint(0,100)

  print(f"Soma de {a} e {b}: {conn.root.exposed_sum(a, b)}")

  print("Rolling the dice...")
  print(f"The dice roll was {conn.root.exposed_loadedDice()}")
