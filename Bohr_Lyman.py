# Υπολογισμός ενεργειακών καταστάσεων
def energy(n):
    return -13.6 / (n ** 2)  # Τύπος του Bohr σε eV

# Λίστα με τιμές του κύριου κβαντικού αριθμού n
quantum_numbers = [1, 2, 3, 4]

# Υπολογισμός ενέργειας για κάθε επίπεδο
for n in quantum_numbers:
    print(f"Ενέργεια για n={n}: {energy(n):.2f} eV")

# Υπολογισμός ενεργειών μετάπτωσης στη σειρά Lyman (n → 1)
n_final = 1  # Το τελικό επίπεδο για τη σειρά Lyman

for n in quantum_numbers:
    if n > n_final:  
        energy_transition = energy(n) - energy(n_final)
        print(f"Ενέργεια μετάπτωσης για n={n} → n={n_final}: {energy_transition:.2f} eV")