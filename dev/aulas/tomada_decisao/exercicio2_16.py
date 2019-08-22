ip = str(127)

posicao = int((ip[:3]))

if(posicao <= 127):
    print("O IP digitado é da classe A")
elif(posicao > 127 and posicao <= 191):
    print("O IP digitado é da classe B")
elif(posicao > 191 and posicao <=223):
    print("O IP digitado é da classe C")
elif(posicao > 223 and posicao <=239):
    print("O IP digitado é da classe D")
elif(posicao > 240):
    print("O IP digitado é da classe E")