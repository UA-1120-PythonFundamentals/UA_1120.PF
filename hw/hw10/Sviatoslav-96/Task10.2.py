class Human():
  def __init__(self, *names):
      self.names = names

  def welcome_message(self):
      for name in self.names:
          print("Hello,", name)

  @classmethod
  def get_species_info(cls):
      return f"This is a species of {cls.__name__}"

  @staticmethod
  def arbitrary_message():
      return "This is a static method that returns an arbitrary message."

human = Human("John", "George", "Paul", "Ringo")

human.welcome_message()

print(Human.get_species_info())

print(Human.arbitrary_message())