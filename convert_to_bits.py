# ============================================
# FUNÇÕES DE CONVERSÃO (definidas ANTES de usar)
# ============================================

def char_para_bits_8(caractere):
    """Converte um caractere para string de bits (8 bits - ASCII)"""
    codigo = ord(caractere)
    return f"{codigo:08b}"

def char_para_bits_16(caractere):
    """Converte um caractere para string de bits (16 bits - UTF-16)"""
    codigo = ord(caractere)
    return f"{codigo:016b}"

def char_para_bits_32(caractere):
    """Converte um caractere para string de bits (32 bits - UTF-32/Unicode completo)"""
    codigo = ord(caractere)
    return f"{codigo:032b}"

def bits_para_char(bits):
    """Converte string de bits para caractere"""
    codigo = int(bits, 2)
    return chr(codigo)

def string_para_bits(texto, bits=8):
    """Converte string completa para lista de bits com tamanho especificado"""
    if bits == 8:
        return [char_para_bits_8(c) for c in texto]
    elif bits == 16:
        return [char_para_bits_16(c) for c in texto]
    elif bits == 32:
        return [char_para_bits_32(c) for c in texto]
    else:
        raise ValueError("Bits deve ser 8, 16 ou 32")

def bits_para_string(lista_bits):
    """Converte lista de bits de volta para string"""
    return ''.join(bits_para_char(bits) for bits in lista_bits)

def mostrar_comparacao(caractere):
    """Mostra o caractere em diferentes formatos de bits"""
    print(f"\n📌 Caractere: '{caractere}'")
    print(f"   Código Unicode: {ord(caractere)}")
    print(f"   8 bits  (ASCII): {char_para_bits_8(caractere)}")
    print(f"   16 bits (UTF-16): {char_para_bits_16(caractere)}")
    print(f"   32 bits (UTF-32): {char_para_bits_32(caractere)}")


# ============================================
# PROGRAMA PRINCIPAL (MENU INTERATIVO)
# ============================================

print("=" * 60)
print("🔄 CONVERSOR CARACTERE ↔ BITS (8, 16 e 32 bits)")
print("=" * 60)

while True:
    print("\nOpções:")
    print("1 - Caractere para bits (escolher formato)")
    print("2 - Bits para caractere")
    print("3 - String para bits")
    print("4 - Comparar formatos (8, 16 e 32 bits)")
    print("5 - Sair")
    
    opcao = input("\nEscolha: ")
    
    if opcao == '1':
        char = input("Digite um caractere: ")
        if len(char) == 1:
            print(f"\nFormato de bits para '{char}':")
            print(f"8 bits:  {char_para_bits_8(char)}")
            print(f"16 bits: {char_para_bits_16(char)}")
            print(f"32 bits: {char_para_bits_32(char)}")
            print(f"Decimal: {ord(char)}")
        else:
            print("❌ Digite apenas UM caractere!")
    
    elif opcao == '2':
        bits = input("Digite os bits (ex: 00000000000000000000000001000001 para 32 bits): ")
        try:
            # Verifica se tem apenas 0s e 1s
            if not all(b in '01' for b in bits):
                print("❌ Use apenas 0s e 1s!")
            else:
                num = int(bits, 2)
                char = chr(num)
                print(f"\n{bits}")
                print(f"→ Decimal: {num}")
                print(f"→ Caractere: '{char}'")
        except ValueError:
            print("❌ Bits inválidos! Verifique se o valor é válido para Unicode.")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    elif opcao == '3':
        texto = input("Digite um texto: ")
        print("\nQual formato de bits?")
        print("1 - 8 bits (ASCII)")
        print("2 - 16 bits (UTF-16)")
        print("3 - 32 bits (UTF-32)")
        fmt = input("Escolha: ")
        
        if fmt == '1':
            bits_lista = string_para_bits(texto, 8)
            print(f"\nBits (8 bits cada):")
            for i, char in enumerate(texto):
                print(f"'{char}' → {bits_lista[i]}")
        
        elif fmt == '2':
            bits_lista = string_para_bits(texto, 16)
            print(f"\nBits (16 bits cada):")
            for i, char in enumerate(texto):
                print(f"'{char}' → {bits_lista[i]}")
        
        elif fmt == '3':
            bits_lista = string_para_bits(texto, 32)
            print(f"\nBits (32 bits cada):")
            for i, char in enumerate(texto):
                print(f"'{char}' → {bits_lista[i]}")
        else:
            print("❌ Opção inválida!")
    
    elif opcao == '4':
        texto = input("Digite um texto (máximo 5 caracteres): ")
        print("\n" + "=" * 80)
        print(f"{'Caractere':<10} {'Decimal':<8} {'8 bits':<12} {'16 bits':<18} {'32 bits':<35}")
        print("=" * 80)
        for char in texto[:5]:
            print(f"{char:<10} {ord(char):<8} {char_para_bits_8(char):<12} {char_para_bits_16(char):<18} {char_para_bits_32(char):<35}")
    
    elif opcao == '5':
        print("Até mais! 👋")
        break
    
    else:
        print("❌ Opção inválida! Escolha 1, 2, 3, 4 ou 5.")