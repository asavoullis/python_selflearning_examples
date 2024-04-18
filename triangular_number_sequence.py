def decode(message_file):
    # Read the file contents
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Create a dictionary to store the word-number mapping
    word_dict = {}
    for line in lines:
        number, word = line.strip().split()
        word_dict[int(number)] = word
    
    # print(word_dict)
    # Find the maximum number to determine the number of lines in the pyramid
    max_num = max(word_dict.keys())
    # print(max_num)

    # sorted_dict = dict(sorted(word_dict.items()))
    # print("")
    # print(sorted_dict)

    
    decoded_message = []

    # The triangular number sequence
    triangular_numbers = [int(i*(i+1)/2) for i in range(1, max_num + 1)]

    for i in range(1, max_num + 1):
        if i in triangular_numbers:
            # print(i)
            decoded_message.append(word_dict[i])
    
    return ' '.join(decoded_message)

print("")
message = decode('number_word_input.txt') # coding _ qual_ input
print(message)
