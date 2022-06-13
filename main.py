# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    content = open(filename,"r") 
    filename = content.read()

    for line in filename:
        line = line.strip() 
        line = line.lower()
        line = line.strip("/n,.?")
        words = filename.split(" ")
    print(words)
    return words
# print(words)
# read_file_content("./story.txt")


def count_words():
    content = read_file_content("./story.txt") 
    dict = {}
    for word in content:
        if word in dict:
            dict[word] += 1   
        else:
            dict[word] = 1
    for key in list(dict.keys()):
        print(key, ":", dict[key])
    # return count_words
print(count_words())