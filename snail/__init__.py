from functools import cached_property
from web3 import Web3
from web3.middleware import geth_poa_middleware

from . import abi

CONTRACT_INCUBATOR = '0x09457e0181dA074610530212A6378605382764b8'


class Client:
    def __init__(
        self,
        wallet,
        web3_provider,
    ):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.wallet = wallet

    @cached_property
    def incubator_contract(self):
        return self.web3.eth.contract(
            address=self.web3.toChecksumAddress(CONTRACT_INCUBATOR), abi=abi.INCUBATOR
        )

    def get_current_coefficent(self):
        return self.incubator_contract.functions.getCurrentCoefficent().call(
            {'from': self.wallet}
        )
