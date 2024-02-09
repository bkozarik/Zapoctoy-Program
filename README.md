# Dokumentace

## Úvod do L-systémů

L-systémy, nebo Lindenmayerovy systémy, jsou typem formální gramatiky, která se používá k popisu růstu rostlin nebo fraktálních struktur. Byly navrženy v roce 1968 Aristidem Lindenmayerem, holandským biologem, jako způsob modelování chování rostlinných buněk. L-systémy se vyznačují sadou pravidel, která iterativně transformují počáteční řetězec (axiom) na složitější struktury. Tyto systémy najdou uplatnění v počítačové grafice pro generování fraktálů a simulaci přírodních struktur.

## Fraktály založené na L-systémech

### Gosperova křivka
Logika: Gosperova křivka, známá také jako Peano-Gosperova křivka, je fraktální křivka, která se rozšiřuje tím, že nahrazuje každý segment křivky složitějším vzorem. Tento proces se opakuje v několika iteracích, což vede ke komplexnímu a detailnímu vzoru. Gosperova křivka je příkladem křivky, která vyplňuje prostor a může být použita pro vytvoření 2D drakonické dlaždice.

### Hilbertova křivka
Logika: Hilbertova křivka je fraktální křivka, která postupně vyplňuje čtvercovou plochu. V každé iteraci se každý segment křivky nahradí vzorem, který zahrnuje čtyři menší části původního segmentu, propojené tak, aby vytvořily složitější a hustší strukturu. Hilbertova křivka je známá svou schopností minimalizovat vzdálenost mezi sousedními body, což ji činí užitečnou v různých aplikacích, včetně optimalizace úložiště dat.

### Kochova antivločka
Logika: Kochova antivločka je varianta klasické Kochovy vločky, kde je střední část každého segmentu nahrazena dvěma segmenty vytvářejícími výčnělek ven z původního tvaru. Tím se vytvoří "negativní" prostor ve tvaru vločky, což dává celé struktuře charakteristický vzhled. Každá iterace zvětšuje komplexitu obrysu tím, že přidává více výčnělků.

### Kochova křivka
Logika: Kochova křivka je jedním z nejjednodušších příkladů fraktálu, který demonstruje, jak se z jednoduchého segmentu může stát složitá, nekonečně se opakující struktura. Každý segment je nahrazen čtyřmi segmenty, které tvoří "zub" směřující ven. Tento proces se opakuje pro každý segment vytvořený v předchozí iteraci, což vede k exponenciálnímu zvýšení detailů a délky křivky.

### Kochova vločka
Logika: Kochova vločka rozšiřuje koncept Kochovy křivky tím, že aplikuje stejná pravidla na každou stranu rovnostranného trojúhelníku. Výsledkem je komplexní, symetrický vzor, který připomíná sněhovou vločku. S každou iterací se obvod vločky stává stále detailnějším, zatímco plocha zůstává relativně konstantní.

### Strom
Logika: Fraktální stromy jsou generovány pomocí L-systémů tak, že se modeluje růst od základny (kmene) k větvím a listům. Pravidla L-systému definují, jak se segmenty stromu rozdělují a rozšiřují do různých úhlů, což imituje přirozený růst stromů. Tento proces vytváří realistické struktury, které mohou reprezentovat různé typy stromů v závislosti na použitých pravidlech a parametrech.




# Uživatelská dokumentace pro spuštění programu fraktálů

## Předpoklady

Než začnete, ujistěte se, že máte nainstalovaný Python 3 na vašem systému. Program využívá knihovnu Turtle pro vykreslování, která je součástí standardní instalace Pythonu.

## Stažení programu

Stáhněte si zdrojové kódy programu fraktálů, včetně main.py a všech souborů s fraktály na váš počítač.

## Spuštění programu

#### Otevřete příkazový řádek nebo terminál ve vašem operačním systému.
#### Přejděte do složky, kam jste si stáhli program. Můžete použít příkaz cd cesta/k/složce pro navigaci.
#### Spusťte program zadáním příkazu python main.py a stiskněte Enter. Ujistěte se, že používáte verzi Pythonu 3, pokud máte na systému instalováno více verzí, můžete potřebovat použít příkaz python3 main.py.

## Použití programu
Po spuštění main.py se objeví menu s výběrem dostupných fraktálů. Každý fraktál je přiřazen číslu. Postupujte podle těchto kroků pro vykreslení fraktálu:

### Zobrazí se vám seznam fraktálů s číslem vedle každého názvu. Například:
##### 1: Gosperova křivka
##### 2: Hilbertova křivka
##### 3: Kochova antivločka
##### ...

#### Vyberte fraktál, který chcete vykreslit, zadáním čísla odpovídajícího vašemu výběru a stiskněte Enter.
#### Po zadání všech potřebných údajů program začne s vykreslováním zvoleného fraktálu pomocí Turtle grafiky. Vykreslení může chvíli trvat v závislosti na složitosti fraktálu a počtu iterací.
#### Po dokončení vykreslení můžete okno Turtle grafiky zavřít a vrátit se do příkazové řádky nebo terminálu.

## Ukončení programu

Pro ukončení programu zavřete okno Turtle grafiky, pokud je otevřené, a v příkazové řádce nebo terminálu stiskněte Ctrl+C nebo jednoduše zavřete terminál.

