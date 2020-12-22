print('Welcome to Heaven Is For Real Game')

name = input("What is your name? ")
age = int(input('How old are you? '))
congs = '----->>> CONGRATULATIONS, HEAVEN IS YOURS <<<-----'

print('Welcome ', name)

if age >= 18:
    ans = input('Are you saved yet ' + name + ' ?' + '(Yes or No) ').lower()
    if ans == 'yes':
        input('When did you get born again? ')
        print('Glad you are !')
        ans = input('Are you walking right with Christ? (Yes or No or Not Sure) ').lower()
        if ans == 'yes':
            print('Wow, that\'s great to hear? ')
            input('When Did you last read the Bible ?')
            print('That\'s okay, nah worries, God\'s love never ceases! ')
            ans = input('Do you pray? (Yes or No) ').lower()
            if ans == 'no':
                print('Well You need to! God loves communicating to us on a daily!')
                ans = input('Can we pray together? (Yes or No) ')
                if ans == 'yes':
                    print('Heavenly Father, we thank you for today, Thanks for this child of yours!')
                    print(congs)
                else:
                    print("Well, God Loves you still!")
                    ans = input('Can you do me a favor? (yes or no) ').lower()
                    if ans == 'yes':
                        print("When you go home, ask your parents to pray for you! God Bless You")
                        print(congs)
                    else:
                        print("It's okay child of God!")
                        print(congs)
            else:
                print('Ohh, that\'s a great practice')
                print(congs)
        else:
            print('Nah Worries, God still loves you the way how you are but u gotta pray!')
            print('Otherwise')
            print(congs)
    else:
        ans = input("Can I lead you to a beautiful life? (Yes or No) ").lower()
        if ans == 'yes':
            print('Say this simple prayer with me!')
            print('Dear Jesus, I welcome you into my heart today, Help me coz Iam in need of a Saviour!Thank You Lord!')
            input('How do you feel now?')
            print('I know!')
            ans = input('Do you have a home church? (Yes or No? )').lower()
            if ans == 'yes':
                print('Send Love & Greetings!')
                print(congs)
            else:
                print('Feel free to make this your home base! More than welcome!')
                print(congs)
        else:
            print('There is never time to be ready! Change your life today, otherwise God Loves You!')
            print('You STILL NEED JESUS!')
elif age <= 10:
    ans = input('Have you heard of Jesus yet? (Yes or No) ').lower()
    if ans == 'yes':
        print('Ohh great!')
        ans = input('so have you given your life to Him yet? (Yes or No) ').lower()
        if ans == 'yes':
            print(congs)
        else:
            print('You need to give your life to Christ!')
            ans = input('Are you ready? (Yes or No)')
            if ans == 'yes':
                print('Say this simple prayer with me!')
                print('Dear Jesus, I welcome you into my heart today, '
                      'Help me coz Iam in need of a Saviour!Thank You Lord!')
                input('How do you feel now?')
                print('I know!')
                print(congs)
            elif ans == "no":
                print('What\'s that?')
            else:
                print('The Time will come when you are ready!')
                print('God Bless you!')
    else:
        print('Jesus is the son of God who came on Earth  to save us! When You Believe Him, everything changes!')
else:
    ans = input('Do you know a man called Jesus? ').lower()
    if ans == "yes":
        print("Wow, that's great!")
        ans = input('Do you mind giving your life to Jesus Now? (Yes or No) ').lower()
        if ans == "yes":
            print('Say this simple prayer with me!')
            print('Dear Jesus, I welcome you into my heart today, Help me coz Iam in need of a Saviour!Thank You Lord!')
            ans = input('How do you feel now?')
            print('I know!')
            print('Anyway')
            print(congs)
        else:
            print("It's okay, God still loves you and\n he would like you to be a part of him\n "
                  "whenever you are ready!")
            print('God Bless you and stay well!')
    elif ans == "no":
        print("It is very okay, Jesus is the son of God and came here on earth to live" +
              " with us and whoever believes in him will become a child of God")
    else:
        print('I did not understand that!')