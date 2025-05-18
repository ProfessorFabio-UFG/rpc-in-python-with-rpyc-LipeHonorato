import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer
import random

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_accumulator(self):
    self.accumulator = 0
    for i in range(len(self.value)):
      self.accumulator += self.value[i]
    return self.accumulator

  def exposed_sum(self, value1, value2):
    return value1 + value2

  def exposed_loadedDice(self):
    if random.randint(1,10) == 3:
      return random.randint(1,6)
    else: 
      return 4
    

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

