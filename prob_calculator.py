import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**balls):
    self.contents = []
    for key in balls.items():
      for number in range(key[1]): 
        self.contents.append(key[0])
  
  def draw(self,number):
    temp = []
    if number > len(self.contents):
      return self.contents
    for i in range(number):
      rball = random.randint(0,len(self.contents)-1)
      temp.append(self.contents[rball])
      self.contents.remove(self.contents[rball])
    return temp

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  cont = 0
  cond = True
  for i in range(num_experiments):
    expec = copy.deepcopy(expected_balls)
    another_hat = copy.deepcopy(hat)
    temp = another_hat.draw(num_balls_drawn)
    
    for i in temp:
      if (i in expec):
        expec[i] -= 1
    
    for i in expec:
      if expec[i] > 0:
        cond = False
    
    if cond == True:
      cont = cont + 1
    else:
      cond = True  

  return cont/num_experiments
