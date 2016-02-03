if __name__ == "__main__":
    name = input("What's your name:")
    greeting = "Hello,%s"%name
    l_count = greeting.count('l')
    l_percent = (l_count/len(greeting))*100
    print(greeting)
    print("The length of the sentence is %d, there are %d 'l' in it(%.2f%%)."
          %(len(greeting),l_count,l_percent))