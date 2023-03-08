from psycopg2 import connect
from bcrypt import checkpw, gensalt, hashpw

con = connect(host='containers-us-west-57.railway.app',database='railway', port=6423, user='postgres', password='bbBG9F68pngQR3pxnWjT')

cursor = con.cursor()

password = b'jeff221988' # O PASSWORD DO USUÁRIO DEVE SEGUIR ANTES COM O 'b' repassar a string em bytes

print(password)

salt = gensalt() # O salt é uma sequência aleatória de caracteres que é adicionada à senha antes de criptografá-la. Isso ajuda a tornar o hash único, mesmo para senhas idênticas
print(salt)

senhaCripto = hashpw(password, salt) #com a string em bytes a função hashpw converterá a senha para cripto + o salt pra aumentar a segurança da senha

senhaCripto = senhaCripto.decode('utf-8')

print(senhaCripto)

# senhaDigitada = '1234'
# senhaDigitada = senhaDigitada.encode('utf-8') 



cursor.execute(f'''UPDATE signin SET senha = '{senhaCripto}' where func_id = '7';''')
con.commit()

# cursor.execute(f'''SELECT senha from signin where func_id = '13';''')
# senhaBanco = cursor.fetchone()[0].encode('utf-8')
# print(senhaBanco)

# boleano = checkpw(senhaDigitada, senhaBanco)

# print(boleano)
