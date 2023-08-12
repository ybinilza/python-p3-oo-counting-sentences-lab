import re

class MyString:

  def __init__(self, string=""):
    self.string = string

  def set_value(self, string):
    if(type(string) is str):
      self._string = string
    else:
      print("The value must be a string.")
  
  def get_value(self):
    return self._string
  
  def is_sentence(self):
    if(self.string[len(self.string) - 1] == "."):
      return True
    else:
      return False
    
  def is_question(self):
    if(self.string[len(self.string) - 1] == "?"):
      return True
    else:
      return False
  
  def is_exclamation(self):
    if(self.string[len(self.string) - 1] == "!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    my_list = re.split(r'[.?!]+', self.string)
    count = 0
    for word in my_list:
      if word != "":
        count = count + 1
    
    return count

  value = property(get_value,set_value)