Online obchod s administrátorským panelem
Stručný popis systému
Součástí tohoto projektu je vytvoření aplikace, která umožní přidávat produkty do nabídky obchodu skrze administrátorský panel, umožní registraci uživatele, přihlašování do uživatelského účtu a vytváření objednávek.

Hlavní funkce systému
Přihlašovací panel. Administrátor:

Přidávání kategorií produktů.
Přehled stromu kategorií.
Přidávání produktů.
Seznam produktů + . Uživatel:
Registrace.
Seznam produktů.
Tabulka produktů se stránkováním (číslováním stránek).
Zobrazení počasí v lokalitě uživatele.
Obecné pokyny
Vytvořte webovou stránku s použitím Django. Zaveďte v aplikaci rozdělení na modely, zobrazení a ovladače a pro každý z nich využijte vhodnou logiku. Zabezpečte přístup k aplikaci a jejím funkcím pomocí django.contrib.auth.

Základní entity (návrh)
Kategorie
název
nadřazené kategorie a dceřiné kategorie (umístění ve stromu)
Uživatelský účet
přihlašovací údaje (email)
heslo (hash)
město
adresa (země, město, ulice, PSČ)
logotyp / náhled / avatar
role (ADMINISTRÁTOR/UŽIVATEL - entita)
preferovaný komunikační kanál (pošta / email)
Produkt
název
popis
náhled (url)
kategorie (entita)
cena
typ produktu (enumerace)
autor (entita)
Fronta objednávek
Produkt (entita)
Počet produktů
Cena produktu
Objednávka
Uživatelské jméno
Celková cena
Doručovací adresa
Adresa uživatele
Datum vytvoření objednávky
Fronty objednávek (entita)
Klient (entita)
Status (enumerace)
Autor
Jméno
Příjmení
Role
Název role
Košík (bez entity)
Fronty objednávek
Funkcionality
ADMINISTRÁTOR: Přidání kategorie

název kategorie
rodičovské ID
Přehled stromu kategorií
vyhledávání kategorií
možnost přemisťování kategorií (změna pozice)
Přidávání produktu
název
popis
url obrázku
dostupnost
cena
produktový typ (rozevírací seznam)
kategorie (rozevírací seznam)
autor (rozevírací seznam)
Seznam produktů
seznam všech přidaných produktů s detailními informacemi
tlačítko pro editaci produktu
vyhledávač produktů
UŽIVATEL:
Registrace uživatele
vkládání dat do polí formuláře + validace těchto polí
Přihlášení
Možnosti přihlášení uživatele (po předchozí registraci)
možnost odhlášení uživatele
Widget počasí
zobrazuje počasí v lokalitě, ve které se nachází přihlášený uživatel
Seznam produktů
zobrazuje produkty v podobě seznamu nebo mřížky
vyhledávání produktů
přidání produktu do košíku
Tabulka s produkty (pomocí Ajaxu na dotaz GET a vkládání parametrů do adresy URL)
zobrazení produktů v tabulce se stránkováním
třídění produktů v tabulce
Ajax vyhledávání produktů
přidávání produktů do košíku
Košík
zobrazení produktů přidaných do košíku
možnost objednání produktů z košíku -> vede ke statické stránce s poděkováním a snížení dostupnosti produktu
Další úkoly a rozšíření
editace uživatelského účtu (údaje)
přehled objednávek uživatele (z úrovně uživatele a administrátora)
přidání autora do administrátorského panelu
Dodatečné požadavky
je nutné, aby byly splněny estetické i funkční požadavky projektu
data získávaná od uživatelů by měla být předem ověřena