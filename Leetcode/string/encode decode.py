class EncodeDecode:
    #make a encode, decode algorithm by yourself 
    def encode(self,strs):
        encode_string =''
        delimeter = '#'
        for item in strs:
            length = len(item)
            encode_string += str(length) + delimeter + item
        return encode_string


    def decode(self,s):
        string = s
        delimeter = '#'
        output_array = []
        last_input_index = 0
        for index,char in enumerate(string):
            if char == delimeter and string[index-1].isdigit():
                number_index = int(string[last_input_index:index:1])
                start_index = index+1
                end_index = (start_index)+(number_index)
                last_input_index = end_index
                slice = string[start_index:end_index]
                output_array.append(slice)
        return output_array
    

input =  ["neet","code","love","you"]
input =  ["neet","#code","love","you"]
input = ["we","say",":","yes","!@#$%^&*()"]

encodeDecode = EncodeDecode()
encoded = encodeDecode.encode(input)
decoded_string = encodeDecode.decode(encoded)
print(decoded_string)


