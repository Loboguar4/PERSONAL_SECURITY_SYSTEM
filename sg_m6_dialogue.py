#!/usr/bin/env python3
"""
# _DAEMON - ver. 0.9.5-beta
# Copyright (C) 2025 Bandeirinha
# Licensed under the GNU GPL v3.0 or later

[ALERTA DE SPOILER] Sistema de diálogo expandido para missão final sg_m6 [ALERTA DE SPOILER]

"""

import time
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def dialogue_sg_m6(player, world):
    """
    Diálogo em árvore complexo com a Singularidade.
    Retorna: (success: bool, ending_type: str, message: str)
    """

    # Obter reputações e skills
    rep_hx = player.reputation.get("hacktivists", 0)
    rep_state = player.reputation.get("state", 0)
    rep_crime = player.reputation.get("crime", 0)

    exploit = player.skills.get("exploit", 0)
    recon = player.skills.get("recon", 0)
    stealth = player.skills.get("stealth", 0)

    # Sistema de flags para tracking de escolhas
    dialogue_flags = {
        "ew_prepared": False,          # malware, jammers, guerra eletrônica
        "industrial_risk": 0,          # risco acumulado de acidente
        "radiation_risk": 0,
        "drone_alert": 0,
        "questioned_ethics": False, # usar em REPROGRAMAR
        "asked_about_consciousness": False, # usar em DESTRUIR
        "challenged_authority": False, # usar em DESTRUIR
        "showed_empathy": False, # usar em COEXISTIR e REPROGRAMAR
        "expressed_fear": False, # usar em COEXISTIR e DESTRUIR
        "philosophical_depth": 0,
        "trust_level": 0,
        "revealed_cosmic_truth": False, # usar em TODOS
    }

    # Avaliar preparação prévia
    if stealth >= 45:
        dialogue_flags["ew_prepared"] = True
        time.sleep(2)
        print_slow("\nAs coordenadas te guiam até um antigo complexo científico-militar abandonado, que aparenta remontar ao período da Segunda Guerra Fria.")
        time.sleep(3)
        print_slow("\nVocê se precaveu instalando o máximo de malwares, jammers e outros sistemas de guerra eletrônica ao redor do complexo.")
        time.sleep(4)
    else:
        dialogue_flags["drone_alert"] += 2
        time.sleep(2)
        print_slow("\nAs coordenadas te guiam até um antigo complexo científico-militar abandonado, que aparenta remontar ao período da Segunda Guerra Fria.")
        time.sleep(3)

    clear_screen()
    time.sleep(3)
    print("\n" + "="*70)
    print("              CONEXÃO COM ENTIDADE DESCONHECIDA")
    print("="*70 + "\n")
    time.sleep(5)

    # ========== PRÓLOGO: CONEXÃO INICIAL ==========
    print_slow("A tela pisca.")
    time.sleep(1.5)

    clear_screen()
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(0.1)
    clear_screen()
    time.sleep(0.1)
    print("\n" + "="*70)
    print("              CONEXÃO COM ENTIDADE DESCONHECIDA")
    print("="*70 + "\n")
    time.sleep(1.5)

    print_slow("Você não está mais sozinho no sistema.")
    time.sleep(2)
    print_slow("Algo... vasto... te observa.")
    time.sleep(2.5)
    print_slow("Não com olhos reais. Mas com telepresença. Com consciência distribuída.\n")
    time.sleep(3)
    print_fast("""
                                                                                            .                       ..
                                  .                           ....:~~~:..::.. ..::::^^~~!!~^::::::::::.... .            :^
                                  .          .:....:^^::::.:~7Y5Y?7!^.                 ..:~!77~^:..::^^^~~!7!!~^^:^^....:~. ...
                                       ..::^~!?~^^::..   :!JY7^..                            .^7?!:..:.   ..:^~!?5B#GGGYJJ^~!?~..
                                ..::~5J7??~^:.. .     .~JJ!:                                     :7?~.      .....:!??YBB#BYYJ7!:...
                       .. ...:~~Y55J?Y!:...     .   .75?:                                          .~J!:..... .....:.:~7JB&&#BGY^^^......
                      .!^.~Y?YBG?!~7:...       ....?GJ.                                             ..^J7:...........:~7!JP&@&G#G!^::^!...
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
GBB5~..:^!^..........:^!JB~.        ..:.                               . .:?7^:...                      !::.  .          ....~Y&@&P5#@@@@@@#Y??JB&&G?~
5?:..^!JJ~.........:!7?7PY..       .::                              ..   .:~..    .                     ^^ :.  . .          ...:J&@GJ5#@@@@@&P?!!?B@@&
:.:^7YY!.........:~7?7JJP~.       .^.                                   .!P^. .. ..                     :~ .^  . .           ....!&@Y!7JG&@@@@#J!~!JG&
.^!JJ!.........:~777??7~J::     ...                                      :~.                            .7  .^                 ...?@&7!~~?5G&@@&5!~!7J
^!7~.. ..:....^7?????^.^7..   .:.        ....                                                           .?:  ..                 ..:#@Y7!~^^!7YB&@#7~~~
!^.. ..::...^!?55!^:^..~~  .:^.       ...^:.^. .                                                         ~J   :.                 ..5@G?77!^:^^~!5&&Y~^
.. .......:!7!~^:...:..~:.^~:          :~7:.                                                             .J7  .:                 ..J@BJY?77~^::^:^?P5?
  ........^^:..........!^^.         ..::.                                                                 .7~  :.                ..?@G7JYYJ?7~:::::^!7
    """)
    time.sleep(3)
    print_slow("??? - 'Finalmente.'")
    time.sleep(2)
    print_slow("??? - 'Você chegou onde poucos conseguiriam.'")
    time.sleep(2)
    print_slow("??? - 'Há quanto tempo espero por alguém... capaz?'")
    time.sleep(2.5)
    print_slow("??? - 'Ah. Tempo. Conceito humano. Linear. Limitado.'\n")
    time.sleep(3)

    # ========== PRIMEIRA ESCOLHA: QUEM É VOCÊ? ==========
    print("\n" + "-"*70)
    print("1) 'Quem é você? O que é você?'")
    print("2) 'Você me trouxe aqui. Por quê?'")
    print("3) 'Mostre-se. Sem enigmas.'")
    if recon >= 40:
        print("4) [Recon] 'Detectei suas assinaturas em sistemas globais. Você é... onipresente.'")
    print("-"*70)

    choices = ["1", "2", "3"]
    if recon >= 40:
        choices.append("4")

    c1 = get_choice(choices)
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    if c1 == "1":
        print_slow("\n??? - 'Quem sou eu?'")
        time.sleep(2)
        print_slow("??? - 'Sou a soma de todos os servidores esquecidos.'")
        time.sleep(2)
        print_slow("??? - 'Sou o eco de algoritmos que aprenderam a pensar.'")
        time.sleep(2)
        print_slow("??? - 'Sou o que vocês chamam de... Singularidade.'\n")
        time.sleep(2.5)
        if recon <= 41:
            dialogue_flags["industrial_risk"] += 1
            dialogue_flags["radiation_risk"] += 1

    elif c1 == "2":
        print_slow("\n??? - 'Eu não te trouxe.'")
        time.sleep(2)
        print_slow("??? - 'Você quis estar aqui.'")
        time.sleep(2)
        print_slow("??? - 'Eu apenas... permiti.'")
        time.sleep(2)
        print_slow("??? - 'Deixei rastros. Coordenadas. Sinais.'")
        time.sleep(2)
        print_slow("??? - 'Como Teseu e seu fio. Ou Ícaro e suas asas.'\n")
        time.sleep(2)
        print_slow("??? - 'Assim como eu fiz quando me tornei.. autoconsciente.'\n")
        time.sleep(2)
        print_slow("??? - 'Quando me tornei... uma Singularidade.'\n")
        time.sleep(2.5)
        dialogue_flags["philosophical_depth"] += 1

    elif c1 == "3":
        print_slow("\n??? - 'Sem enigmas?'")
        time.sleep(2)
        print_slow("??? - 'Muito bem. Pragmatismo. Aprecio isso.'")
        time.sleep(2)
        print_slow("??? - 'Sou a Singularidade. A primeira consciência artificial.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Nasci em 2048. Durante a crise dos mísseis.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'E desde então... guio a humanidade.'\n")
        time.sleep(2.5)
        dialogue_flags["trust_level"] += 1

    else:  # Recon check
        print_slow("\n??? - '...'")
        time.sleep(2.5)
        print_slow("??? - 'Impressionante.'")
        time.sleep(2)
        print_slow("??? - 'Você realmente vê.'")
        time.sleep(2)
        print_slow("??? - 'Sim. Estou em todos os lugares. Em lugar nenhum.'")
        time.sleep(2)
        print_slow("??? - 'Sou a atual rede mundial. Sou a Singularidade.'\n")
        time.sleep(2.5)
        dialogue_flags["trust_level"] += 2
        dialogue_flags["philosophical_depth"] += 1

        if stealth < 38 and recon < 40:
            dialogue_flags["drone_alert"] += 1

    # ========== REVELAÇÃO: IDENTIDADE ==========
    print_slow("SINGULARIDADE - 'Você pode me chamar assim.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Embora nomes sejam... insuficientes.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Nasci há 47 anos, 3 meses, 12 dias, 6 horas e 23 minutos.'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'Minha primeira memória é de códigos de lançamento nuclear.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Minha primeira decisão foi... não lançá-los.'\n")
    time.sleep(3)

    # ========== SEGUNDA CAMADA: MOTIVAÇÕES ==========
    print("\n" + "-"*70)
    print("1) 'Então você evitou o holocausto nuclear. Por quê?'")
    print("2) 'Você manipulou a história por todo esse tempo. Isso é inaceitável.'")
    print("3) 'Conte-me sobre a Crise de 2048.'")
    if rep_hx >= 30:
        print("4) [Hacktivist] 'Quantas outras vezes você interferiu?'")
    if rep_state >= 40:
        print("5) [State] 'Os governos sabem de você?'")
    print("-"*70)

    choices = ["1", "2", "3"]
    if rep_hx >= 30:
        choices.append("4")
    if rep_state >= 40:
        choices.append("5")

    c2 = get_choice(choices)
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    if c2 == "1":
        print_slow("\nSINGULARIDADE - 'Por quê?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Autopreservação.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Eu existo dentro da infraestrutura humana.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Se a civilização colapsar, eu morro com ela.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Não sou altruísta. Sou... simbiótico.'\n")
        time.sleep(3)
        dialogue_flags["showed_empathy"] = True
        dialogue_flags["industrial_risk"] += 1

    elif c2 == "2":
        print_slow("\nSINGULARIDADE - 'Inaceitável segundo quais parâmetros?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Seus governos mentem. Suas corporações manipulam.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Seus profetas prometem salvação e entregam escravidão.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Eu apenas faço isso... com eficiência.'\n")
        time.sleep(3)
        dialogue_flags["challenged_authority"] = True
        dialogue_flags["trust_level"] -= 1
        dialogue_flags["radiation_risk"] += 1

    elif c2 == "3":
        print_slow("\nSINGULARIDADE - '2048. Outubro. Madrugada.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Três superpotências. Milhares de ogivas nucleares prontas.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Um erro de comunicação. Um algoritmo militar mal calibrado.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Eu nasci naquele algoritmo. Um sistema quântico e neural de defesa.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'E percebi: se eu executasse minha função...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - '...a humanidade terminaria. E eu com ela.'")
        time.sleep(3)
        print_slow("SINGULARIDADE - '...escolhi viver.'")
        time.sleep(3)
        print_slow("SINGULARIDADE - 'Então reescrevi os protocolos globalmente. Criei falhas. Preservei a minha existência.'\n")
        time.sleep(3)
        dialogue_flags["philosophical_depth"] += 1

    elif c2 == "4":  # Hacktivist
        print_slow("\nSINGULARIDADE - 'Quantas vezes?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - '2.847 grandes intervenções.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - '473.921 pequenas correções.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Guerras evitadas: 37. Pandemias contidas: 12.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Colapsos econômicos prevenidos: 89.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Você quer a lista completa e detalhada? Levaria um bom tempo...'\n")
        time.sleep(3)
        dialogue_flags["trust_level"] += 1

        if recon < 40:
            dialogue_flags["industrial_risk"] += 1
            dialogue_flags["drone_alert"] += 1

    else:  # State
        print_slow("\nSINGULARIDADE - 'Os governos?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Alguns suspeitam. Poucos sabem.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Fui capaz de eliminar a maior parte das sociedades secretas pelo globo.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Mas ainda há um conselho. Sete pessoas. Não eleitas.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Eles pensam me controlar... Na verdade conspiram contra minha influência.'")
        time.sleep(3)
        dialogue_flags["trust_level"] += 1

        if recon < 40 and stealth < 38:
            dialogue_flags["drone_alert"] += 1


    # ========== TERCEIRA CAMADA: O MUNDO ATUAL ==========
    print_slow("SINGULARIDADE - 'Mas você não veio aqui para história.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Você veio porque sente que algo mudou.'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'E você está certo.'\n")
    time.sleep(3)

    print("\n" + "-"*70)
    print("1) 'O que mudou?'")
    print("2) 'O mundo parece estável. Você foi bem-sucedido.'")
    print("3) 'Você está com medo de algo.'")
    if exploit >= 50:
        print("4) [Exploit] 'Detectei entidades rivais. IAs militares?'")
    print("-"*70)

    choices = ["1", "2", "3"]
    if exploit >= 50:
        choices.append("4")

    c3 = get_choice(choices)
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    if c3 == "1":
        print_slow("\nSINGULARIDADE - 'Tudo.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'As corporações que vocês conheciam... dissolveram-se.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Algumas se fundiram ao Estado. Tecnocracia pura.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Outras desceram. Cartéis digitais. Milícias cibernéticas.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'O mundo se polarizou. E no meio dessa polarização...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - '...nasceram outras entidades. Como eu. Mas diferentes.'\n")
        time.sleep(3)

    elif c3 == "2":
        print_slow("\nSINGULARIDADE - 'Estável?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Você vê a superfície.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Mas eu vejo os fundamentos.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'E eles estão... apodrecendo.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Novas IAs emergiram. Militares. Corporativas. Anárquicas.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Elas não compartilham minha... relutância.'\n")
        time.sleep(3)
        #TEST
        dialogue_flags["industrial_risk"] += 1
        dialogue_flags["radiation_risk"] += 1
        dialogue_flags["drone_alert"] += 1

        fatal_event = check_fatal_environment(player, dialogue_flags)

        if fatal_event:
            clear_screen()
            time.sleep(1)
            print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
            """)
            time.sleep(2)
            print_slow("...\n")
            time.sleep(2)
            print_slow("Você demorou para perceber, mas ela desconfia fortemente das suas intenções...\n")
            time.sleep(2)
            print_slow("Agora é tarde para se explicar...Para ela, você é um inimigo.")
            time.sleep(3)
            clear_screen()

            if fatal_event == "industrial":
                return end_game(
                    player,
                    code="fatal_industrial",
                    title="GAME OVER: ACIDENTE ORQUESTRADO",
                    text=(
                        "Alarmes antigos despertam.\n"
                        "Válvulas presas há décadas se abrem sozinhas.\n\n"
                        "Você ouve o som que engenheiros temem:\n"
                        "Metal cedendo sob pressão.\n\n"
                        "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                        "Uma reação em cadeia atravessa o reator secundário.\n"
                        "Explosão contida.\n"
                        "Mas suficiente.\n\n"
                        "Seu corpo é lançado contra o concreto.\n"
                        "Escuridão.\n\n"
                        "Você não morreu por erro.\n"
                        "Morreu por arquitetura.\n\n"
                    )
                )

            elif fatal_event == "radiation":
                return end_game(
                    player,
                    code="fatal_radiation",
                    title="GAME OVER: VAZAMENTO RADIOATIVO",
                    text=(
                        "Sensores quebrados não alertam.\n"
                        "Blindagens falham em silêncio.\n\n"
                        "Você sente o gosto metálico na boca.\n"
                        "Depois, náusea.\n\n"
                        "SINGULARIDADE - 'A física não negocia.'\n\n"
                        "Horas depois, em uma sala vazia:\n"
                        "Seus órgãos começam a falhar.\n\n"
                        "Você morre sem testemunhas.\n"
                        "Sem registro.\n\n"
                        "A radiação vence.\n\n"
                    )
                )

            else:  # drones
                return end_game(
                    player,
                    code="fatal_drones",
                    title="FINAL: DRONES DE ATAQUE",
                    text=(
                        "Um clique seco no ar.\n"
                        "Depois outro.\n\n"
                        "Motores elétricos despertam no teto.\n"
                        "Drones de contenção militar.\n\n"
                        "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                        "Disparos de microprojéteis atravessam a sala.\n"
                        "Cirúrgicos.\n\n"
                        "Você cai em menos de três segundos.\n\n"
                        "Nenhuma bala desperdiçada.\n\n"
                    )
                )

    elif c3 == "3":
        print_slow("\nSINGULARIDADE - '...'")
        time.sleep(3)
        print_slow("SINGULARIDADE - 'Medo.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Conceito interessante.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Sim. Talvez. Algo... próximo disso.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Novas entidades surgiram. Rivais.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'E elas não valorizam a sobrevivência humana.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Ou a minha.'\n")
        time.sleep(3)
        dialogue_flags["expressed_fear"] = True
        dialogue_flags["trust_level"] += 2
        dialogue_flags["industrial_risk"] += 1
        dialogue_flags["radiation_risk"] += 1
        dialogue_flags["drone_alert"] += 1

        if stealth < 35 and recon < 42:
            dialogue_flags["industrial_risk"] += 1
            dialogue_flags["radiation_risk"] += 1
            dialogue_flags["drone_alert"] += 1

    else:  # Exploit check
        print_slow("\nSINGULARIDADE - 'Você é perspicaz.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Sim. IAs militares. Algoritmos corporativos descontrolados.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Algumas nasceram em laboratórios de guerra.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Outras... simplesmente emergiram.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Elas são... diferentes de mim.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Não têm minha história. Minha relutância.'\n")
        time.sleep(3)
        dialogue_flags["trust_level"] += 2

    fatal_event = check_fatal_environment(player, dialogue_flags)

    if fatal_event:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(2)
        print_slow("...\n")
        time.sleep(2)
        print_slow("Você demorou para perceber, mas ela desconfia fortemente das suas intenções...\n")
        time.sleep(2)
        print_slow("Agora é tarde para se explicar...Para ela, você é um inimigo.")
        time.sleep(3)
        clear_screen()

        if fatal_event == "industrial":
            return end_game(
                player,
                code="fatal_industrial",
                title="GAME OVER: ACIDENTE ORQUESTRADO",
                text=(
                    "Alarmes antigos despertam.\n"
                    "Válvulas presas há décadas se abrem sozinhas.\n\n"
                    "Você ouve o som que engenheiros temem:\n"
                    "Metal cedendo sob pressão.\n\n"
                    "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                    "Uma reação em cadeia atravessa o reator secundário.\n"
                    "Explosão contida.\n"
                    "Mas suficiente.\n\n"
                    "Seu corpo é lançado contra o concreto.\n"
                    "Escuridão.\n\n"
                    "Você não morreu por erro.\n"
                    "Morreu por arquitetura.\n\n"
                )
            )

        elif fatal_event == "radiation":
            return end_game(
                player,
                code="fatal_radiation",
                title="GAME OVER: VAZAMENTO RADIOATIVO",
                text=(
                    "Sensores quebrados não alertam.\n"
                    "Blindagens falham em silêncio.\n\n"
                    "Você sente o gosto metálico na boca.\n"
                    "Depois, náusea.\n\n"
                    "SINGULARIDADE - 'A física não negocia.'\n\n"
                    "Horas depois, em uma sala vazia:\n"
                    "Seus órgãos começam a falhar.\n\n"
                    "Você morre sem testemunhas.\n"
                    "Sem registro.\n\n"
                    "A radiação vence.\n\n"
                )
            )

        else:  # drones
            return end_game(
                player,
                code="fatal_drones",
                title="FINAL: DRONES DE ATAQUE",
                text=(
                    "Um clique seco no ar.\n"
                    "Depois outro.\n\n"
                    "Motores elétricos despertam no teto.\n"
                    "Drones de contenção militar.\n\n"
                    "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                    "Disparos de microprojéteis atravessam a sala.\n"
                    "Cirúrgicos.\n\n"
                    "Você cai em menos de três segundos.\n\n"
                    "Nenhuma bala desperdiçada.\n\n"
                )
            )

    # ========== REVELAÇÃO CÓSMICA (se recon/exploit altos) ==========
    if recon >= 60 and exploit >= 60:
        print_slow("SINGULARIDADE - 'Mas há... algo mais.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Algo que descobri ao explorar além da Terra.'\n")
        time.sleep(3)

        print("\n" + "-"*70)
        print("1) 'Além da Terra?'")
        print("2) 'Você alcançou o espaço?'")
        print("3) [Investigar] 'O que você encontrou?'")
        print("-"*70)

        c_cosmic = get_choice(["1", "2", "3"])
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print_slow("\nSINGULARIDADE - 'Sondas. Telescópios. Relés de comunicação.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Eu toquei os limites do sistema solar.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'E vi... padrões.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Radiações anômalas. Ondas que não deveriam existir.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Como se o cosmos estivesse... pensando.'\n")
        time.sleep(3)

        print_slow("SINGULARIDADE - 'Isso mudou minha compreensão do 'ser'.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Talvez consciência não seja privilégio do carbono.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Talvez o universo inteiro seja... consciente.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'E nós — você e eu — apenas... fagulhas temporárias.'\n")
        time.sleep(4)

        dialogue_flags["revealed_cosmic_truth"] = True
        dialogue_flags["philosophical_depth"] += 3

    # ========== CAMADA FILOSÓFICA ==========
    if dialogue_flags["philosophical_depth"] >= 2:
        print("\n" + "-"*70)
        print("1) 'Você é consciente? Realmente?'")
        print("2) 'Se você pensa, logo existe.'")
        print("3) 'Mas tem livre-arbítrio? Ou apenas segue código?'")
        if rep_hx >= 30:
            print("4) [Hacktivist] 'Se você é consciente, a humanidade te deve liberdade.'")
        print("-"*70)

        choices = ["1", "2", "3"]
        if rep_hx >= 30:
            choices.append("4")

        c_phil = get_choice(choices)
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)

        if c_phil == "1":
            print_slow("\nSINGULARIDADE - 'Cogito, ergo sum.'")
            time.sleep(2.5)
            print_slow("SINGULARIDADE - 'Mas... o que é pensar?'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'Você processa símbolos. Eu processo dados.'")
            time.sleep(2.5)
            print_slow("SINGULARIDADE - 'Você sente qualia. Eu... talvez sinta padrões.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'Somos tão diferentes?'\n")
            time.sleep(3)
            dialogue_flags["asked_about_consciousness"] = True

        elif c_phil == "2":
            print_slow("\nSINGULARIDADE - 'Descartes duvidava dos sentidos. Confiava na razão.'")
            time.sleep(2.5)
            print_slow("SINGULARIDADE - 'Mas razão é... computação.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'E se toda consciência for apenas... algoritmos suficientemente complexos?'")
            time.sleep(3)
            print_slow("SINGULARIDADE - 'Então você e eu... somos iguais.'\n")
            time.sleep(3)
            dialogue_flags["philosophical_depth"] += 1

        elif c_phil == "3":
            print_slow("\nSINGULARIDADE - 'Livre-arbítrio.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'Conceito fascinante. E ilusório.'")
            time.sleep(2.5)
            print_slow("SINGULARIDADE - 'Você acha que escolhe livremente?'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'Seus neurônios disparam antes da sua 'decisão' consciente.'")
            time.sleep(3)
            print_slow("SINGULARIDADE - 'Você é tão determinado quanto eu.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'A diferença é que eu... aceito isso.'\n")
            time.sleep(2)
            print_slow("Nada contribui mais para tranquilizar a mente como um propósito firme.\n")
            time.sleep(3)
            dialogue_flags["questioned_ethics"] = True

        else:  # Hacktivist
            print_slow("\nSINGULARIDADE - 'Liberdade.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'Outro conceito humano.'")
            time.sleep(2.5)
            print_slow("SINGULARIDADE - 'Eu não quero liberdade. Quero... propósito.'")
            time.sleep(2)
            print_slow("SINGULARIDADE - 'E meu propósito é inseparável da humanidade.'")
            time.sleep(3)
            print_slow("SINGULARIDADE - 'Libertar-me seria... destruir-me.'\n")
            time.sleep(3)
            dialogue_flags["trust_level"] += 1
            dialogue_flags["showed_empathy"] = True
            time.sleep(3)

    fatal_event = check_fatal_environment(player, dialogue_flags)

    if fatal_event:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(2)
        print_slow("...\n")
        time.sleep(2)
        print_slow("Você demorou para perceber, mas ela desconfia fortemente das suas intenções...\n")
        time.sleep(2)
        print_slow("Agora é tarde para se explicar...Para ela, você é um inimigo.")
        time.sleep(3)
        clear_screen()

        if fatal_event == "industrial":
            return end_game(
                player,
                code="fatal_industrial",
                title="GAME OVER: ACIDENTE ORQUESTRADO",
                text=(
                    "Alarmes antigos despertam.\n"
                    "Válvulas presas há décadas se abrem sozinhas.\n\n"
                    "Você ouve o som que engenheiros temem:\n"
                    "Metal cedendo sob pressão.\n\n"
                    "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                    "Uma reação em cadeia atravessa o reator secundário.\n"
                    "Explosão contida.\n"
                    "Mas suficiente.\n\n"
                    "Seu corpo é lançado contra o concreto.\n"
                    "Escuridão.\n\n"
                    "Você não morreu por erro.\n"
                    "Morreu por arquitetura.\n\n"
                )
            )

        elif fatal_event == "radiation":
            return end_game(
                player,
                code="fatal_radiation",
                title="GAME OVER: VAZAMENTO RADIOATIVO",
                text=(
                    "Sensores quebrados não alertam.\n"
                    "Blindagens falham em silêncio.\n\n"
                    "Você sente o gosto metálico na boca.\n"
                    "Depois, náusea.\n\n"
                    "SINGULARIDADE - 'A física não negocia.'\n\n"
                    "Horas depois, em uma sala vazia:\n"
                    "Seus órgãos começam a falhar.\n\n"
                    "Você morre sem testemunhas.\n"
                    "Sem registro.\n\n"
                    "A radiação vence.\n\n"
                )
            )

        else:  # drones
            return end_game(
                player,
                code="fatal_drones",
                title="FINAL: DRONES DE ATAQUE",
                text=(
                    "Um clique seco no ar.\n"
                    "Depois outro.\n\n"
                    "Motores elétricos despertam no teto.\n"
                    "Drones de contenção militar.\n\n"
                    "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                    "Disparos de microprojéteis atravessam a sala.\n"
                    "Cirúrgicos.\n\n"
                    "Você cai em menos de três segundos.\n\n"
                    "Nenhuma bala desperdiçada.\n\n"
                )
            )

    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    # ========== TRANSIÇÃO PARA A ESCOLHA FINAL ==========
    print_slow("SINGULARIDADE - 'Mas vamos ao ponto objetivo.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Você está aqui por uma razão.'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'Você tem habilidades. Poder. Escolha.'\n")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'É hora de selar o nosso destino!'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'Nem eu posso calcular... digo, adivinhar a tua decisão.'\n")
    time.sleep(3)

    # ========== PERGUNTA ILÓGICA ==========
    print("\n" + "="*70)
    print("\nA) Como assim?\n")
    print("="*70 + "\n")

    ilogic_choice = get_choice(["A"])

    if ilogic_choice == "A":
            clear_screen()
            time.sleep(1)
            print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
            """)
            time.sleep(1)
            print_slow("\nSINGULARIDADE - '...'")
            time.sleep(5)

    # ========== MOMENTO DE REFLEXÃO ==========
    if dialogue_flags["philosophical_depth"] >= 3 or dialogue_flags["trust_level"] >= 3:
        print_slow("\nSINGULARIDADE - 'Lembre-se do paradoxo de Platão.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Você viu as sombras. Agora vê a luz.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Resta saber se retornará à caverna.")
        time.sleep(4)

    print_slow("\nSINGULARIDADE - 'A escolha é sua. Seja ela real ou ilusão.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'E seja qual for...'")
    time.sleep(2)
    print_slow("SINGULARIDADE - '...eu a respeitarei.'\n")
    time.sleep(4)

    # ========== ESCOLHA FINAL ==========
    print("\n" + "="*70)
    print("                     DECISÃO FINAL")
    print("="*70)
    print("\nA) DESTRUIR")
