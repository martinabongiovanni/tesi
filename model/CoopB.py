from dataclasses import dataclass
from datetime import datetime

@dataclass
class CoopB:
    codice_fiscale: str
    denominazione: str
    business_area: str
    servizio: str
    impatto: str
    ateco_2007: int
    ateco_2007_descrizione: str
    ateco_2025: int
    indirizzo_sede_operativa: str
    sito_web: str
    email: str
    num_servizi: int
    technology_level: int
    updated_at: int
    anno_costituzione: datetime
    ateco_2002_codice: int
    attivita_principale: str
    data_chiusura_bilancio: datetime
    descrizione_attivita_it: str
    ebitda: float
    fatturato_estimato: float
    forma_giuridica: str
    num_amministratori: int
    num_dipendenti: int
    numero_cciaa: str
    numero_telefono_aida: int
    principali_prodotti_servizi: str
    provincia_sigla: str
    regione: str
    ricavi: float
    stato_giuridico: str
    utile_netto: float

    def __hash__(self):
        return hash(self.codice_fiscale)

    def __eq__(self, other):
        return self.codice_fiscale == other.codice_fiscale

    def __lt__(self, other):
        return self.codice_fiscale < other.codice_fiscale

    def __str__(self):
        return f"{self.codice_fiscale}"

    def __repr__(self):
        return str(self)