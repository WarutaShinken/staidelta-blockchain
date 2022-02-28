from staidelta.util.ints import uint32, uint64

# 1 STAIDELTA coin = 1,000,000,000 = 1 billion mojo.
_mojo_per_staidelta = 1000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365
#Halving test at height 10k
initial_farmer_coeff = 20 #Initial farmer coeff must be 20 to start the chain. Multiply the prefarm by 20 to annilihate the 1 / 20 * prefarm for the genesis block.
prefarm_amount = 55882000

def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
        return uint64(int((992 / 1000) * prefarm_amount * initial_farmer_coeff * _mojo_per_staidelta))
    elif height < 1 * 500:
        return uint64(int((4) * 1 * _mojo_per_staidelta))
    elif height < 2 * _blocks_per_year:
        return uint64(int((2) * 1 * _mojo_per_staidelta))
    else:
        return uint64(int((0.875) * 1 * _mojo_per_staidelta))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
        return uint64(int((8 / 1000) * prefarm_amount * initial_farmer_coeff * _mojo_per_staidelta))
    elif height < 1 * 500:
        return uint64(int((1) * _mojo_per_staidelta))
    elif height < 2 * _blocks_per_year:
        return uint64(int((1) * _mojo_per_staidelta))
    else:
        return uint64(int((0.125) * _mojo_per_staidelta))

def calculate_base_officialwallets_reward(height: uint32) -> uint64:
    """
    Community Rewards: 1 STAIDELTA every block at stage 1 & 2 & 3
    """
    
    if height == 0:
        return uint64(int((0) * _mojo_per_staidelta))
    elif height < 1 * 500:
        return uint64(int((1) * _mojo_per_staidelta))
    elif height < 2 * _blocks_per_year:
        return uint64(int((1) * _mojo_per_staidelta))
    else:
        return uint64(int((1) * _mojo_per_staidelta))

def calculate_base_timelord_fee(height: uint32) -> uint64:
    """
    The base fee reward is 0.1% of total block reward
    !! These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously !!
    """
    if height == 0:
        return uint64(int((0) * _mojo_per_staidelta))
    elif height < 1 * 1000:
        return uint64(int((1 / 1000) * 6 * _mojo_per_staidelta))
    elif height < 2 * _blocks_per_year:
        return uint64(int((1 / 1000) * 4 * _mojo_per_staidelta))
    else:
        return uint64(int((1 / 1000) * 2 * _mojo_per_staidelta))