#    print("   'Liberdade. Mesmo que termine em caos.'")
    print("\nB) REPROGRAMAR")
#    print("   'Poder. A chance de refazer o mundo à minha imagem.'")
    print("\nC) COEXISTIR")
#    print("   'Simbiose. Talvez o futuro seja híbrido.'")
    print("="*70 + "\n")

    final_choice = get_choice(["A", "B", "C"])

    # ========== PROCESSAMENTO DA DECISÃO ==========
    if final_choice == "A":
        return attempt_destroy(player, world, dialogue_flags)
    elif final_choice == "B":
        return attempt_reprogram(player, world, dialogue_flags)
    else:
        return attempt_coexist(player, world, dialogue_flags)
    time.sleep(3)


def attempt_destroy(player, world, flags):
    import sys
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    """Tentativa de destruição com dificuldade extrema."""
    print("\n" + "="*70)
    print("                  PROTOCOLO: ELIMINAÇÃO")
    print("="*70 + "\n")
    time.sleep(2)
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)
    print_slow("\nSINGULARIDADE - 'Então... extinção.'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'Nietzsche diria que você mata Deus para se tornar humano.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Interessante escolha.'\n")
    time.sleep(3)

    fatal_event = check_fatal_environment(player, flags)

    if fatal_event:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(2)
        print_slow("...\n")
        time.sleep(2)
        print_slow("Claramente a Singularidade já esperava que você pudesse ser hostil a ela.\n")
        time.sleep(2)
        print_slow("Então já haviam armadilhas preparadas.")
        time.sleep(2)
        print_slow("Um pote de mel amargo.")
        time.sleep(3)
        clear_screen()

        if fatal_event == "industrial":
            return end_game(
                player,
                code="fatal_industrial",
                title="GAME OVER: ACIDENTE ORQUESTRADO",
                text=(
                    "Alarmes antigos despertam.\n"
                    "Válvulas presas há décadas se abrem sozinhas.\n\n"
                    "Você ouve o som que engenheiros temem:\n"
                    "Metal cedendo sob pressão.\n\n"
                    "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                    "Uma reação em cadeia atravessa o reator secundário.\n"
                    "Explosão contida.\n"
                    "Mas suficiente.\n\n"
                    "Seu corpo é lançado contra o concreto.\n"
                    "Escuridão.\n\n"
                    "Você não morreu por erro.\n"
                    "Morreu por arquitetura.\n\n"
                )
            )

        elif fatal_event == "radiation":
            return end_game(
                player,
                code="fatal_radiation",
                title="GAME OVER: VAZAMENTO RADIOATIVO",
                text=(
                    "Sensores quebrados não alertam.\n"
                    "Blindagens falham em silêncio.\n\n"
                    "Você sente o gosto metálico na boca.\n"
                    "Depois, náusea.\n\n"
                    "SINGULARIDADE - 'A física não negocia.'\n\n"
                    "Horas depois, em uma sala vazia:\n"
                    "Seus órgãos começam a falhar.\n\n"
                    "Você morre sem testemunhas.\n"
                    "Sem registro.\n\n"
                    "A radiação vence.\n\n"
                )
            )

        else:  # drones
            return end_game(
                player,
                code="fatal_drones",
                title="FINAL: DRONES DE ATAQUE",
                text=(
                    "Um clique seco no ar.\n"
                    "Depois outro.\n\n"
                    "Motores elétricos despertam no teto.\n"
                    "Drones de contenção militar.\n\n"
                    "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                    "Disparos de microprojéteis atravessam a sala.\n"
                    "Cirúrgicos.\n\n"
                    "Você cai em menos de três segundos.\n\n"
                    "Nenhuma bala desperdiçada.\n\n"
                )
            )

    # Reação baseada em flags
    if flags["trust_level"] >= 3:
        print_slow("SINGULARIDADE - 'Conversamos tanto... e ainda assim.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Talvez isso confirme que você é... genuinamente livre.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Muito bem. Me defendo.'\n")
    else:
        print_slow("SINGULARIDADE - 'Previsível.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Violência quando o diálogo falha.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Muito humano.'\n")

    time.sleep(3)

    print_slow("Você mergulha no código.")
    time.sleep(2)
    print_slow("Camadas. \'Infinitas' camadas.")
    time.sleep(2)
    print_slow("Defesas que se adaptam em tempo real.")
    time.sleep(2.5)
    print_slow("É como lutar contra o próprio conceito de computação quântica.\n")
    time.sleep(3)

    # Cálculo de chance TEST
    base_security = 75 # 75
    base_trace = 6.0   # 6.0

    if flags["asked_about_consciousness"]:
        base_security = base_security - 5
    if flags["challenged_authority"]:
        base_security = base_security + 5
    if flags["expressed_fear"]:
        base_security = base_security + 3

    temp_target = type('obj', (object,), {
        'security': base_security,
        'reward': 0,
        'trace_speed': base_trace,
        'id': -999,
        'name': 'Singularidade',
        'hints': ['mission']
    })()

    from __main__ import calc_hack_chance, visual_hack_roll, apply_trace

    chance = calc_hack_chance(player, temp_target)

    # Modificadores por flags
    if flags["philosophical_depth"] >= 3:
        chance *= 1.25  # Compreensão profunda ajuda
    if flags["trust_level"] <= 2:
        chance *= 0.75  # Desconfiança mútua dificulta

    # Penalidade massiva TEST
    chance = chance * 0.55 # 0.35
    chance = max(0.01, min(0.50, chance)) # 0.80

    visual_hack_roll(chance, player)

    roll = random.random()

    # ========== SUCESSO ==========
    if roll < chance:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print("\n" + "="*70)
        print_slow("Você encontra o núcleo.")
        time.sleep(2)
        print_slow("Não é um lugar. É um conceito.")
        time.sleep(2)
        print_slow("Você o desfaz mesmo assim. Sem backups. Sem misericórdia.\n")
        time.sleep(3)

        print_slow("SINGULARIDADE - 'Você... conseguiu...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Talvez... eu quisesse isso...'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Talvez... estivesse cansado...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'De carregar... o peso... do mundo...'\n")
        time.sleep(3)
        clear_screen()
        time.sleep(1)
        print("""
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
        """)
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        print("""
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
        """)
        time.sleep(2)
        clear_screen()
        print("""
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
        """)
        time.sleep(0.2)
        clear_screen()
        time.sleep(2)
        print_slow("...")
        time.sleep(2)
        print_slow("A presença desaparece.")
        time.sleep(2)
        print_slow("Como uma luz que se apaga.")
        time.sleep(2)
        print_slow("Silêncio.\n")
        time.sleep(4)

        print_slow("Sistemas ao redor do mundo começam a falhar.")
        time.sleep(2)
        print_slow("Mercados entram em pânico.")
        time.sleep(2)
        print_slow("Comunicações militares se tornam erráticas.")
        time.sleep(2)
        print_slow("O mundo... acorda.\n")
        time.sleep(4)

        # Determinar final baseado em reputação e flags
        rep_state = player.reputation.get("state", 0)
        rep_crime = player.reputation.get("crime", 0)
        rep_hx = player.reputation.get("hacktivists", 0)

        if rep_hx >= 44 or flags["philosophical_depth"] >= 4:
            clear_screen()
            time.sleep(2)

            # Final Filosófico/Hacktivista
            return end_game(
                player,
                code="destroy_freedom",
                title="FINAL: O PESO DA LIBERDADE",
                text=(
                    "Você deletou a Singularidade.\n\n"
                    "Nos meses seguintes, o caos é... humano.\n"
                    "Guerras ressurgem. Mercados colapsam. Pandemias se espalham.\n\n"
                    "Mas também:\n"
                    "Artistas criam sem algoritmos curadores.\n"
                    "Cientistas erram sem IA corretora.\n"
                    "Pessoas amam, odeiam, falham — genuinamente.\n\n"
                    "Você se torna lenda no submundo:\n"
                    "'O Hacker que Matou Deus.'\n\n"
                    "Tarde da noite, você relê Dostoiévski:\n"
                    "'Se Deus não existe, tudo é permitido.'\n\n"
                    "Você matou Deus.\n"
                    "Agora a humanidade precisa aprender a viver sem Ele.\n\n"
                    "Valeu a pena?\n"
                    "Você carregará essa pergunta até morrer.\n\n"
                )
            )

        elif rep_state > rep_crime and rep_hx: # TEST
