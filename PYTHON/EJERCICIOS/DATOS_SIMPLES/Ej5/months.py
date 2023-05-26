months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'Agoust', 9:'Septiember', 10:'Octuber', 11:'November', 12:'December'}
print("Set the date in format='dd/mm/aaaa': ", end="")
date = input()
date = date.split('/')
print(date)
print(date[0], 'of', months[int(date[1])], 'of', date[2])