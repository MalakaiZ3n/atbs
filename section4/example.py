def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error: You tried to divide by an invalid number.')
#Like Zero
        
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
