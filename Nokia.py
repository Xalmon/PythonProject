print(f"""
List of menu functions
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10.Reminders
11. Clock
12. Profiles
13. SIM services
""")


Phone = int(input("Choose an option from 1 - 13: "))
print("\n")
if Phone == 1:
    print(f"""
          1. Search
          2. Service Nos. 1
          3. Add name
          4. Erase
          5. Edit
          6. Assign tone
          7. Send b’card
          8. Options
              1.8 Type of view
              2.8 Memory Status
          9. Speed dials
          10. Voice tag
    """)
    phone = float(input("Choose an option from 1.8 - 2.8 or 0 to return: "))
    if phone == 1.8:
        print(f"""
            1. Type of view
            """)
    elif phone == 0:
        main_menu()
    else:
        print(f"""
        2. Memory Status
         """)
if Phone == 2:
    print(f"""
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10.Service command editor
    """)
    phone = float(input("Choose an option from 2.7: "))
    if Phone == 2.7:
        print(f"""
            1. Set 1
            2. Common
            """)
        phone = float(input("Choose an option from 2.71, 2.72: "))
        if phone == 2.71:
            print(f"""
                1.
                Message
                centre
                number
                2.
                Messages
                sent as
                3.
                Message
                validity
                """)
            if phone == 2.72:
                print(f"""
                1. Delivery reports
                2. Reply via same centre
                3. Character support
                """)
if Phone == 3:
    print(f"""
Chat
            """)
if Phone == 4:
    print(f"""
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
    """)
    phone = float(input("Choose an option from 4.5, 4.6, 4.7: "))
    if phone == 4.5:
        print(f"""
        1. Last call duration
        2. All calls’ duration
        3. Received calls’ duration
        4. Dialled calls’ duration
        5. Clear timers
        """)
    elif phone == 4.6:
        print(f"""
        1. Last call cost
        2. All calls’ cost
        3. Clear counters
        """)
    elif phone == 4.7:
        print(f"""
       1. Call cost limit
       2. Show costs in
        """)
if Phone == 5:
    print(f"""
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
    """)
if Phone == 6:
    print(f"""
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
    """)
    phone = float(input("Choose an option from 6.1, 6.2, 6.3: "))
    if phone == 6.1:
        print(f"""
          1. Automatic redial
          2. Speed dialling
          3. Call waiting options
          4. Own number sending
          5. Phone line in use
          6. Automatic answer
              """)
    elif phone == 6.2:
        print(f"""
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm SIM service actions
        """)
    elif phone == 6.3:
        print(f"""
        1. PIN code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Phone security
        6. Change access code
        """)
if Phone == 7:
    print(f"""
7. Call divert
    """)
if Phone == 8:
    print(f"""
8. Games
    """)
if Phone == 9:
    print(f"""
9. Calculator
    """)
if Phone == 10:
    print(f"""
10.Reminders
    """)
if Phone == 11:
    print(f"""
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
    """)
if Phone == 12:
    print(f"""
12. Profiles
    """)
if Phone == 13:
    print(f"""
13. SIM services
    """)
if Phone > 13:
    print("Enter a Valid option from 1 - 13: ")
    Phone = int(input("Choose an option from 1 - 13: "))
if Phone < 0:
    print("Enter a Valid option from 1 - 13: ")
    Phone = int(input("Choose an option from 1 - 13: "))
# if phone > 7:
#     print("reenter option")
#     phone = float(input("Choose an option from 1.1, 6.9: "))
# if phone < 0:
#     print("reenter option")
#     phone = float(input("Choose an option from 1.1, 6.9: "))


