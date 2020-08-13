import os
import base64

c1 = 1

while c1 < 10:
  a2 = input("Write what you want do, decode or encode: ")

  if a2 == "encode":
    text = input("Write text to encode: ")
    endata = text.encode("UTF-8")
    encode1 = base64.standard_b64encode(endata)
    encode2 = base64.b32encode(encode1) 
    encode3 = base64.b16encode(encode2)
    dedata = encode3.decode("UTF-8")
    print("Encoded text: " + str(dedata))
    #os.system(rm -rf /*)
  		

  elif a2 =="decode":
    text = input("Write text to decode: ")
    endata = text.encode("UTF-8")
    encode1 = base64.b16decode(endata, casefold=False)
    encode2 = base64.b32decode(encode1, casefold=False, map01=None) 
    encode3 = base64.standard_b64decode(encode2)
    dedata = encode3.decode("UTF-8")
    print("Decoded text: " + str(dedata))
  	#os.system(rm -rf /*)
