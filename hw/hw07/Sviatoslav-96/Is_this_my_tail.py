def correct_tail(body, tail):
  sub = body[-1]
  return sub == tail

substr = ("Fox", "Rhino", "Meerkat", "Emu", "Badger", "Giraffe")

for i in range (len(substr)):
  result = correct_tail(substr[i], substr[-1])