nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar.")


### 4. **`if` dentro de `if`** (Estruturas aninhadas)

idade = 20
tem_habilitacao = True

if idade >= 18:
    if tem_habilitacao:
        print("Você pode dirigir.")
    else:
        print("Você precisa de habilitação para dirigir.")
else:
    print("Você é menor de idade.")