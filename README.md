# StaiDelta Performance Mods

- Exposed the following update intervals in `config.yaml`:
  - `UPDATE_POOL_FARMER_INFO_INTERVAL`
  - `UPDATE_HARVESTER_CACHE_INTERVAL`
- Added dynamic staking summary mod:
  - Caches staking addresses when using `-sa`/`--staking-addresses` with `farm summary`.
  - Shows the cached info when running `farm summary` without `-sa`.
  - Staking balances are shown with `-sb`/`--staking-balance` and uses cached addresses.
    - The cache is updated before the staking balances are calculated when using both `-sa` and `-sb`, meaning that combining both options will show up to date staking balances (assuming a fully synced node).

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
