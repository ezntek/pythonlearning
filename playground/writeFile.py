import os

while True:
    print("welcome to basicFileWriter")
    choice = input("[r]ead, [w]rite, [a]ppend?: ")
    file = input("to what file? (full path): ")

    buffer = None
    writeBuffer = None

    try:
        if choice == "r":
            with open(file) as readFrom:
                buffer = readFrom.read()
                print("I read: \n\n"+buffer+"")

                exit()

        if choice == "w":
            with open(file, "w") as writeTo:
                writeBuffer = input("What to write to that file?: ")
                writeTo.write(writeBuffer)

                print("it wrote: \n\n"+writeBuffer+"")
                exit()
        
        if choice == "a":
            with open(file, "a") as appendTo:
                writeBuffer = input("what to append to that file?: ")
                appendTo.write("\n"+writeBuffer+"")

                print("I appended: \n\n"+writeBuffer+"")
    except FileNotFoundError:
        print("that file doesn't exist, smartass...")