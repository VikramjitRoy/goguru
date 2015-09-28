from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("../brain")
rs.sort_replies()
print("----------------------------------------------------")
print("|              WELCOME TO GOGURU                   |")
print("----------------------------------------------------")

while True:
    msg = raw_input("You> ")
    #msg = msg.lower()
    if msg == '/quit' or msg == 'bye':
        quit()
    reply = rs.reply("localuser", msg)
    print ("GoGuru>"), reply


