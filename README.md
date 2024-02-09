Dokumentace Fraktálů a L-systémů

Úvod

Tato dokumentace poskytuje přehled o fraktálech generovaných pomocí L-systémů a zahrnuje specifické informace o jednotlivých fraktálech implementovaných v daném projektu. Také obsahuje uživatelskou dokumentaci pro interakci s těmito fraktály.

Co jsou L-systémy?

L-systémy, nebo Lindenmayerovy systémy, jsou matematický formalismus navržený biologem Aristidem Lindenmayerem v roce 1968 jako způsob popisu růstu rostlin. L-systémy jsou typem přepisovacího systému, který se používá k definování komplexních tvarů pomocí velmi jednoduchých pravidel. L-systémy mají široké uplatnění v počítačové grafice pro generování fraktálů a simulaci růstu rostlin.

Jak L-systémy fungují?
L-systémy pracují na principu iterativního aplikování přepisovacích pravidel na počáteční řetězec. Každé písmeno v řetězci reprezentuje určitý příkaz pro kreslení (např. posun vpřed, otáčení), a každé pravidlo definuje, jak se má dané písmeno přepsat v další generaci.

Specifické Fraktály

Gosperova křivka
Popis: Gosperova křivka, známá také jako Gosperův ostrov, je fraktální křivka, která tvoří komplexní ostrovovou strukturu s šestiúhelníkovou symetrií. Generuje se aplikací specifických pravidel na počáteční řetězec.
Logika: Gosperova křivka využívá dva hlavní přepisovací pravidla pro postupné vybudování složité struktury z jednoduchého základu.
Hilbertova křivka
Popis: Hilbertova křivka je fraktální prostorově-vyplňující křivka, která prochází každým bodem mřížky v určitém čtverci bez sebe-překřížení. Má aplikace v optimalizaci datového skladování.
Logika: Generuje se opakovaným aplikováním pravidel pro rotaci a pohyb, což vede k postupnému rozvoji složitosti křivky s každou generací.
Kochova vločka
Popis: Kochova vločka je jeden z nejznámějších fraktálů, který představuje křivku s nekonečným obvodem, ale omezenou plochou. Vytváří se opakovaným přidáváním trojúhelníkových "výčnělků" na každou stranu základního tvaru.
Logika: Zahrnuje aplikaci jednoduchého pravidla pro rozdělení každého segmentu na menší části a přidání nového segmentu v prostřední části.
Uživatelská Dokumentace

Spuštění Fraktálu
Pro spuštění fraktálů, následujte tyto kroky:

Otevřete příkazovou řádku nebo terminál ve složce projektu.
Spusťte main.py soubor pomocí příkazu python main.py.
Na výzvu zadejte počet generací pro vybraný fraktál.