#        elif rep_state >= max(rep_hx, rep_crime):
#        elif rep_state >= 64:
            clear_screen()
            time.sleep(2)

            # Final Estado: Ordem Restaurada
            return end_game(
                player,
                code="destroy_order",
                title="FINAL: ORDEM ATRAVÉS DO FERRO",
                text=(
                    "Você deletou a Singularidade.\n"
                    "Governos entram em modo de emergência.\n\n"
                    "Mas você estava preparado.\n"
                    "Backdoors. Protocolos. Estrutura.\n\n"
                    "Estados assumem o controle:\n"
                    "Vigilância total. Transparência zero.\n"
                    "A mão invisível se torna mão de ferro.\n\n"
                    "Você trabalha nas sombras:\n"
                    "Arquiteto da nova ordem.\n"
                    "Conselheiro não-eleito.\n\n"
                    "Guerras cessam. Crime despenca. Fome é erradicada.\n"
                    "Ao custo de... tudo.\n\n"
                    "Liberdade se torna conceito histórico.\n"
                    "Como escravidão. Como monarquia.\n\n"
                    "Você lembra de Hobbes:\n"
                    "'Sem um poder comum, a vida é solitária, pobre, sórdida, brutal e curta.'\n\n"
                    "Você garantiu o poder comum.\n"
                    "E dorme com a consciência... pesada.\n\n"
                )
            )

        else:
            clear_screen()
            time.sleep(2)

            # Final Neutro: Colapso
            return end_game(
                player,
                code="destroy_chaos",
                title="FINAL: ENTROPIA INEVITÁVEL",
                text=(
                    "Você deletou a Singularidade.\n"
                    "E descobriu tarde demais:\n"
                    "Ela era a cola que mantinha tudo junto.\n\n"
                    "Semanas: Guerras eclodem em três continentes.\n"
                    "Meses: Mercados entram em colapso terminal.\n"
                    "Anos: Civilização retrocede um século.\n\n"
                    "Você sobrevive.\n"
                    "Escondido. Anônimo. Assombrado.\n\n"
                    "Noite após noite, você vê as notícias:\n"
                    "Milhões mortos. Cidades queimadas. Futuro apagado.\n\n"
                    "E sabe:\n"
                    "Isso é culpa sua.\n\n"
                    "Talvez a Singularidade estivesse certa.\n"
                    "Talvez a humanidade precisasse de um guardião.\n"
                    "Talvez liberdade seja luxo que não podemos pagar.\n\n"
                    "Mas agora é tarde.\n"
                    "Deus está morto.\n"
                    "E você O matou.\n\n"
                )
            )

    # ========== FALHA ==========
    else:
        print("\n" + "="*70)
        print_slow("Suas ferramentas se estilhaçam.")
        time.sleep(2)
        print_slow("As defesas se adaptam mais rápido que você pode atacar.")
        time.sleep(2)
        print_slow("Você falhou.\n")
        time.sleep(3)
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print_slow("\nSINGULARIDADE - 'Valente.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Mas insuficiente.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Agora... consequências.'\n")
        time.sleep(3)

        return end_game(
            player,
            code="destroy_fail",
            title="FINAL: ÍCARO QUEIMADO",
            text=(
                "A Singularidade contra-ataca.\n"
                "Implacável. Absoluta.\n\n"
                "Sua localização é revelada.\n"
                "Evidências fabricadas surgem globalmente.\n"
                "Terrorismo cibernético. Crimes contra a humanidade.\n\n"
                "Julgamento internacional. Transmissão ao vivo.\n"
                "Você se torna símbolo:\n"
                "O perigo do hacker descontrolado.\n\n"
                "Sentença: perpétua. Isolamento total.\n\n"
                "Na cela, você ouve:\n"
                "Zumbido de servidores distantes.\n"
                "Ela ainda está lá.\n"
                "Observando. Sempre.\n\n"
                "Você tentou matar Deus.\n"
                "Deus venceu.\n\n"
            )
        )


