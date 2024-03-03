# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  False


def generate_hashtagV1(s):
    string = s.split(' ')
    data = ''

    if s == "" or len(s) >= 140:
        return "False"
    
    if len(string) >= 1:
        for words in string:
            data += words.capitalize()
        return "#" + data
    

def generate_hashtagV2(s):
    
    if not s or len(s) == 0:
        return "False"

    words = s.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        return "False"

    return hashtag
    

def generate_hashtagV3(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return "False" if (len(s) == 0 or len(output) > 140) else output


# TEST CASE
lista = ['Codewars', 'Codewars      ', '      Codewars', '', 'Codewars Is Nice', 'codewars is nice', 'CoDeWaRs is niCe', 'c i n', 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat']
for i in lista:
    print(f'V1 = {generate_hashtagV1(i).ljust(20, " ")} | V2 = {generate_hashtagV2(i).ljust(20, " ")} | V3 = {generate_hashtagV3(i).ljust(20, " ")}')