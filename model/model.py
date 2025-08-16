from typing import List
from model.BusinessArea import BusinessArea


class Model:
    def __init__(self):
        self.lista_combinazioni: List[(str, BusinessArea)] = []

    def associazione_codiceAteco_BusinessArea (self, codice):
        '''
        Questa funzione associa ogni codice ateco, che riceve come parametro, a un oggetto di tipo
        Business area tra:
        P&O (Production and Operations), M&S (Marketing and Sales), R&D (Research and Development),
        F&C (Finance and Control), HR (Human Resources), ICT (Information and Communication Technology),
        CS (Customer Service), LOG (Logistics), G&A (Governance and Administration).
        Più chiamate di questa funzione permettono quindi di costruire una lista di tuple del tipo
        (codice ateco (int), area (Business Area)).

        :return: Oggetto di tipo business area associato al codice passato come parametro, relativo
        quindi all'ultima tupla inserita nella lista.
        Se il codice passato come parametro è già stato analizzato in precedenza (è già nella lista) o
        non è gestito da nessun caso, la funzione restituisce None.
        '''
        # converto il codice ateco passato come parametro in stringa, lo analizzo e lo assegno a una business area
        codice = str(codice)

        # se la lista di combinazioni è ancora vuota
        if len(list(self.lista_combinazioni)) == 0:
            self.logica_assegnazioni(codice)
            return self.lista_combinazioni[0][1]

        # se la lista di combinazioni ha degli elementi,
        # verifico prima che il codice in esame non sia già stato analizzato
        elenco_codici = [combinazione[0] for combinazione in self.lista_combinazioni]
        if codice not in elenco_codici: # not in: per evitare di sovrascrivere codici già analizzati
            self.logica_assegnazioni(codice)
        return self.lista_combinazioni[-1][1]

    def logica_assegnazioni(self, codice):
        '''
        Questa funzione racchiude la logica di assegnazione della business area analizzando il codice.
        :param codice: Codice ateco.
        :return: Inserisce una nuova tupla del tipo (codice, area) nella lista di tuple.
        '''
        if (codice[:2] == "01" or codice[:2] == "02" or codice[:2] == "05" or codice[:2] == "10" or
                codice[:2] == "11" or codice[:2] == "12" or codice[:2] == "13" or codice[:2] == "14" or
                codice[:2] == "15" or codice[:2] == "16" or codice[:2] == "17" or codice[:2] == "18" or
                codice[:2] == "19" or codice[:2] == "20" or codice[:2] == "21" or codice[:2] == "22" or
                codice[:2] == "23" or codice[:2] == "24" or codice[:2] == "25" or codice[:2] == "26" or
                codice[:2] == "27" or codice[:2] == "28" or codice[:2] == "29" or codice[:2] == "30" or
                codice[:2] == "31" or codice[:2] == "32" or codice[:2] == "33" or codice[:2] == "34" or
                codice[:2] == "35" or codice[:2] == "36" or codice[:2] == "37" or codice[:2] == "40" or
                codice[:2] == "41" or codice[:2] == "45" or codice[:3] == "502" or codice[:3] == "504" or
                codice[:3] == "527" or codice[:2] == "55" or codice[:3] == "642" or codice[:2] == "71" or
                codice[:3] == "746" or codice[:3] == "747" or codice[:4] == "7481" or codice[:4] == "7482" or
                codice[:4] == "7485" or codice[:4] == "7487" or codice[:2] == "90" or codice[:2] == "93" or
                codice[:2] == "95" or codice[:2] == "97"):
            self.lista_combinazioni.append((str(codice), BusinessArea("P&O", "Production and Operations", "#6495ed")))
        elif (codice[:3] == "501" or codice[:3] == "503" or codice[:3] == "505" or codice[:2] == "51" or
              codice[:3] == "521" or codice[:3] == "522" or codice[:3] == "523" or codice[:3] == "524" or
              codice[:3] == "525" or codice[:3] == "526" or codice[:3] == "633" or codice[:3] == "634" or
              codice[:2] == "70" or codice[:3] == "744" or codice[:2] == "92"):
            self.lista_combinazioni.append((str(codice), BusinessArea("M&S", "Marketing and Sales", "#ffd700")))
        elif codice[:2] == "73" or codice[:3] == "742" or codice[:3] == "743":
            self.lista_combinazioni.append((str(codice), BusinessArea("R&D", "Research and Development", "#9acd32")))
        elif codice[:2] == "65" or codice[:2] == "66" or codice[:2] == "67" or codice[:3] == "741":
            self.lista_combinazioni.append((str(codice), BusinessArea("F&C", "Finance and Control", "#9370db")))
        elif codice[:3] == "745" or codice[:2] == "80":
            self.lista_combinazioni.append((str(codice), BusinessArea("HR", "Human Resources", "#ffc0cb")))
        elif codice[:2] == "72":
            self.lista_combinazioni.append((str(codice), BusinessArea("ICT", "Information and Communication Technology", "#20b2aa")))
        elif codice[:4] == "7486":
            self.lista_combinazioni.append((str(codice), BusinessArea("CS", "Customer Service", "#c0c0c0")))
        elif (codice[:2] == "60" or codice[:2] == "61" or codice[:2] == "62" or codice[:3] == "631" or
              codice[:3] == "632" or codice[:3] == "641"):
            self.lista_combinazioni.append((str(codice), BusinessArea("LOG", "Logistics", "#ffa500")))
        elif codice[:2] == "75" or codice[:2] == "85" or codice[:2] == "91" or codice[:2] == "99":
            self.lista_combinazioni.append((str(codice), BusinessArea("G&A", "Governance and Administration", "#ff4500")))
        else:  # codice ateco non gestito o già analizzato
            return None

    def get_lista_combinazioni(self):
        return self.lista_combinazioni