<h2>Staking Detail Mod - Version 1</h2>

Due to the fact that Silicoin, Gold and Stai (staking testnet) fetch the farmer public key from every single plot, `farm summary` can take a while to run, especially when you have multiple forks competing for system resouces at the same time.

This mod provides a flag for `farm summary` that lets you control how detailed the staking information is: `-sd`/`--staking-detail`

This mod was first published here: https://github.com/zcomputerwiz/silicoin-blockchain/commit/c1d8721647d9045eb7f4a2fc8a6d9d491e8afc5b

Here is the output for `staidelta farm summary -h` that shows how to use this mod:
```
  -sd, --staking-detail INTEGER   Set the level of detail to display for staking information.
                                  Higher detail levels will make this command run slower.
                                  0 - Don't show staking information (default).
                                  1 - Show staking addresses.
                                  2 - Show staking addresses plus staked coins per address.
                                  3 - Show staking addresses plus staked coins and plot count per address.
```

Example output of `staidelta farm summary -sd 1`:
```
Farming status: Farming
Local Harvester
   974 plots of size: 96.400 TiB
Plot count for all harvesters: 974
Total size of plots: 96.400 TiB
Staking addresses:
  sit1c097dnqlx7st9ehaw4m5m3znzs629wk9r7ytrz37f8l0gdzruhyspxwfrs
  sit1l3lcz90rtlrumfcq6dcay20qhlqr0ngqa6t2ujqtfj5gdtazxfssqw2tlf
Estimated network space: 495.957 PiB
Expected time to win: 1 day and 7 hours
For details on farmed rewards and fees you should run 'sit start wallet' and 'sit wallet show'
For number of coins staked per address you should run 'sit farm summary -sd 2'
```

Additionally, it shows staking addresses for keys without plots that are accessible to the system you're running it on. This is useful if you want to stake with coins from a cold wallet.

### Install (linux)
Use `git clone https://github.com/WarutaShinken/staidelta-blockchain -b staking-detail-mod-1` to clone the repo to your machine and then run `sh install.sh` as usual.

### Note for Developers

If you're a developer who wants to incorporate this into their own fork, I suggest you wait for the next version of this mod, where I implement caching.

<p id="station"></p>
<h2>STAIDELTA - FOOD, WATER AND ELECTRICITY - WORLDWIDE</h2>

Find more about our project : https://www.station-i.de/staidelta/en

Join our growing community : https://discord.com/invite/staidelta-blockchain

Follow us on Twitter : https://twitter.com/staideltaglobal

Check our new Facebook page : https://www.facebook.com/STAIDELTAGlobal

Get our electricity : https://lumenaza.community/staideltaenergy/

<br><br>
Wallets:<br>
<a href="https://github.com/STATION-I/staidelta-blockchain/releases/download/1.1.2/StaiDelta-1.1.2.dmg">Mac Wallet</a> (1.1.2)<br>
<a href="https://github.com/STATION-I/staidelta-blockchain/releases/download/1.1.2/StaiDeltaSetup-1.1.2.exe">Windows Wallet</a> (1.1.2)<br>
<a href="https://github.com/STATION-I/staidelta-blockchain/releases/download/1.1.2/staidelta-blockchain_1.1.2_amd64.deb">Ubuntu Wallet</a> (1.1.2)<br>
<br><br>
Nodes:

<a href="https://alltheblocks.net/staidelta/peers">https://alltheblocks.net/staidelta/peers</a><br><br>
<img src="https://www.station-i.de/wp-content/uploads/2016/07/sw_zuweso_iguru_station-i_gruen.jpg"/>
<br>
STAIDELTA is technically based on the proof-of-space-and-time consensus algorithm from <a href="https://github.com/Chia-Network/chia-blockchain/">Chia Network</a>. We used also open-source Code from <a href="https://github.com/STATION-I/staidelta-blockchain">StaiDelta Chia Fork</a>, <a href="https://github.com/HiveProject2021/chives-blockchain">Chives Blockchain</a>, <a href="https://github.com/Gold-Coin-Network/goldcoin-blockchain">Goldcoin</a> and <a href="https://github.com/pinksheetscrypto/covid-blockchain">pinksheetscrypto's Chia Fork</a>.
