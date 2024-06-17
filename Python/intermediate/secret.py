sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
      
  # Move the cursor to the beginning of the file
  file.seek(0)

  # Modify the message to simulate unsending
  unsent_message = 'This message has been unsent.'

  file.write(unsent_message)

try:
    file = open('sent_message.txt', 'r')
    current_message = file.read()
finally:
    print("Original:", original_message)
    print("Current:", current_message)
    file.close()
