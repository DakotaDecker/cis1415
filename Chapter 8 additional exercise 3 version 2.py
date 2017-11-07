codes = {'A':'@', 'a':'9', 'B':'%', 'b':'#', 'C':'!', 'c':'1', 'D':')', 'd':'0', 'E':'(', 'e':'3', 'F':'^', 'f':'4', 'G':'*', 'g':'2', 'H':'$', 'h':'8', 'I':'9', 'i':'5', 'J':'~', 'j':'`', 'K':':', 'k':';', 'L':'7', 'l':'|', 'M':'+', 'm':'6', 'N':'_', 'n':'=', 'O':'/', 'o':'"', 'P':'.', 'p':',', 'Q':'?', 'q':'<', 'R':'>', 'r':'}', 'S':']', 's':'{', 'T':'[', 't':'&', 'U':'0', 'u':'10', 'V':'11', 'v':'12', 'W':'13', 'w':'14', 'X':'15', 'x':'16', 'Y':'17', 'y':'18', 'Z':'19', 'z':'20'}

Text_in = ''

while Text_in.capitalize() != '21':
      Text_in = input('Enter a sentence:\n').capitalize()

      Text_out = ''
      
      for char in Text_in:
          if char in codes:
              Text_out += codes[char]
          else:
              Text_out += char

      print(Text_out)
      

      
      
