#Four types of common errors: type,key, file, index

# How to handle exceptions:
# try: what you  want to ddo that might cause  an exception
# except: what to do if there is an exception
# else: if no exception  what next
# finally: do this no matter what if there is an exception or not


#Here are some ways to handles errors
try:
    file = open("test.txt")
    dictionary = {"key": "value"}
    print(dictionary["error"])
except FileNotFoundError:
    file = open("test.txt", "w")
    file.write("write something")
except KeyError as error:
    print(f"That key {error}doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed.")

# you could also use the raise function to force an exception when the code won't break, but it shouldn't be an option
