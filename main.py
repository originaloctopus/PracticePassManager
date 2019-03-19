import random
import string
#password manager
#input the information for saving

#this needs to be encrypted


def newPassword():
    website = input("What's the website? ")

    username = input("What's the username? ")

    password = input("What's the password?\nIf you want a randomly generated password, type random.\n")

    if password == 'random':
        numOfDigits = int(input('How many characters long do you want the password to be?'))
        randomPassword = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(numOfDigits))
        #f is format string to allow us to put a variable into the string.
        print(f'This is the random password: {randomPassword}')
        password = randomPassword
    else:
        pass

    websiteEntry = dict([("website", website), ("username", username), ("password", password) ])

    passwordList.append(websiteEntry)

    print(passwordList)

# print "dict['Name']: ", dict['Name']
# print "dict['Age']: ", dict['Age']

def findPassword():
    userSeeks = input('What website do you seek? ')
    for entry in passwordList:
        if userSeeks == entry['website']:
            print(entry['website'])
            print(entry['password'])
        else:
            print('That website isn\'t stored yet.')
    # for userSeeks in passwordList:
    #     userSeeks.strip()
    

passwordList = []

while True:
    print('''This is a password manager, ya dingle.
    Type "new" to create a new password.
    Type "show" to look up a password.
    ''')
    userChooses = input('Whatcha wanna do?')
    if userChooses == 'new':
        newPassword()
    elif userChooses == 'show':
        findPassword()
        print('You need to actually do this....')
    else:
        print('Try again sonny.')



    #print(website + username + password)

    #inside the list there will be 3 dictionary lists inside the lists.
    

