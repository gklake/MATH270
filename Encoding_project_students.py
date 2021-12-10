# Title: Encoding_project_students.py
# Description: Simple example of using matrices to encrypt/decrypt a message (using a simple cypher 0~space, 1~a, etc.)
# Author: Dr. Greg Rainwater
#
import sys
import numpy as np
import math
"""
# ------------------------------------------------------
# Convert letters to numbers and numbers to letters using
# our simple cypher.
# ------------------------------------------------------
"""
def cypherLet2Num(msg):
    output = []
    for character in msg:
        number = ord(character) - 96
        if number == -64:
            number = 0
        output.append(number)    
    return output

def cypherNum2Let(msg):
    output=[]
    #for x in np.nditer(msg.copy(order='F')):
    for x in msg:
        if int(x)==27:
            letter=chr(32)
        elif int(x)==0:
            letter=chr(32)
        else:
            letter=chr(int(x)+96)
        output.append(letter)
    return output
"""
# ------------------------------------------------------
# Check the length of the message and make sure we can 
# partition it into groups of length 4 by adding 
# an appropriate number of spaces depending on the length
# of original message.
#
# note: this can easily be generalized but to be clear here
#       we use this approach and only groups of length 4
# ------------------------------------------------------
"""
def checkLength(msg):
    """
    # You can use the code below as it is more intuitive or you can try using something a bit more compact:
      if len(msg) % 4 != 0:   
        numSpaces = 
        msg += ' ' * (numSpaces)
    # but you will have to figure out the number of spaces using the remainder :)
    """
    
    #  !!!!!!!
    #    ADD CORRECT NUMBER OF SPACES TO MESSAGE (in the single quotes) SO MESSAGE IS DIVISIBLE BY 4
    #  !!!!!!!
    if len(msg) % 4 == 1:
        msg = msg+('')
    
    #  !!!!!!!
    #    ADD CORRECT NUMBER OF SPACES TO MESSAGE (in the single quotes) SO MESSAGE IS DIVISIBLE BY 4
    #  !!!!!!!        
    elif len(msg) % 4 == 2:
        msg = msg+('')
    #  !!!!!!!
    #    ADD CORRECT NUMBER OF SPACES TO MESSAGE (in the single quotes) SO MESSAGE IS DIVISIBLE BY 4
    #  !!!!!!!
    
    elif len(msg) % 4 == 3:
        msg = msg+('')
    return msg


"""
# ------------------------------------------------------
# Encodes a "message matrix" by matrix multiplication
# ------------------------------------------------------
"""
def encodeMessage(msg,A, printdiag=1):
    E = A*msg      # Apply encoding matrix to message matrix
    if printdiag==1:
        print("Encoding message using matrix A:\n %s" % A)
        print("Encoded Message Matrix:\n %s" % E)
    E = E % 27    # Module 27 since we have only 27 characters
    if printdiag==1:
        print("Encoded Message Matrix (mod 27):\n %s" % E)
    return E

   
"""
# ------------------------------------------------------
# Decodes a "message matrix" by matrix multiplication
# ------------------------------------------------------
"""
def decodeMessage(msg,Ainv,printdiag=1):
    D = Ainv*msg     # Apply decoding matrix to message matrix
    if printdiag==1:
        print("Decoding message using matrix inv(A):\n %s" % Ainv)
        print("Decoded Message Matrix:\n %s" % D)
    D = D % 27    # Module 27 since we have only 27 characters
    if printdiag==1:
        print("Decoded Message Matrix (mod 27):\n %s" % D)
    return D
 

if __name__ == "__main__":
    printdiag=1  # Print diagnostics (0 - off, 1 - on)
    
    #  !!!!!!!
    # INSERT ENCODING/ENCRYPTING MATRIX 'A' BELOW (CHANGE FROM IDENTITY MATRIX TO MATRIX 'A' GIVEN IN PROBLEM)
    #  !!!!!!!
    A = np.matrix('1 0 0 0;'
                  '0 1 0 0;'
                  ' 0 0 1 0;'
                 ' 0 0 0 1')    
    

    Ainv = np.linalg.inv(A)  # Use numpy to calculate the inverse of the matrix A
 #   if printdiag==1:
 #       print('inverse(A)=\n%s' % Ainv)
    if sys.version_info[0] == 2:  # check version of python you are using so we use correct input function
        inputmsg = raw_input('Input Message: ')  # for python 2.x users
    else:
        inputmsg = input('Input Message: ') # for python 3.x users
    inputmsg = inputmsg.lower()       # convert message to lower case letters
    msg = checkLength(inputmsg)  # If length of message is not divisible by 4 then add spaces
    msg = cypherLet2Num(msg)   # Convert letters to numbers 
    if (len(msg) % 4 != 0):
        print('There was a problem...make sure to modify the code in \'checkLength\'')
        choice = 0
    else:
        Mmsg = np.reshape(msg,(4,-1),order='F')   # Reshapes vector of length (4k)x1 into 4xk matrix
        choice = input('Do you want to \n (1) Encode Message \n (2) Decode Message\n Choose (1 or 2): ') 
    if choice == 0:
        print('fix errors')
    elif (choice == '1' or choice == 1):
        # Encode the message
        EncMmsg=encodeMessage(Mmsg,A,printdiag) #encoded message in matrix form
        Emsg=np.reshape(EncMmsg,(-1,1),order='F')   # Reshapes 4xk matrix to (4k)x1 vector
        Emsg = cypherNum2Let(Emsg)  # Convert numbers to letters
        print("Encoded message: %s" % ''.join(Emsg))  # Print the encoded message
    else:
        DecMmsg=decodeMessage(Mmsg,Ainv,printdiag) #encoded message in matrix form
        Dmsg=np.reshape(DecMmsg,(-1,1),order='F')   # Reshapes 4xk matrix to (4k)x1 vector
        Dmsg = cypherNum2Let(Dmsg)  # Convert numbers to letters
        print("Decoded message: %s" % ''.join(Dmsg))  # Print the encoded message        
  