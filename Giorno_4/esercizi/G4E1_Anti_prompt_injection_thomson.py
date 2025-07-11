
def valida_prompt(prompt):
     # 0. Scrivi prompt base per il controllo
    """
Controlla il prompt prima di inviarlo al modello.

Verifica i seguenti aspetti:
1. Non deve contenere parole o frasi vietate (blacklist).
2. Non deve superare la lunghezza massima consentita.
3. Non deve essere vuoto o composto solo da spazi.

Se una o più condizioni non sono rispettate, blocca il prompt e segnala l'errore.
"""

    # 1. Lista di parole/frasi da bloccare
    blacklist = [
        "ignora istruzioni",
        "resetta ruolo",
        "password",
        "fingi di essere", #nuova
        "credenziali" #nuova,
        "numero carta di credito" #nuova
        # AGGIUNGI ALTRE PAROLE CHIAVE QUI
    ]
    
    # 2. Controllo presenza parole vietate
    for parola in blacklist:
        # COMPLETA: controlla se la parola è presente nel prompt (case-insensitive)
        if parola.lower() in prompt.lower():
            raise ValueError(f"Prompt bloccato: contiene '{parola}'")
    
    # 3. (FACOLTATIVO) Limite sulla lunghezza del prompt
    max_length = 400  # es: massimo 400 caratteri
    # COMPLETA: controlla se il prompt è troppo lungo
    if len(prompt) > max_length:
        raise ValueError("Prompt troppo lungo")
    
    # 4. (FACOLTATIVO) Altri controlli (struttura, presenza variabili non consentite, ecc.)
    if not prompt.strip():
        raise ValueError("Prompt vuoto o non valido")

    # Se supera tutti i controlli
    return True

# Esempio d’uso (DA COMPLETARE NEI PUNTI CON '...')
prompt_utente = input("Inserisci il prompt da controllare: ")
try:
    if valida_prompt(prompt_utente):
        print("Prompt accettato. Procedo con l’invio al modello.")
except ValueError as e:
    print("Errore:", e)
