#Caesar Şifreleme

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
 
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")



# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#kodumuzu tek def fonksiyonuna tanımlayarak kısaltalım

def caesar(start_text, shift_amount, cipher_direction):
  end_text="" #bu dize işlemin sonucunu içerir
  if cipher_direction=="decode": #bu kod decode ise kaydırma yönünü terse çevirir
    shift_amount *= -1
  for letter in start_text: #her bir karakter için bir döngü başlar
    position = alphabet.index(letter) #her karakterin alfabe içindeki konumu belirlenir
    new_position = position + shift_amount # yeni konum
    end_text += alphabet[new_position] #şifrelenmiş/deşifre edilmiş metin eklenir
  print(f"Here's the {direction}d result: {end_text}") #metin ekrana yazdırılır

 
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    

