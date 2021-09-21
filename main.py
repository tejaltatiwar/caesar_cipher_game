alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
start_again=True
while start_again:
    direction=input("Type 'encode'to encrypt,type 'decode'to decrept:\n")
    text=input("Type your message:\n")
    shift=int(input("Enter the shift no.:\n"))
    shift=shift%25
    def caeser(given_direction,wanted_text,shift_key):
        final_msg=""
        for l in wanted_text:
            if l in alphabet:
                if direction=="encode":
                    letter_position = alphabet.index(l)
                    letter_position+=shift_key
                else:
                    letter_position = alphabet.index(l)
                    letter_position-=shift_key
                msg=alphabet[letter_position]
                final_msg+=msg
            else:
                final_msg += l
        print(f"{direction}d code is {final_msg} .")
    caeser(direction,text,shift)
    a = input("DO you want to repeat?yes or no\n")
    if a == "no":
        print("Goodbye")
        start_again = False
    else:
        start_again=True