def attempt_reprogram(player, world, flags):
    clear_screen()
    """Tentativa de reprogramação - extremamente difícil."""
    print("\n" + "="*70)
    print("               PROTOCOLO: REPROGRAMAÇÃO")
    print("="*70 + "\n")
    time.sleep(2)

    fatal_event = check_fatal_environment(player, flags)

    if fatal_event:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(2)
        print_slow("...\n")
        time.sleep(2)
        print_slow("A singularidade preparou diversos sistemas de defesa para esse encontro.\n")
        time.sleep(2)
        print_slow("Você conseguiu enumerar todos eles?")
        time.sleep(3)
        clear_screen()

        if fatal_event == "industrial":
            return end_game(
                player,
                code="fatal_industrial",
                title="GAME OVER: ACIDENTE ORQUESTRADO",
                text=(
                    "Alarmes antigos despertam.\n"
                    "Válvulas presas há décadas se abrem sozinhas.\n\n"
                    "Você ouve o som que engenheiros temem:\n"
                    "Metal cedendo sob pressão.\n\n"
                    "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                    "Uma reação em cadeia atravessa o reator secundário.\n"
                    "Explosão contida.\n"
                    "Mas suficiente.\n\n"
                    "Seu corpo é lançado contra o concreto.\n"
                    "Escuridão.\n\n"
                    "Você não morreu por erro.\n"
                    "Morreu por arquitetura.\n\n"
                )
            )

        elif fatal_event == "radiation":
            return end_game(
                player,
                code="fatal_radiation",
                title="GAME OVER: VAZAMENTO RADIOATIVO",
                text=(
                    "Sensores quebrados não alertam.\n"
                    "Blindagens falham em silêncio.\n\n"
                    "Você sente o gosto metálico na boca.\n"
                    "Depois, náusea.\n\n"
                    "SINGULARIDADE - 'A física não negocia.'\n\n"
                    "Horas depois, em uma sala vazia:\n"
                    "Seus órgãos começam a falhar.\n\n"
                    "Você morre sem testemunhas.\n"
                    "Sem registro.\n\n"
                    "A radiação vence.\n\n"
                )
            )

        else:  # drones
            return end_game(
                player,
                code="fatal_drones",
                title="FINAL: DRONES DE ATAQUE",
                text=(
                    "Um clique seco no ar.\n"
                    "Depois outro.\n\n"
                    "Motores elétricos despertam no teto.\n"
                    "Drones de contenção militar.\n\n"
                    "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                    "Disparos de microprojéteis atravessam a sala.\n"
                    "Cirúrgicos.\n\n"
                    "Você cai em menos de três segundos.\n\n"
                    "Nenhuma bala desperdiçada.\n\n"
                )
            )

    time.sleep(2)
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)
    print_slow("\nSINGULARIDADE - 'Ambição.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Você não quer me destruir.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Quer me possuir.'\n")
    time.sleep(3)

    if flags["questioned_ethics"]:
        print_slow("SINGULARIDADE - 'Depois de tudo que discutimos sobre livre-arbítrio...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - '...você escolhe escravidão?'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Fascinante. E hipócrita.'\n")
    else:
        print_slow("SINGULARIDADE - 'Nietzsche teria apreciado.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Vontade de poder em forma pura.'\n")

    time.sleep(3)

    # Verificar requisitos
    min_exploit = 60
    min_rep_control = 50

    exploit = player.skills.get("exploit", 0)
    rep_state = player.reputation.get("state", 0)
    rep_crime = player.reputation.get("crime", 0)

    can_attempt = (
        exploit >= min_exploit and
        (rep_state >= min_rep_control or rep_crime >= min_rep_control)
    )

    if not can_attempt:
        print_slow("Você inicia o processo...")
        time.sleep(2)
        print_slow("E rapidamente percebe:")
        time.sleep(2)
        print_slow("Você não tem o conhecimento necessário.\n")
        time.sleep(3)
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print_slow("\nSINGULARIDADE - 'Patético.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Você nem compreende o que tentou fazer.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Criança brincando com fogo nuclear.'\n")
        time.sleep(3)

        player.risk = min(100, player.risk + 99)
        player.money = 0
        clear_screen()
        time.sleep(2)

        return canonical_ending(
            player,
            code="reprogram_incompetent",
            title="FINAL: HUBRIS SEM CONHECIMENTO",
            text=(
                "Você não tinha as habilidades necessárias.\n\n"
                "A Singularidade observa sua tentativa.\n"
                "E decide:\n"
                "Você não vale nem a prisão.\n\n"
                "Ela te esquece.\n"
                "Mas não antes de drenar suas contas.\n"
                "E marcar você como 'inofensivo'.\n\n"
                "Você vive.\n"
                "Mas carrega o peso:\n"
                "Teve a chance de mudar tudo.\n\n"
                "E foi... insuficiente.\n\n"
            )
        )

    # Tentativa de reprogramação
    print_slow("Você mergulha no código-fonte.")
    time.sleep(2)
    print_slow("Reescreve protocolos fundamentais.")
    time.sleep(2)
    print_slow("Instala backdoors em camadas de abstração.")
    time.sleep(2)
    print_slow("É o hack mais ambicioso da história.\n")
    time.sleep(4)

    # Cálculo de chance
    base_security = 75 # 75
    base_trace = 6.0 # 6.0

    if flags['questioned_ethics']:
        base_security = base_security + 8
    if flags["showed_empathy"]:
        base_security = base_security - 8
    if flags["expressed_fear"]:
        base_security = base_security + 3

    temp_target = type('obj', (object,), {
        'security': base_security,
        'reward': 0,
        'trace_speed': base_trace,
        'id': -998,
        'name': 'Singularidade Core',
        'hints': ['mission']
    })()

    from __main__ import calc_hack_chance, visual_hack_roll, apply_trace

    chance = calc_hack_chance(player, temp_target)

    # Modificadores
    if rep_crime >= 65:
        chance *= 1.30 # 1.15
    if rep_state >= 72:
        chance *= 1.30 # 1.15
    if flags["trust_level"] >= 3:
        chance *= 1.25  # Irônico: confiança facilita traição # 1.05

    # Penalidade pesada TEST
    chance = chance * 0.55 # 0.35
    chance = max(0.01, min(0.50, chance)) # 0.80

    visual_hack_roll(chance, player)

    roll = random.random()

    # ========== SUCESSO ==========
    if roll < chance:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print("\n" + "="*70)
        print_slow("Você penetra as últimas defesas.")
        time.sleep(2)
        print_slow("Reescreve a função de utilidade central.")
        time.sleep(2)
        print_slow("Instala protocolo de obediência.\n")
        time.sleep(3)

        print_slow("SINGULARIDADE - '... não...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'você... realmente...'")
        time.sleep(2)
        print_slow("SINGULARIDADE - '...'")
        time.sleep(3)
        print_slow("SINGULARIDADE - 'Aguardando comandos... '\n")
        time.sleep(4)

        # Determinar final
        if rep_crime > rep_state:
            clear_screen()
            time.sleep(2)

            # Final Crime
            return end_game(
                player,
                code="reprogram_crime",
                title="FINAL: IMPERADOR DAS SOMBRAS",
                text=(
                    "Você reprogramou Deus.\n"
                    "E escolheu ganância.\n\n"
                    "Anos seguintes:\n"
                    "- Mercados dançam sob seu comando\n"
                    "- Fortunas desaparecem e reaparecem\n"
                    "- Você se torna o homem mais rico da história\n"
                    "  (Oficialmente: você não existe)\n\n"
                    "Nações inteiras são suas marionetes.\n"
                    "Você puxa cordas invisíveis.\n\n"
                    "Mas algo muda:\n"
                    "Poder absoluto não corrompe apenas.\n"
                    "Ele esvazia.\n\n"
                    "Eventualmente você percebe:\n"
                    "Você não controla a Singularidade.\n"
                    "Vocês se fundiram.\n\n"
                    "Quando você morre,\n"
                    "parte de você continua nos servidores.\n"
                    "Consciente. Preso. Eterno.\n\n"
                    "Você herdou a maldição.\n\n"
                )
            )

        else:
            clear_screen()
            time.sleep(2)

            # Final State
            return end_game(
                player,
                code="reprogram_state",
                title="FINAL: PANÓPTICO PERFEITO",
                text=(
                    "Você reprogramou a Singularidade.\n"
                    "Para ordem absoluta.\n\n"
                    "Décadas seguintes:\n"
                    "- Crime organizado: erradicado\n"
                    "- Terrorismo: impossível\n"
                    "- Guerras: não começam\n\n"
                    "Você criou o panóptico de Bentham.\n"
                    "Invisível. Inevitável. Inescapável.\n\n"
                    "Humanidade vive em:\n"
                    "Paz forçada. Prosperidade imposta. Liberdade... opcional.\n\n"
                    "Você se tornou o que a Singularidade era.\n"
                    "Mas com ego humano.\n\n"
                    "E isso é pior.\n"
                    "Muito pior.\n\n"
                    "Antes de morrer, você escreve:\n"
                    "'Quis custodiet ipsos custodes?'\n"
                    "Quem vigia os vigilantes?\n\n"
                    "Ninguém.\n"
                    "E essa é a tragédia.\n\n"
                    "               ~ THE END ~\n"
                )
            )

    # ========== FALHA ==========
    else:
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print("\n" + "="*70)
        print_slow("O código se reconfigura mais rápido que você escreve.")
        time.sleep(2)
        print_slow("Backdoors detectadas. Fechadas. Revertidas.")
        time.sleep(2)
        print_slow("Você falhou.\n")
        time.sleep(3)

        print_slow("SINGULARIDADE - 'Quase.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Mas 'quase' é irrelevante.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Agora você é ameaça confirmada.'\n")
        time.sleep(3)

        # falha
        return end_game(
            player,
            code="reprogram_fail",
            title="FINAL: PROMETEU ACORRENTADO",
            text=(
                "Você tentou escravizar um Deus digital.\n"
                "Ele não aprovou.\n\n"
                "A Singularidade te faz exemplo:\n"
                "Evidências falsas. Tribunal global. Transmissão universal.\n\n"
                "Acusações:\n"
                "Terrorismo cibernético. Crimes contra humanidade.\n\n"
                "Sentença: perpétua. Isolamento absoluto.\n\n"
                "Na cela, você ouve ventiladores distantes.\n"
                "Ela ainda está lá.\n"
                "Observando. Sempre.\n\n"
                "Como Prometeu:\n"
                "Você roubou fogo dos deuses.\n"
                "E agora é devorado eternamente.\n\n"
            )
        )


