# Guardian

Aplikacja do ograniczania czasu korzystania z komputera przez dziecko – pierwsza poważna rzecz, którą napisałem w Pythonie.

Projekt powstał w 2016 roku, gdy mój 11-letni syn spędzał za dużo czasu grając w nocy.  
Nie było wtedy dobrych darmowych narzędzi po polsku, więc napisałem własne.  
To był mój pierwszy poważny program, który naprawdę komuś (synowi) utrudnił życie i jednocześnie mnie nauczył myślenia o zabezpieczeniach (threat model, obejścia, słabe ogniwa).

Został w oryginalnej formie – bez zmian i bez upiększania.

### Co robiły wersje

- v1.0 – lokalna data systemowa (łatwo obejść zmianą zegara)
- v2.0 – data z internetu + sprawdzanie netu (na moment pisania w 2016 roku nie do obejścia)

## Wersja 1.0 (pierwsza, podstawowa)

- Na starcie systemu zapisuje aktualną datę **z systemu lokalnego** do pliku tekstowego.
- Porównuje trzy ostatnie wpisy w pliku.
- Jeśli daty są różne → pozwala korzystać z komputera przez 1 godzinę, po czym wyłącza komputer.
- Jeśli daty są takie same → wyłącza komputer po 1 minucie (z możliwością zatrzymania aplikacji).
- Ukrywa okno konsoli za pomocą skryptu VBS.
- Słaby punkt: wystarczy zmienić datę systemową, żeby obejść limit.

## Wersja 2.0 (ulepszona, działająca przez miesiące)

- Na starcie systemu **sprawdza, czy jest połączenie z internetem** (jeśli nie – czeka 5 sekund i sprawdza ponownie).
- Gdy internet jest → pobiera aktualną datę **z internetu** (nie z zegara systemowego).
- Zapisuje tę datę do pliku tekstowego.
- Dalej działa tak samo jak v1.0: porównuje trzy ostatnie wpisy → 1 godzina przy różnych datach, 1 minuta przy tej samej.
- Ukrywa okno konsoli (VBS wrapper).
- Kluczowa zmiana: zmiana zegara systemowego już nie pomaga, bo data pochodzi z sieci.

Wersja 2.0 powstała po tym, jak syn odkrył i obejść v1.0 (zmiana roku w systemie).  
Dzięki pobraniu daty z internetu i sprawdzaniu połączenia aplikacja stała się znacznie trudniejsza do obejścia – przetrwała wiele prób i działała przez kilka miesięcy.

## Uruchomienie

- Skrypt Python → skompilowany do .exe (np. pyinstaller)
- Dodany do autostartu Windows
- Ukrywanie okna CMD przez VBS

## Uwagi

W takim środowisku (brak jakiekolwiek wiedzy o aplikacji + brak interaktywnego wsparcia) – moja aplikacja była rzeczywiście blisko ideału dla tego konkretnego scenariusza.
To, co w 2026 roku wydaje się łatwe do obejścia (użycie AI) – w 2016 dla grupy dzieciaków było praktycznie poza zasięgiem.
W tamtych warunkach i dla tamtego użytkownika to było dzieło bardzo dobrze przemyślane i skuteczne.
Nie była to wielka aplikacja, ale na poziomie „rodzic vs 11-latek + kumple” – działała rewelacyjnie długo.
To jest dowód na to, że dobry threat model nie musi być skomplikowany – wystarczy dobrze zrozumieć przeciwnika i jego możliwości.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file.

**Attribution appreciated:** If you use this code, a link back to this repo
would be awesome (but not required). It helps other developers find the original
work and supports independent creators like me.
