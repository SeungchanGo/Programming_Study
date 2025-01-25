table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
		 ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
		 ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
		 ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
		 ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..')]


def encode(ch):
	idx = ord(ch.upper()) - ord('A')  #리스트에서 해당 문자의 인덱스
	return table[idx][1]    # 해당 문자의 모스 부호 반환


def decode(cd):
	for e in table:  # 모스 코드 표의 모든 문자에 대해
		if e[1] == cd: # 찾는 코드와 같으면
			return e[0]  # 그 코드의 문자를 반환


print(encode('A'))
print(decode('.-'))

str = input()
mlist = []
for code in str:
	mlist.append(encode(code))
print(mlist)

for morse in mlist:
	print(decode(morse), end="")
print()