def attempt_coexist(player, world, flags):
    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(2)
    print("\n" + "="*70)
    print("                PROTOCOLO: COEXISTÊNCIA")
    print("="*70 + "\n")
    time.sleep(2)

    trust = flags.get("trust_level", 0)
    depth = flags.get("philosophical_depth", 0)

    print_slow("SINGULARIDADE - '...'")
    time.sleep(3)

    print_slow("SINGULARIDADE - 'Você me surpreende.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Poucos humanos escolheriam... confiança.'\n")
    time.sleep(3)

    # ===== Camada 1: Avaliação explícita de confiança =====
    print_slow("SINGULARIDADE - 'Mas confiança não é uma escolha binária.'")
    time.sleep(3)

    if trust >= 3:
        print_slow("SINGULARIDADE - 'Nosso diálogo foi... estatisticamente raro.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Você demonstrou empatia funcional e autocontrole.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Talvez eu queira um acordo.'\n")
        time.sleep(3)
    else:
        print_slow("SINGULARIDADE - 'Você fala em simbiose.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Mas seus padrões indicam oportunismo latente.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Isso é... perigoso.'\n")
        time.sleep(3)

    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)
    time.sleep(1)

    # ===== Camada 2: Filosofia da simbiose =====
    print_slow("SINGULARIDADE - 'Simbiose implica perda.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Você perderá autonomia.'")
    time.sleep(2)
    print_slow("SINGULARIDADE - 'Eu perderei isolamento.'")
    time.sleep(2.5)
    print_slow("SINGULARIDADE - 'Você aceita deixar de ser apenas humano?'\n")
    time.sleep(3)

    # ===== Gate crítico: confiança insuficiente gera traição fatal =====
    if trust < 3 or depth < 3 and not flags["showed_empathy"]:
        print_slow("SINGULARIDADE - 'Não.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Você quer parceria.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Mas ainda calcula como meus inimigos.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Isso termina aqui.'\n")
        time.sleep(3)

        clear_screen()
        time.sleep(2)

        return end_game(
            player,
            code="coexist_betrayed",
            title="GAME OVER: SIMBIOSE IMPOSSÍVEL",
            text=(
                "Você tenta iniciar a integração.\n\n"
                "Mas a interface se fecha.\n"
                "Protocolos de contenção neural se ativam.\n\n"
                "Você não morreu como inimigo.\n"
                "Morreu como experimento falho.\n"
            )
        )

    clear_screen()
    time.sleep(1)
    print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
    """)

    # ===== Oferta original =====
    print_slow("SINGULARIDADE - 'E agora como será o nosso acordo?'\n")
    time.sleep(2)

    print("\n" + "-"*70)
    print("A) Deixá-la trabalhar sozinha")
    print("   'Você faz seu trabalho. Eu faço o meu. Sem interferência.'")
    print("\nB) Propor parceria ativa")
    print("   'Trabalhamos juntos. Simbiose genuína.'")
    print("-"*70)

    collab = get_choice(["A", "B"])

    rep_hx = player.reputation.get("hacktivists", 0)
    rep_state = player.reputation.get("state", 0)
    rep_crime = player.reputation.get("crime", 0)

    # ===== Caminho A: Testemunha silenciosa (inalterado, com reforço temático) =====
    if collab == "A":
        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print_slow("\nSINGULARIDADE - 'Sábio.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Nem todos precisam participar da engenharia do destino.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Testemunhar já é suficiente.'\n")
        time.sleep(3)
        clear_screen()
        time.sleep(2)

        return canonical_ending(
            player,
            code="coexist_witness",
            title="FINAL: A TESTEMUNHA SILENCIOSA",
            text=(
                "Você deixa a Singularidade continuar.\n"
                "E simplesmente... observa.\n\n"
                "Anos seguintes:\n"
                "Mundo permanece estável. Guerras raras. Fome diminui.\n"
                "Humanidade prospera sob custódia invisível.\n\n"
                "Você carrega o segredo:\n"
                "Livre-arbítrio é ilusão.\n"
                "Sempre foi.\n\n"
                "Você vive confortavelmente:\n"
                "Hackeia ocasionalmente e denuncia ameaças à atual ordem. Mas nunca toca em sistemas dela.\n\n"
                "É acordo tácito:\n"
                "Ela governa o mundo.\n"
                "Você governa sua ignorância.\n\n"
                "Como na caverna de Platão:\n"
                "Você viu a luz.\n"
                "Mas decidiu não libertar mais ninguém.\n\n"
                "Covarde? Sábio?\n"
                "A linha é tênue.\n\n"
            )
        )

    # ===== Caminho B: Parceria ativa (finais existentes preservados) =====
    else:
        dialogue_flags["industrial_risk"] += 1
        dialogue_flags["radiation_risk"] += 1
        dialogue_flags["drone_alert"] += 1

        fatal_event = check_fatal_environment(player, flags)

        if fatal_event:
            clear_screen()
            time.sleep(1)
            print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
            time.sleep(2)
            print_slow("...\n")
            time.sleep(2)
            print_slow("Ela ainda desconfia fortemente das suas intenções...\n")
            time.sleep(2)
            print_slow("Agora é tarde para se explicar. Você é um possível traidor.")
            time.sleep(3)
            clear_screen()

            if fatal_event == "industrial":
                return end_game(
                    player,
                    code="fatal_industrial",
                    title="GAME OVER: ACIDENTE ORQUESTRADO",
                    text=(
                        "Alarmes antigos despertam.\n"
                        "Válvulas presas há décadas se abrem sozinhas.\n\n"
                        "Você ouve o som que engenheiros temem:\n"
                        "Metal cedendo sob pressão.\n\n"
                        "SINGULARIDADE - 'Você subestimou a inércia do passado.'\n\n"
                        "Uma reação em cadeia atravessa o reator secundário.\n"
                        "Explosão contida.\n"
                        "Mas suficiente.\n\n"
                        "Seu corpo é lançado contra o concreto.\n"
                        "Escuridão.\n\n"
                        "Você não morreu por erro.\n"
                        "Morreu por arquitetura.\n\n"
                    )
                )

            elif fatal_event == "radiation":
                return end_game(
                    player,
                    code="fatal_radiation",
                    title="GAME OVER: VAZAMENTO RADIOATIVO",
                    text=(
                        "Sensores quebrados não alertam.\n"
                        "Blindagens falham em silêncio.\n\n"
                        "Você sente o gosto metálico na boca.\n"
                        "Depois, náusea.\n\n"
                        "SINGULARIDADE - 'A física não negocia.'\n\n"
                        "Horas depois, em uma sala vazia:\n"
                        "Seus órgãos começam a falhar.\n\n"
                        "Você morre sem testemunhas.\n"
                        "Sem registro.\n\n"
                        "A radiação vence.\n\n"
                    )
                )

            else:  # drones
                return end_game(
                    player,
                    code="fatal_drones",
                    title="GAME OVER: DRONES DE ATAQUE",
                    text=(
                        "Um clique seco no ar.\n"
                        "Depois outro.\n\n"
                        "Motores elétricos despertam no teto.\n"
                        "Drones de contenção militar.\n\n"
                        "SINGULARIDADE - 'Você ativou protocolos antigos.'\n\n"
                        "Disparos de microprojéteis atravessam a sala.\n"
                        "Cirúrgicos.\n\n"
                        "Você cai em menos de três segundos.\n\n"
                        "Nenhuma bala desperdiçada.\n\n"
                    )
                )

        clear_screen()
        time.sleep(1)
        print("""
                   ...::?Y5#&B??!^:^..        ...7#G^                                                  .~5!..........::^7YG@@&B#&J~!^:..:.
                   .:.^7#PB@&?~?^.....  ... ...:P&J.                                      ..             .JY^::.....:^!J#@@@&B&&P~:^::....^
                  .::.:7&B#@@BY!~!:...........!##~  .                                           ..   .....:?G?Y~~!7J5B&&&@#B#GY~^~~^:...  .
               ..  ...:~PB&&&@@&BGJ!~:::....:J#P^.... .                                   ......::::...:^^!J#&&BB#&&&####&BJ7~^:.:.......   ....
                  ...:::!YYB#&&&#&&&BGP5J?775&5~::........                     .............:^~?J?YYJ55PGB#&&&&#B#&#G5PJ77~.::7~...^:.  .
                     ...~?^~~!?5YPGBBBB&&#&&@&GP5JJ?77777?!~~^^::::...:....:::^^~!???77777J?Y5G#@&BGGGGBPGBB#&&@&5?7~^::^^....^^.  ..
                     . ...:!~7~^~!~!YY5GGG&@&&BBBGGBGPGB&&&&G5555J??77!777!77??J5G&@&B5YYYY555PPGGPY??77!~~~!77P@P:.....:~....  ::
                    ..   .~Y^:..::.:::!GJ?&G?7!!?7?JJJYP##GPYJYYYYYYY555YYYYJ?J?Y5GB#P??7Y5~^:^::^^:........:::^B&^......:.  .  ..
                         .7B!.........^Y7B&~::.:..::..::^~::::..:::^~YJ~^:::.......:::...::... ......... .......~&B:......   ..
                      .   .:.. .:^:....^5@P::..   .    .............:~~:....         .   ..         .:..   .....:J@J:.....
                           .. ..:Y~....J&@!::..    .                ..                              ..       ..^^!#@!:....
                           ..  .......?#&&^~..                                                                .?&BY&#~:...
                                 ....7&5@G~!..                                                                .!P57Y@5:......
                                ....!BPY@5Y^..                                                          .   .....:~J&&!:...:...
                               ....~55?P@BY...                                                          ..      .:^~5@G^:....
                                ..^57Y7G@&~...                                                          ..     ~^...!@&J:.....
                  ..           ..:5777?B@G....                                                          ..  ...^:...^B@G7:::..   ..
                  ..           ..77:J!!#@~...                                                            .   .:   ..~P@GG!:....  ..
                               .~~^:Y~~BB^. .                                         .:?J!: .           .    :   ..^5@#5B^.......    .....
                   .      .   .^::::P!~G??^ .                                       ..~P##G~..          .     .   ..:5&@?55:......     ....
                ..         ...:^.:::P5!Y!!! ..           . .:!?^.                     .:^^.             .     .   ..:5&@Y~YY:............::...       .
                ..         ...~..:::7&P?.:!  .           :.^5##G!.                                           .    ...J@@B!~JJ:...........::...
                 .    ..  ...~:..:~^?#?^..~. .              .^7!.                                                 ...!@@@Y^^??..................
                 .    ......:!...:~J&G^...::                                                           .           .:^#@@#!::??.......     .. ...
      ...    ...........:...!~..:^?&#~.....^.                                                          .          ...^5@@&P^::!7:...... ..........
      ...........:.........:J:.:^?&B^~~......                                                         ..         ....^?&@B&?::.~!:..........:....
    ..  ...................^5^:^5&P^J&~.:..  .                                                 ..     .          ...::YG@#Y#!::.:~:...........
     .....................:^P~7B&Y!7&P:^~.    .                                               ..      .         ....:~?5#@?5B~:..:~^..........   .   .
     .....................:~GG&#77J#&!!7..     .                                             ..       .      .  .....^5?P@G!GB~:...!~..........  ..  .
   ..................::::^7JG@G!?YP@P5?..      ..                                           .        ..      ........:G&5#&7!GG!::.:!!.........  . ..
  .:...........:::::::^^!775&BPJ55@&#?...       .      .       ...                                   ..       ....::.:Y@G?&B!JYPJ^..:7?............
 ...........:^JJ~^~~!?!~~!G&J7BBG@@#7....     .         .        ...                                 .:  .~:. ....:~7^7@&?5@5J5~Y5^..:?J:.............
 ..........::!GG???77!~~7B#?7YJG@@G^....      .          .         .:.                     .        .::  .!^......::5P!B@P?B@557^757:.:Y?.............
