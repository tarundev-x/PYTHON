  def findComplement(self, num: int) -> int:
   # 1. int.bit_length()
  #Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
        num_bits=num.bit_length()
    '''a = 5 = 0000 0101 (Binary)
       a << 1 = 0000 1010 = 10'''

        mask=(1<<num_bits)-1
        return num^mask
