import sys

def printing(output):
    row = ""
    lines = ""
    row_count = 0
    for char in output:
        row += char 
        if len(row) == 5 and row_count < 9:
            row += " "
            lines += row
            row_count += 1
            row = ""
        elif len(row) == 5 and row_count == 9:
            lines += row +"\n"
            row_count = 0
            row = ""

    return(lines + row + "\n")

def encryption(message, n):
    message = message.upper()
    characters = ""
    
    for char in message:
      if char.isalpha():
        characters += char
    
    encoded_text = []
    
    for char in characters:
      char_ascii = ord(char)
      new_ascii = char_ascii + n
      
      if new_ascii > ord("Z"):
        res = (new_ascii - ord("Z")) % 26
        
        if res == 0:
          res = 26
        
        new_ascii = res + 64
    
      encoded_text.append(chr(new_ascii))

    value = ''.join(encoded_text)
    return printing(value)
   
args = sys.argv

for line in sys.stdin:
    res = encryption(line.strip(), int(args[1]))
    sys.stdout.write(res)