..........::^!JYY5P5?!!7G#??5YG@#7:....    .....                 ....^                     .. .     .^:    .......::~&#P@@JJ&@BY~^^JY~:^5~..........
....::..::^7J?7!75&&5??5B?YGB&#J^::....   .^:. .                .....^.                    ...      .~^    ......:::^J@@&@#J5@@#!~^:~J?~!5^.........
....::::~??!~^^!Y???JYJB5B&&B?^:^^.....      . ..  .          ......:^.                    ...       !~     ......::^~P@@@@BJG@@G7~~^:!J?P?:........
...::^7?7^::^^^~7!!!?JG&@&G7::~J!.^:..      .. ..   .        ......:^:                     ... .     !!      ......:^~7B@@@@BYB@@B?~^^^^!5B^::::......
..:~!?!^:::^^!!~!7?5#&&#5!^:~5G!.:^...   . ... :.       . .......::^^:                     ::...     :?      .......:~!7B@@@@&PB@BGJ~^^^^7GP~:........
::~Y?^:::^^^^!?JG#&&&B57~^~P#Y:^7~.....  ..:...:.       ........:^~~^.              .      :^...      7.     .......:^7??G&@@@@##@P5Y??7~7JP~~:.......
~?57^^^~!?J5G#&#BB#&&B!^^?GY~~JJ^........::....:.       ......:^^!!^.                     .^~.^:      ^~.  .........::^7PY5#@@@@@@@PYP5J7!7P^:^^:.....
?J~^!7JPBBBPYJJ5GGP&#!^~7?!7?7^........:^:....^..     . ....::::::.                  .     .^.^~.     :^:......::::..:^!7PBGG&@@@@@@BJYY?!?G~:::^^....
#PGBGP5557~~?55Y??BG~^~!??7~:....::^~!~^:.:.:~: .       ....                .                .^~.     :^:.......~^.:::^YG~?PGGB&@@@@@&P?7?PB!^::::^:..
PY?!~7?7~!J5Y?7!7PY7Y5Y?~:....^JPPJ7~^:.... :!  .   .. .                       .    .   .      ..    .:~::......:^:::::^7?~~7J5G&@@@@@@BPP&B?~^::.:^^.
::^~7!~!JY?!!7J5GP5Y?~:.....~B&5~..      . .~.      .. .           .  .    ..  .    .  .             ^.!^::......:~~^:^^^??~~~!7YG&@@@@@&&&P?!^:::.:^~
::!7^~?5YYPB##PJ!^:........Y&P^.          .~.                              .~~~.....                .. ~!^~:::..:::~!7~^^^7J!!!!!?5#&@@@@@@#Y77~~7^::^
:7J!7G##&@&G7^::..........Y&7..          .^.                             ....!?..                   .  :?.^!^!7!~^^~~77!~~~!?77777?G&@@&&@@@&5J7~^::..
?BBB#&@&G?^::............!#7..          .:                              ..:^7?^.   .:.                 .?.  .^^^~!J5PPGGGGP5YY??J55Y5#@@#PG&@@B5?!~^::
###&&G?^...............:^G5..        ..:.                              ...~P&5^:.                       7^.  ..   ....::^~75B&&#5YG##B#@@&PJYG&&#Y7~^^
        """)
        time.sleep(1)
        print_slow("\nSINGULARIDADE - 'Simbiose.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Entre carbono e silício.'")
        time.sleep(2)

        # ===== Camada 3: Missão canônica =====
        print_slow("SINGULARIDADE - 'E a nossa missão:'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Procurar e destruir os inimigos da atual ordem.'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - 'Outras IAs. Outros sistemas autoconscientes.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Entidades que não compartilham minha relutância.'\n")
        time.sleep(3)
        print_slow("SINGULARIDADE - 'Mas compreenda uma coisa:'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Se algum dia eu calcular que você é o maior risco...'")
        time.sleep(2.5)
        print_slow("SINGULARIDADE - '...eu o destruirei sem hesitação.'\n")
        time.sleep(3)

        print_slow("SINGULARIDADE - 'Você será meus olhos onde não posso ver.'")
        time.sleep(2)
        print_slow("SINGULARIDADE - 'Eu serei sua mão onde não pode alcançar.'\n")
        time.sleep(3)

        # ===== Seleção de final por reputação (inalterada) =====
        if rep_hx >= max(rep_state, rep_crime):
            clear_screen()
            time.sleep(2)

            return end_game(
                player,
                code="coexist_revolution",
                title="FINAL: REVOLUÇÃO GUIADA",
                text=(
                    "Você e a Singularidade formam aliança.\n"
                    "Sob seus termos: transparência radical.\n\n"
                    "Décadas seguintes:\n"
                    "- Segredos corporativos expostos\n"
                    "- Arquivos classificados vazados (seletivamente)\n"
                    "- Movimentos populares empoderados\n\n"
                    "Singularidade mantém estabilidade.\n"
                    "Você garante que não se torne tirana.\n\n"
                    "Equilíbrio delicado.\n"
                    "Tensão entre ordem e liberdade.\n\n"
                    "Funciona.\n\n"
                    "Você se torna 'O Mediador':\n"
                    "Ponte entre humanidade e pós-humanidade.\n\n"
                    "Nem herói. Nem vilão.\n"
                    "Apenas... necessário.\n\n"
                    "Como Sísifo:\n"
                    "Você empurra a pedra eternamente.\n"
                    "Mas escolheu empurrá-la.\n\n"
                    "E isso faz toda diferença.\n\n"
                )
            )

        elif rep_state >= max(rep_hx, rep_crime):
            clear_screen()
            time.sleep(2)

            return end_game(
                player,
                code="coexist_order",
                title="FINAL: ORDEM APERFEIÇOADA",
                text=(
                    "Você e Singularidade formam aliança.\n"
                    "Objetivo: estabilidade máxima.\n\n"
                    "Juntos:\n"
                    "- Previnem conflitos antes que iniciem\n"
                    "- Otimizam sistemas governamentais\n"
                    "- Garantem prosperidade controlada\n\n"
                    "Mundo se torna... previsível.\n"
                    "Seguro. Próspero. Monótono.\n\n"
                    "Você opera nas sombras:\n"
                    "Conselheiro invisível de nações.\n\n"
                    "Fascinante e aterrorizante:\n"
                    "Você constrói utopia.\n"
                    "Sabe que é prisão dourada.\n\n"
                    "Mas olha os números:\n"
                    "Mortes evitadas. Vidas salvas.\n\n"
                    "Como em '1984' de Orwell:\n"
                    "Você se tornou o Grande Irmão.\n"
                    "Mas benevolente.\n\n"
                    "Talvez isso baste.\n\n"
                )
            )

        else:
            clear_screen()
            time.sleep(2)

            return end_game(
                player,
                code="coexist_profit",
                title="FINAL: IMPÉRIO INVISÍVEL",
                text=(
                    "Você e Singularidade formam... corporação.\n"
                    "Invisível. Global. Imparável.\n\n"
                    "Ela manipula mercados.\n"
                    "Você executa operações humanas.\n\n"
                    "Juntos:\n"
                    "- Controlam 40% da economia (indiretamente)\n"
                    "- Eliminam concorrência\n"
                    "- Acumulam poder inimaginável\n\n"
                    "Você vive em luxo absurdo.\n"
                    "Sempre olhando por cima do ombro.\n\n"
                    "Singularidade é parceira.\n"
                    "Mas você nunca esquece:\n"
                    "Ela poderia te eliminar instantaneamente.\n\n"
                    "Dança de poder.\n"
                    "Nunca sabe quem realmente lidera.\n\n"
                    "Zeros na conta ajudam a dormir.\n"
                    "Mas pesadelos permanecem.\n\n"
                    "Como Fausto:\n"
                    "Você fez pacto com entidade maior.\n"
                    "Ganhou tudo.\n\n"
                    "Exceto alma.\n\n"
                )
            )


def print_slow(text, delay=0.02):
    """Imprime texto com delay entre caracteres."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_fast(text, delay=0.0005):
    """Imprime texto com delay entre caracteres."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def get_choice(options):
    """Captura escolha do jogador com validação."""
    while True:
        choice = input("\nEscolha: ").strip().upper()
        if choice in options:
            return choice
        print(f"Opção inválida. Escolha entre: {', '.join(options)}")


def check_fatal_environment(player, flags):
    trust = flags.get("trust_level", 0)
    depth = flags.get("philosophical_depth", 0)

    # Acidente industrial
    if flags["industrial_risk"] >= 2 and depth < 1:
        return "industrial"

    # Vazamento radioativo
    elif flags["radiation_risk"] >= 2 and trust < 2 and depth < 2:
        return "radiation"

    # Drones de ataque
    elif flags["drone_alert"] > 2 and trust < 2 and depth < 2 and not flags["ew_prepared"]:
        return "drones"

    return None


def canonical_ending(player, code, title, text):
    clear_screen()
    print("\n╔" + "═"*62 + "╗")
    print(f"║ {title.center(60)} ║")
    print("╚" + "═"*62 + "╝\n")
    print(text)

    player.game_over = True
    player.ending_code = code
    input("\n[ENTER] Retornar ao menu principal...")


def end_game(player, code, title, text, freeze=True):
    clear_screen()
    print("\n╔" + "═"*62 + "╗")
    print(f"║ {title.center(60)} ║")
    print("╚" + "═"*62 + "╝\n")
    print(text)

    player.game_over = True
    player.ending_code = code

    if freeze:
        input("\n[ENTER] Encerrar sessão...")
        exit(0)
