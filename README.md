# nx-ovlloader (Ryazha edition)

**EN:** Sysmodule that chainloads Tesla overlay menus on Nintendo Switch. Fork of [ppkantorski/nx-ovlloader](https://github.com/ppkantorski/nx-ovlloader) adapted for the Ryazha ecosystem (Ryazhahand-Overlay, RCU, libryazhahand). Adds the Applet memory pool, Applet program type and display-register mapping required by deko3d glass overlays; title ID is preserved. License: ISC. HOS 16.0.0+.

---

## Что это

Core-загрузчик sysmodule для Tesla-совместимых overlay-меню. Стартует с консолью, маппит overlay NRO в память и chainload'ит `/switch/.overlays/ovlmenu.ovl`. Без него Tesla-overlay не запустится.

Этот репозиторий — форк ppkantorski/nx-ovlloader. Title ID `420000000007E51A` сохранён. Manifest использует пул и тип Applet и доступ к регистрам дисплея для оверлеев deko3d. Используйте Ryzhand 2.5.2 и оверлеи `-deko3d` с событиями UEvent; старые версии на событиях ядра требуют обновления.

## Отличия от upstream

- Брендирование (README/CI под Ryazha-проекты).
- Авто-sync workflow `.github/workflows/sync_upstream.yml` — ежедневный cron подтягивает изменения от ppkantorski и открывает PR. Ручной merge не нужен.
- Используется как submodule в `Ryazhahand-Overlay/vendor/nx-ovlloader/`. Релизная сборка тянет наш бинарь, а не online-fetch из upstream releases.

## Установка

Если используешь Ryazhahand-Overlay (релиз `sdout.zip`) — nx-ovlloader уже включён в bundle, ничего отдельно ставить не нужно.

Если ставишь руками:

1. Скачать релиз → распаковать в корень SD.
2. Структура:
   - `atmosphere/contents/420000000007E51A/exefs.nsp` — sysmodule.
   - `atmosphere/contents/420000000007E51A/flags/boot2.flag` — авто-старт при boot.
   - `atmosphere/contents/420000000007E51A/toolbox.json` — manifest для Tesla-launcher'ов.
3. Перезагрузить консоль.

## Сборка из исходников

```sh
git clone https://github.com/Dimasick-git/nx-ovlloader.git
cd nx-ovlloader
export DEVKITPRO=/opt/devkitpro
make
```

Результат — SD-структура в `out/`; `make dist` создаёт `nx-ovlloader.zip`. Права скомпилированного NPDM проверяются перед упаковкой.

## Лицензия

ISC. См. `LICENSE.md`.

Авторы: ppkantorski (upstream), Atmosphere-NX (loader-base), switchbrew (libnx), Dimasick-git (Ryazha-rebrand + sync workflow).
